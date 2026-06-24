from flask import Blueprint, render_template, request, jsonify, current_app, session, redirect, url_for

parent_bp = Blueprint('parent', __name__)


def get_mysql():
    return current_app.extensions['mysql']


def parent_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('parent_logged_in'):
            return redirect(url_for('parent.login'))
        return f(*args, **kwargs)
    return decorated


@parent_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password', '')
        mysql = get_mysql()
        cur = mysql.connection.cursor()
        cur.execute("SELECT setting_value FROM parent_settings WHERE setting_key='password'")
        row = cur.fetchone()
        cur.close()
        stored = row['setting_value'] if row else 'maman'
        if password == stored:
            session['parent_logged_in'] = True
            return redirect(url_for('parent.dashboard'))
        error = 'Mot de passe incorrect.'
    return render_template('parent/login.html', error=error)


@parent_bp.route('/logout')
def logout():
    session.pop('parent_logged_in', None)
    return redirect(url_for('parent.login'))


@parent_bp.route('/')
@parent_required
def dashboard():
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT DATE(started_at) as day, COUNT(*) as sessions,
               SUM(correct_answers) as correct, SUM(total_exercises) as total,
               ROUND(SUM(
                 TIMESTAMPDIFF(SECOND, started_at, COALESCE(ended_at, started_at))
               ) / 60) as minutes
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
@parent_required
def progress():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM progress ORDER BY element_type, element_value")
    all_progress = cur.fetchall()
    cur.close()
    return render_template('parent/progress.html', progress=all_progress)


@parent_bp.route('/settings')
@parent_required
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
@parent_required
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
@parent_required
def levels():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    # Read from new `levels` table — is_unlocked=FALSE means locked
    # Also check level_locks for manual overrides
    cur.execute("""
        SELECT l.level_key, l.name_fr, l.block, l.order_index,
               l.is_unlocked,
               COALESCE(ll.is_locked, NOT l.is_unlocked) AS is_locked
        FROM levels l
        LEFT JOIN level_locks ll ON ll.level_key = l.level_key
        ORDER BY l.block, l.order_index
    """)
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


@parent_bp.route('/comprehension')
@parent_required
def comprehension_unlocks():
    import json, os
    from routes.comprehension import PLAYLISTS, get_overrides
    mysql = get_mysql()
    overrides = get_overrides()
    playlists_data = []
    for key, info in PLAYLISTS.items():
        path = os.path.join(current_app.static_folder, 'data', info['file'])
        with open(path, 'r', encoding='utf-8') as f:
            texts = json.load(f)
        playlists_data.append({
            'key': key,
            'name': info['name'],
            'texts': [
                {
                    'id': t['id'],
                    'titre': t['titre'],
                    'level_key': f"comp_{key}_{t['id']}",
                    'is_locked': overrides.get(f"comp_{key}_{t['id']}"),
                }
                for t in texts
            ]
        })
    return render_template('parent/comprehension_unlocks.html', playlists=playlists_data)


