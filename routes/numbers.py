import json
import os
from flask import Blueprint, render_template, request, jsonify, current_app, redirect, url_for

numbers_bp = Blueprint('numbers', __name__)

MASTERY = {
    'n1': {'min_correct': 3, 'min_accuracy': 0.90},
    'n2': {'min_correct': 3, 'min_accuracy': 0.80},
    'n3': {'min_correct': 5, 'min_accuracy': 0.80},
    'n4': {'min_correct': 5, 'min_accuracy': 0.80},
    'n5': {'min_correct': 3, 'min_accuracy': 0.75},
}


def get_mysql():
    return current_app.extensions['mysql']


def load_numbers():
    path = os.path.join(current_app.static_folder, 'data', 'numbers_fr.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_level_status(level):
    """Return dict of {number_value: progress_row} for a level."""
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT number_value, attempts, correct, mastered
        FROM numbers_progress WHERE level = %s
    """, (level,))
    rows = cur.fetchall()
    cur.close()
    return {r['number_value']: r for r in rows}


def is_unlocked(level_key):
    """Check if a numbers level is unlocked."""
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT is_unlocked FROM levels WHERE level_key = %s", (level_key,))
    row = cur.fetchone()
    cur.close()
    if not row:
        return False
    # Also check level_locks override
    cur2 = get_mysql().connection.cursor()
    cur2.execute("SELECT is_locked FROM level_locks WHERE level_key = %s", (level_key,))
    lock = cur2.fetchone()
    cur2.close()
    if lock:
        return not bool(lock['is_locked'])
    return bool(row['is_unlocked'])


@numbers_bp.route('/')
def home():
    data = load_numbers()
    levels_info = [
        {'key': 'nombres_n1', 'level': 'n1', 'name': 'Les nombres 0–10',   'range': '0–10',   'count': len(data['n1'])},
        {'key': 'nombres_n2', 'level': 'n2', 'name': 'Les nombres 11–20',  'range': '11–20',  'count': len(data['n2'])},
        {'key': 'nombres_n3', 'level': 'n3', 'name': 'Les dizaines 21–69', 'range': '21–69',  'count': len(data['n3'])},
        {'key': 'nombres_n4', 'level': 'n4', 'name': 'Les nombres 70–99',  'range': '70–99',  'count': len(data['n4'])},
        {'key': 'nombres_n5', 'level': 'n5', 'name': 'Les centaines',      'range': '100+',   'count': len(data['n5'])},
    ]
    for lvl in levels_info:
        lvl['unlocked'] = is_unlocked(lvl['key'])
        status = get_level_status(lvl['level'])
        lvl['mastered'] = sum(1 for v in status.values() if v['mastered'])
    return render_template('numbers/home.html', levels=levels_info)


@numbers_bp.route('/n<int:n>/match')
def match(n):
    level = f'n{n}'
    if not is_unlocked(f'nombres_{level}'):
        return redirect(url_for('numbers.home'))
    data = load_numbers()
    numbers = data.get(level, [])
    humor = data['humor'].get(level, [])
    return render_template('numbers/match.html', numbers=numbers, level=level, humor=humor)


@numbers_bp.route('/n<int:n>/spell')
def spell(n):
    level = f'n{n}'
    if not is_unlocked(f'nombres_{level}'):
        return redirect(url_for('numbers.home'))
    data = load_numbers()
    numbers = data.get(level, [])
    return render_template('numbers/spell.html', numbers=numbers, level=level)


@numbers_bp.route('/n2/gallery')
def gallery():
    if not is_unlocked('nombres_n2'):
        return redirect(url_for('numbers.home'))
    data = load_numbers()
    irregular = [n for n in data['n2'] if n.get('irregular')]
    humor = data['humor'].get('n2', [])
    return render_template('numbers/gallery.html', numbers=irregular, humor=humor)


@numbers_bp.route('/n2/vingt')
def vingt():
    if not is_unlocked('nombres_n2'):
        return redirect(url_for('numbers.home'))
    return render_template('numbers/vingt.html')


@numbers_bp.route('/api/record', methods=['POST'])
def record():
    data = request.get_json()
    level = data.get('level')
    number_value = int(data.get('number_value', 0))
    word_form = data.get('word_form', '')
    correct = bool(data.get('correct'))
    error_type = data.get('error_type', '')

    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO numbers_progress (level, number_value, word_form, attempts, correct)
        VALUES (%s, %s, %s, 1, %s)
        ON DUPLICATE KEY UPDATE
            attempts = attempts + 1,
            correct = correct + %s,
            last_error_type = IF(%s = '', last_error_type, %s)
    """, (level, number_value, word_form,
          1 if correct else 0,
          1 if correct else 0,
          error_type, error_type))

    # Update mastered flag
    m = MASTERY.get(level, {'min_correct': 3, 'min_accuracy': 0.80})
    cur.execute("""
        UPDATE numbers_progress
        SET mastered = (correct >= %s AND correct/attempts >= %s)
        WHERE level = %s AND number_value = %s
    """, (m['min_correct'], m['min_accuracy'], level, number_value))

    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})
