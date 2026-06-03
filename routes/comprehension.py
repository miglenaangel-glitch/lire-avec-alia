import json
import os
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, current_app

comprehension_bp = Blueprint('comprehension', __name__)

PLAYLISTS = {
    'remi_eva': {'name': 'Rémi et Éva', 'file': 'comprehension_n1.json', 'emoji': '😄'},
    'famille':  {'name': 'Ma famille',  'file': 'comprehension_famille.json', 'emoji': '💛'},
}

# Proper names that stay black (no Apili coloring)
NEUTRAL_NAMES = {
    'alia', 'damien', 'marci', 'maxi', 'nayden', 'victor',
    'stéphanie', 'stephanie', 'dora', 'ile', 'baba-fille'
}


def get_mysql():
    return current_app.extensions['mysql']


def load_playlist(playlist_key):
    info = PLAYLISTS.get(playlist_key)
    if not info:
        return []
    path = os.path.join(current_app.static_folder, 'data', info['file'])
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_progress(playlist_key):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT text_id, total_questions, correct_answers, completed
        FROM comprehension_progress WHERE playlist = %s
    """, (playlist_key,))
    rows = cur.fetchall()
    cur.close()
    return {r['text_id']: r for r in rows}


def text_unlocked(text_idx, playlist_key, progress):
    """Text 0 always unlocked. Others need previous text ≥ 60%."""
    if text_idx == 0:
        return True
    texts = load_playlist(playlist_key)
    if text_idx >= len(texts):
        return False
    prev_id = texts[text_idx - 1]['id']
    prev = progress.get(prev_id)
    if not prev or prev['total_questions'] == 0:
        return False
    return (prev['correct_answers'] / prev['total_questions']) >= 0.60


@comprehension_bp.route('/')
def home():
    playlists_data = []
    for key, info in PLAYLISTS.items():
        texts = load_playlist(key)
        progress = get_progress(key)
        completed = sum(1 for t in texts if progress.get(t['id'], {}).get('completed'))
        playlists_data.append({
            'key': key,
            'name': info['name'],
            'emoji': info['emoji'],
            'total': len(texts),
            'completed': completed,
            'texts': [
                {
                    'id': t['id'],
                    'titre': t['titre'],
                    'difficulte': t['difficulte'],
                    'unlocked': text_unlocked(i, key, progress),
                    'progress': progress.get(t['id']),
                }
                for i, t in enumerate(texts)
            ]
        })
    return render_template('comprehension/home.html', playlists=playlists_data)


@comprehension_bp.route('/<playlist_key>/<text_id>')
def text_view(playlist_key, text_id):
    texts = load_playlist(playlist_key)
    text_data = next((t for t in texts if t['id'] == text_id), None)
    if not text_data:
        return redirect(url_for('comprehension.home'))
    # Check unlocked
    idx = next((i for i, t in enumerate(texts) if t['id'] == text_id), 0)
    progress = get_progress(playlist_key)
    if not text_unlocked(idx, playlist_key, progress):
        return redirect(url_for('comprehension.home'))
    return render_template('comprehension/text.html',
        text=text_data,
        playlist_key=playlist_key,
        neutral_names=list(NEUTRAL_NAMES))


@comprehension_bp.route('/api/record', methods=['POST'])
def record():
    data = request.get_json()
    playlist = data.get('playlist')
    text_id = data.get('text_id')
    correct = int(data.get('correct', 0))
    total = int(data.get('total', 0))

    mysql = get_mysql()
    cur = mysql.connection.cursor()
    completed = (total > 0 and correct / total >= 0.60)
    cur.execute("""
        INSERT INTO comprehension_progress (playlist, text_id, total_questions, correct_answers, completed)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            total_questions = %s,
            correct_answers = %s,
            completed = %s,
            completed_at = IF(%s AND completed_at IS NULL, NOW(), completed_at)
    """, (playlist, text_id, total, correct, completed,
          total, correct, completed, completed))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True, 'completed': completed})
