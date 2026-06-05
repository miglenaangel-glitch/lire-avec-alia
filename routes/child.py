import json
from flask import Blueprint, render_template, redirect, url_for, current_app
from datetime import datetime

child_bp = Blueprint('child', __name__)


def get_mysql():
    return current_app.extensions['mysql']


def _build_level(row, content_rows):
    """Build a level dict from DB rows — same format as the old hardcoded LEVELS."""
    level_key = row['level_key']
    exercise_type = row['exercise_type']
    name = row['name_fr']

    base = {'name': name, 'exercise_type': exercise_type}

    if exercise_type == 'tap_to_hear':
        elements = []
        for c in sorted(content_rows, key=lambda r: r['order_index']):
            if c['type'] == 'letter':
                elements.append(json.loads(c['value']))
        base['elements'] = elements

    elif exercise_type == 'slide_to_merge':
        consonants = [c['value'] for c in content_rows
                      if c['type'] == 'letter']
        vowels = [c['value'] for c in content_rows
                  if c['type'] == 'syllable' and c['order_index'] < 20]
        base['consonants'] = consonants
        base['vowels'] = vowels
        # words and sentences for consonnes_2 and later levels
        words = [json.loads(c['value']) for c in
                 sorted([c for c in content_rows if c['type'] == 'word'],
                        key=lambda r: r['order_index'])]
        sentences = [c['value'] for c in
                     sorted([c for c in content_rows if c['type'] == 'sentence'],
                             key=lambda r: r['order_index'])]
        if words:
            base['words'] = words
        if sentences:
            base['sentences'] = sentences

    elif exercise_type == 'rapid_read':
        pass  # syllables generated in JS

    elif exercise_type == 'word_tap':
        words = [json.loads(c['value']) for c in
                 sorted([c for c in content_rows if c['type'] == 'word'],
                        key=lambda r: r['order_index'])]
        base['words'] = words

    elif exercise_type == 'sentence_read':
        sentences = [c['value'] for c in
                     sorted([c for c in content_rows if c['type'] == 'sentence'],
                             key=lambda r: r['order_index'])]
        base['sentences'] = sentences

    elif exercise_type == 'number_match':
        numbers = [json.loads(c['value']) for c in
                   sorted([c for c in content_rows if c['type'] == 'word'],
                           key=lambda r: r['order_index'])]
        base['numbers'] = numbers

    return base


def load_levels_from_db():
    """Load all unlocked levels from DB and return dict keyed by level_key."""
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM levels ORDER BY block, order_index")
    level_rows = cur.fetchall()

    # Load all content in one query
    cur.execute("SELECT * FROM level_content ORDER BY level_key, order_index")
    all_content = cur.fetchall()
    cur.close()

    # Group content by level_key
    content_by_level = {}
    for c in all_content:
        content_by_level.setdefault(c['level_key'], []).append(c)

    levels = {}
    for row in level_rows:
        key = row['level_key']
        content = content_by_level.get(key, [])
        levels[key] = _build_level(row, content)

    return levels


def get_db():
    return current_app.extensions['mysql'].connection


@child_bp.route('/')
def home():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters WHERE is_active = TRUE LIMIT 1")
    character = cur.fetchone()
    # Combine level_locks + levels.is_unlocked
    cur.execute("""
        SELECT l.level_key,
               COALESCE(ll.is_locked, IF(l.is_unlocked, 0, 1)) AS is_locked
        FROM levels l
        LEFT JOIN level_locks ll ON ll.level_key = l.level_key
    """)
    locks = {r['level_key']: bool(r['is_locked']) for r in cur.fetchall()}

    # Load today's daily assignment
    from datetime import date, timedelta
    today = date.today().isoformat()
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    cur.execute("SELECT exercise_key FROM daily_assignment WHERE assigned_date = %s", (today,))
    daily = cur.fetchall()
    if not daily:
        cur.execute("SELECT exercise_key FROM daily_assignment WHERE assigned_date = %s", (yesterday,))
        daily = cur.fetchall()
    daily_keys = {r['exercise_key'] for r in daily}
    cur.close()

    levels = load_levels_from_db()
    return render_template('child/home.html', character=character, levels=levels, locks=locks,
                           daily_keys=daily_keys, has_daily=bool(daily_keys))


@child_bp.route('/exercise/<level_key>')
def exercise(level_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    # Verify level exists in DB
    cur.execute("SELECT * FROM levels WHERE level_key = %s", (level_key,))
    level_row = cur.fetchone()
    if not level_row:
        cur.close()
        return redirect(url_for('child.home'))

    # Check if level is locked (level_locks table)
    cur.execute("SELECT is_locked FROM level_locks WHERE level_key = %s", (level_key,))
    lock = cur.fetchone()
    if lock and lock['is_locked']:
        cur.close()
        return redirect(url_for('child.home'))

    # Load content for this level only
    cur.execute("SELECT * FROM level_content WHERE level_key = %s ORDER BY order_index",
                (level_key,))
    content_rows = cur.fetchall()

    # Start a new session
    cur.execute("INSERT INTO sessions (level) VALUES (%s)", (level_key,))
    mysql.connection.commit()
    session_id = cur.lastrowid
    cur.close()

    level = _build_level(level_row, content_rows)
    return render_template(
        'child/exercise.html',
        level=level,
        level_key=level_key,
        session_id=session_id,
    )


@child_bp.route('/reward/<int:session_id>')
def reward(session_id):
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM characters WHERE is_active = TRUE LIMIT 1")
    character = cur.fetchone()

    cur.execute("SELECT phrase FROM reward_phrases WHERE is_active = TRUE ORDER BY RAND() LIMIT 1")
    phrase_row = cur.fetchone()
    phrase = phrase_row['phrase'] if phrase_row else 'Bravo Alia !'

    cur.execute(
        "UPDATE sessions SET reward_shown = TRUE, ended_at = NOW() WHERE id = %s",
        (session_id,)
    )
    mysql.connection.commit()
    cur.close()

    return render_template('child/reward.html', character=character, phrase=phrase)
