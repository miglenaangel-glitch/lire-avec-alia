from flask import Blueprint, render_template, request, jsonify, current_app

parent_bp = Blueprint('parent', __name__)


def get_mysql():
    return current_app.extensions['mysql']


@parent_bp.route('/')
def dashboard():
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT DATE(started_at) as day, COUNT(*) as sessions,
               SUM(correct_answers) as correct, SUM(total_exercises) as total
        FROM sessions
        WHERE started_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
        GROUP BY DATE(started_at)
        ORDER BY day DESC
    """)
    weekly = cur.fetchall()

    cur.execute("""
        SELECT * FROM progress
        WHERE status = 'difficile'
        ORDER BY last_seen DESC
        LIMIT 10
    """)
    difficult = cur.fetchall()

    cur.execute("""
        SELECT * FROM progress
        WHERE status = 'maitrise'
        ORDER BY last_seen DESC
        LIMIT 10
    """)
    mastered = cur.fetchall()

    cur.close()
    return render_template('parent/dashboard.html', weekly=weekly, difficult=difficult, mastered=mastered)


@parent_bp.route('/progress')
def progress():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM progress ORDER BY element_type, element_value")
    all_progress = cur.fetchall()
    cur.close()
    return render_template('parent/progress.html', progress=all_progress)


@parent_bp.route('/settings')
def settings():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters ORDER BY name")
    characters = cur.fetchall()
    cur.execute("SELECT * FROM reward_phrases ORDER BY created_at DESC")
    phrases = cur.fetchall()
    cur.close()
    return render_template('parent/settings.html', characters=characters, phrases=phrases)


@parent_bp.route('/settings/character/activate/<int:char_id>', methods=['POST'])
def activate_character(char_id):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE characters SET is_active = FALSE")
    cur.execute("UPDATE characters SET is_active = TRUE WHERE id = %s", (char_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})


@parent_bp.route('/settings/phrase/add', methods=['POST'])
def add_phrase():
    data = request.get_json()
    phrase = data.get('phrase', '').strip()
    if not phrase:
        return jsonify({'error': 'Phrase vide'}), 400
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO reward_phrases (phrase) VALUES (%s)", (phrase,))
    mysql.connection.commit()
    new_id = cur.lastrowid
    cur.close()
    return jsonify({'success': True, 'id': new_id})


@parent_bp.route('/settings/phrase/delete/<int:phrase_id>', methods=['POST'])
def delete_phrase(phrase_id):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE reward_phrases SET is_active = FALSE WHERE id = %s", (phrase_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})


# ── MAILBOX ──
@parent_bp.route('/mailbox')
def mailbox():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    # Latest undownloaded postcard
    cur.execute("""
        SELECT m.id, m.earned_at, m.downloaded, p.image_path, p.label
        FROM mailbox m JOIN postcards p ON m.postcard_id = p.id
        ORDER BY m.earned_at DESC LIMIT 1
    """)
    latest = cur.fetchone()
    cur.execute("SELECT COUNT(*) as total FROM mailbox")
    total = cur.fetchone()['total']
    cur.close()
    return render_template('parent/mailbox.html', latest=latest, total=total)


@parent_bp.route('/mailbox/download/<int:mailbox_id>', methods=['POST'])
def download_postcard(mailbox_id):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE mailbox SET downloaded = TRUE WHERE id = %s", (mailbox_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})


# ── LEVELS ──
@parent_bp.route('/levels')
def levels():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT level_key, is_locked FROM level_locks ORDER BY id")
    locks = cur.fetchall()
    cur.close()
    return render_template('parent/levels.html', locks=locks)


@parent_bp.route('/levels/toggle/<level_key>', methods=['POST'])
def toggle_level(level_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO level_locks (level_key, is_locked) VALUES (%s, TRUE)
        ON DUPLICATE KEY UPDATE is_locked = NOT is_locked
    """, (level_key,))
    mysql.connection.commit()
    cur.execute("SELECT is_locked FROM level_locks WHERE level_key = %s", (level_key,))
    row = cur.fetchone()
    cur.close()
    return jsonify({'success': True, 'is_locked': bool(row['is_locked'])})


# ── DAILY REPORTS ──
@parent_bp.route('/reports')
def reports():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT * FROM daily_reports
        WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
        ORDER BY report_date DESC
    """)
    all_reports = cur.fetchall()
    cur.close()
    return render_template('parent/reports.html', reports=all_reports)
