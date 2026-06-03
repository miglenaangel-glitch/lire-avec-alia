from flask import Blueprint, render_template, request, jsonify, current_app
from datetime import datetime

child_bp = Blueprint('child', __name__)

# Apili progression data
LEVELS = {
    'voyelles': {
        'name': 'Les voyelles',
        'elements': [
            {'letter': 'a', 'color': 'vowel', 'gesture': 'Tu écartes les mains'},
            {'letter': 'é', 'color': 'vowel', 'gesture': 'Tu lèves le doigt'},
            {'letter': 'i', 'color': 'vowel', 'gesture': 'Montre du doigt et ris'},
            {'letter': 'o', 'color': 'vowel', 'gesture': 'Mets ta main devant ta bouche'},
            {'letter': 'u', 'color': 'vowel', 'gesture': 'Mets tes mains comme un volant'},
            {'letter': 'e', 'color': 'vowel', 'gesture': 'Mets ton index sous ta bouche'},
        ],
        'exercise_type': 'tap_to_hear',
    },
    'consonnes_1': {
        'name': 'Les consonnes',
        'consonants': ['f', 's', 'ch', 'l', 'm', 'r'],
        'vowels': ['a', 'é', 'i', 'o', 'u'],
        'exercise_type': 'slide_to_merge',
    },
    'lecture_rapide': {
        'name': 'Lecture rapide',
        'exercise_type': 'rapid_read',
    },
    'mots_simples': {
        'name': 'Les mots',
        'words': [
            {'word': 'chat', 'silent': ['t']},
            {'word': 'ami', 'silent': []},
            {'word': 'lave', 'silent': ['e']},
            {'word': 'rame', 'silent': ['e']},
            {'word': 'joli', 'silent': []},
            {'word': 'vache', 'silent': ['e']},
            {'word': 'lama', 'silent': []},
            {'word': 'vélo', 'silent': []},
            {'word': 'mari', 'silent': []},
            {'word': 'rémi', 'silent': []},
            {'word': 'fume', 'silent': ['e']},
            {'word': 'mamie', 'silent': ['e']},
            {'word': 'mur', 'silent': []},
            {'word': 'lire', 'silent': ['e']},
            {'word': 'rue', 'silent': ['e']},
            {'word': 'mare', 'silent': ['e']},
            {'word': 'vis', 'silent': ['s']},
            {'word': 'rire', 'silent': ['e']},
            {'word': 'avalé', 'silent': []},
            {'word': 'fil', 'silent': ['l']},
            {'word': 'lime', 'silent': ['e']},
            {'word': 'mal', 'silent': []},
            {'word': 'surimi', 'silent': []},
            {'word': 'folie', 'silent': ['e']},
        ],
        'exercise_type': 'word_tap',
    },
    'phrases': {
        'name': 'Les phrases',
        'sentences': [
            'Rémi lave la vache.',
            'Éva va lire.',
            'Rémi a sali le lit.',
            'Rémi a volé le rat.',
            'Rémi a vomi par la fenêtre.',
            'Éva dort sur un sac de patates.',
            'Rémi a mordu la patte du chat.',
        ],
        'exercise_type': 'sentence_read',
    },
}


def get_db():
    return current_app.extensions['mysql'].connection


@child_bp.route('/')
def home():
    mysql = current_app.extensions['mysql']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters WHERE is_active = TRUE LIMIT 1")
    character = cur.fetchone()
    cur.execute("SELECT level_key, is_locked FROM level_locks")
    locks = {r['level_key']: r['is_locked'] for r in cur.fetchall()}
    cur.close()
    return render_template('child/home.html', character=character, levels=LEVELS, locks=locks)


@child_bp.route('/exercise/<level_key>')
def exercise(level_key):
    if level_key not in LEVELS:
        return redirect(url_for('child.home'))

    mysql = current_app.extensions['mysql']
    cur = mysql.connection.cursor()

    # Check if level is locked
    cur.execute("SELECT is_locked FROM level_locks WHERE level_key = %s", (level_key,))
    lock = cur.fetchone()
    if lock and lock['is_locked']:
        cur.close()
        return redirect(url_for('child.home'))

    # Start a new session
    cur.execute(
        "INSERT INTO sessions (level) VALUES (%s)",
        (level_key,)
    )
    mysql.connection.commit()
    session_id = cur.lastrowid
    cur.close()

    level = LEVELS[level_key]
    return render_template(
        'child/exercise.html',
        level=level,
        level_key=level_key,
        session_id=session_id,
    )


@child_bp.route('/reward/<int:session_id>')
def reward(session_id):
    mysql = current_app.extensions['mysql']
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
