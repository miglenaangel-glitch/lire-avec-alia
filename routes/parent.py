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