@parent_bp.route('/comprehension/unlock/<level_key>', methods=['POST'])
@parent_required
def comprehension_force_unlock(level_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO level_locks (level_key, is_locked) VALUES (%s, FALSE)
        ON DUPLICATE KEY UPDATE is_locked = FALSE
    """, (level_key,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})


@parent_bp.route('/comprehension/reset/<level_key>', methods=['POST'])
@parent_required
def comprehension_reset_unlock(level_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM level_locks WHERE level_key = %s", (level_key,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})


# ── DAILY ASSIGNMENT ──

# All available exercises mama can assign
ALL_EXERCISES = [
    # Bloc 1
    {'key': 'voyelles',       'name': 'Les voyelles',        'url': '/child/exercise/voyelles',       'group': 'Bloc 1'},
    {'key': 'consonnes_1',    'name': 'Les consonnes',       'url': '/child/exercise/consonnes_1',    'group': 'Bloc 1'},
    {'key': 'lecture_rapide', 'name': 'Lecture rapide',      'url': '/child/exercise/lecture_rapide', 'group': 'Bloc 1'},
    {'key': 'mots_simples',   'name': 'Les mots',            'url': '/child/exercise/mots_simples',   'group': 'Bloc 1'},
    {'key': 'phrases',        'name': 'Les phrases',         'url': '/child/exercise/phrases',        'group': 'Bloc 1'},
    # Bloc 2
    {'key': 'consonnes_2',    'name': 'Les consonnes 2',     'url': '/child/exercise/consonnes_2',    'group': 'Bloc 2'},
    {'key': 'lecture_rapide_2','name': 'Lecture rapide 2',   'url': '/child/exercise/lecture_rapide_2','group': 'Bloc 2'},
    {'key': 'mots_2',         'name': 'Les mots 2',          'url': '/child/exercise/mots_2',         'group': 'Bloc 2'},
    {'key': 'phrases_2',      'name': 'Les phrases 2',       'url': '/child/exercise/phrases_2',      'group': 'Bloc 2'},
    # Nombres
    {'key': 'nombres_n1',     'name': 'Les nombres 0–10',    'url': '/numbers/n1/match',              'group': 'Les Nombres'},
    {'key': 'nombres_n1_spell','name': 'Épeler 0–10',        'url': '/numbers/n1/spell',              'group': 'Les Nombres'},
    {'key': 'nombres_n2',     'name': 'Les nombres 11–20',   'url': '/numbers/n2/match',              'group': 'Les Nombres'},
    {'key': 'nombres_n2_gallery','name': 'Galerie irréguliers','url': '/numbers/n2/gallery',          'group': 'Les Nombres'},
    {'key': 'nombres_n2_vingt','name': 'Le piège de vingt',  'url': '/numbers/n2/vingt',              'group': 'Les Nombres'},
    # Compréhension
    {'key': 'comp_remi_eva',  'name': 'Compréhension Rémi/Éva', 'url': '/comprehension/playlist/remi_eva', 'group': 'Compréhension'},
    {'key': 'comp_famille',   'name': 'Ma famille',          'url': '/comprehension/playlist/famille', 'group': 'Compréhension'},
]


@parent_bp.route('/daily')
@parent_required
def daily():
    from datetime import date
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    today = date.today().isoformat()
    cur.execute("SELECT * FROM daily_assignment WHERE assigned_date = %s ORDER BY order_index", (today,))
    today_assignments = cur.fetchall()
    cur.close()
    assigned_keys = {a['exercise_key'] for a in today_assignments}
    return render_template('parent/daily.html',
        exercises=ALL_EXERCISES,
        assigned_keys=assigned_keys,
        today=today,
        today_assignments=today_assignments)


@parent_bp.route('/daily/save', methods=['POST'])
@parent_required
def daily_save():
    from datetime import date
    data = request.get_json()
    selected = data.get('exercises', [])  # list of exercise keys
    today = date.today().isoformat()
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    # Clear today's assignments
    cur.execute("DELETE FROM daily_assignment WHERE assigned_date = %s", (today,))
    # Insert new ones
    ex_map = {e['key']: e for e in ALL_EXERCISES}
    for i, key in enumerate(selected):
        ex = ex_map.get(key)
        if ex:
            cur.execute("""
                INSERT INTO daily_assignment (exercise_key, exercise_name, exercise_url, assigned_date, order_index)
                VALUES (%s, %s, %s, %s, %s)
            """, (key, ex['name'], ex['url'], today, i))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True, 'count': len(selected)})


# ── DAILY REPORTS ──
@parent_bp.route('/reports')
@parent_required
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


@parent_bp.route('/numbers')
@parent_required
def numbers_dashboard():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT level, SUM(attempts) as total_attempts,
               SUM(correct) as total_correct,
               SUM(mastered) as mastered_count,
               COUNT(*) as seen_count
        FROM numbers_progress GROUP BY level ORDER BY level
    """)
    stats = {r['level']: r for r in cur.fetchall()}
    cur.execute("""
        SELECT level, word_form, last_error_type, attempts, correct
        FROM numbers_progress
        WHERE mastered = FALSE AND attempts >= 3 AND correct/attempts < 0.5
        ORDER BY level, attempts DESC LIMIT 10
    """)
    difficulties = cur.fetchall()
    cur.close()
    levels_info = [
        {'level': 'n1', 'name': '0–10',   'key': 'nombres_n1'},
        {'level': 'n2', 'name': '11–20',  'key': 'nombres_n2'},
        {'level': 'n3', 'name': '21–69',  'key': 'nombres_n3'},
        {'level': 'n4', 'name': '70–99',  'key': 'nombres_n4'},
        {'level': 'n5', 'name': '100+',   'key': 'nombres_n5'},
    ]
    return render_template('parent/numbers.html',
        stats=stats, difficulties=difficulties, levels_info=levels_info)


@parent_bp.route('/levels/content/<level_key>')
@parent_required
def level_content(level_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM levels WHERE level_key = %s", (level_key,))
    level = cur.fetchone()
    cur.execute("""
        SELECT type, value, order_index FROM level_content
        WHERE level_key = %s ORDER BY type, order_index
    """, (level_key,))
    content = cur.fetchall()
    cur.close()
    if not level:
        return jsonify({'error': 'Not found'}), 404
    import json
    result = {'name': level['name_fr'], 'exercise_type': level['exercise_type'], 'items': []}
    for c in content:
        item = {'type': c['type'], 'value': c['value']}
        if c['type'] in ('word', 'letter') and c['value'].startswith('{'):
            try:
                item['parsed'] = json.loads(c['value'])
            except:
                pass
        result['items'].append(item)
    return jsonify(result)


@parent_bp.route('/settings/password', methods=['POST'])
@parent_required
def change_password():
    data = request.get_json()
    new_pass = data.get('password', '').strip()
    if len(new_pass) < 4:
        return jsonify({'error': 'Mot de passe trop court (4 caractères minimum).'}), 400
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO parent_settings (setting_key, setting_value) VALUES ('password', %s)
        ON DUPLICATE KEY UPDATE setting_value = %s
    """, (new_pass, new_pass))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})
