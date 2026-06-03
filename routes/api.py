from flask import Blueprint, request, jsonify, current_app
import requests as http
from config import Config

api_bp = Blueprint('api', __name__)

ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'


def claude(prompt):
    resp = http.post(
        ANTHROPIC_URL,
        headers={
            'x-api-key': Config.ANTHROPIC_API_KEY,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json',
        },
        json={
            'model': Config.CLAUDE_MODEL,
            'max_tokens': Config.CLAUDE_MAX_TOKENS,
            'messages': [{'role': 'user', 'content': prompt}],
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()['content'][0]['text'].strip()


def get_mysql():
    return current_app.extensions['mysql']


@api_bp.route('/session-end', methods=['POST'])
def session_end():
    """Record ended_at for a session — called via sendBeacon on page unload."""
    try:
        data = request.get_json(force=True, silent=True) or {}
        session_id = data.get('session_id')
        if session_id:
            mysql = get_mysql()
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE sessions SET ended_at = NOW()
                WHERE id = %s AND ended_at IS NULL
            """, (session_id,))
            mysql.connection.commit()
            cur.close()
    except Exception:
        pass
    return '', 204


@api_bp.route('/last-visit', methods=['GET'])
def last_visit():
    """Return hours since last session — for 24h absence video check."""
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT MAX(started_at) as last FROM sessions")
    row = cur.fetchone()
    cur.close()
    if not row or not row['last']:
        return jsonify({'hours_ago': None})
    from datetime import datetime
    diff = datetime.utcnow() - row['last']
    hours = diff.total_seconds() / 3600
    return jsonify({'hours_ago': round(hours, 1)})


@api_bp.route('/record', methods=['POST'])
def record_answer():
    data = request.get_json()
    element_type = data.get('element_type')
    element_value = data.get('element_value')
    correct = bool(data.get('correct'))
    session_id = data.get('session_id')

    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO progress (element_type, element_value, attempts, correct, last_seen)
        VALUES (%s, %s, 1, %s, NOW())
        ON DUPLICATE KEY UPDATE
          attempts = attempts + 1,
          correct = correct + %s,
          last_seen = NOW()
    """, (element_type, element_value, 1 if correct else 0, 1 if correct else 0))

    cur.execute("""
        UPDATE progress SET status = CASE
          WHEN correct >= 5 AND (correct / attempts) >= 0.8 THEN 'maitrise'
          WHEN attempts >= 2 AND (correct / attempts) < 0.5 THEN 'difficile'
          WHEN attempts >= 1 THEN 'en_cours'
          ELSE 'nouveau'
        END
        WHERE element_type = %s AND element_value = %s
    """, (element_type, element_value))

    if session_id:
        cur.execute("""
            UPDATE sessions
            SET total_exercises = total_exercises + 1,
                correct_answers = correct_answers + %s
            WHERE id = %s
        """, (1 if correct else 0, session_id))

    mysql.connection.commit()

    session = None
    if session_id:
        cur.execute("SELECT total_exercises, correct_answers FROM sessions WHERE id = %s", (session_id,))
        session = cur.fetchone()

    cur.close()

    show_reward = False
    new_postcard = False

    # Per-level reward thresholds
    thresholds = {
        'phrases': 15,
        'mots_simples': 20,
        'lecture_rapide': 20,
        'consonnes_1': 25,
        'voyelles': 999,  # voyelles has its own completion logic
    }
    if session_id and session:
        cur2 = get_mysql().connection.cursor()
        cur2.execute("SELECT level FROM sessions WHERE id = %s", (session_id,))
        sess_row = cur2.fetchone()
        cur2.close()
        level_key = sess_row['level'] if sess_row else ''
        threshold = thresholds.get(level_key, 20)
        if session['total_exercises'] >= threshold:
            accuracy = session['correct_answers'] / session['total_exercises']
            show_reward = accuracy >= Config.REWARD_MIN_ACCURACY

    # Check if this session qualifies (≥70% accuracy) and award postcard every 3 such sessions
    if session_id and session and session['total_exercises'] >= 5:
        accuracy = session['correct_answers'] / session['total_exercises']
        if accuracy >= Config.REWARD_MIN_ACCURACY:
            cur2 = get_mysql().connection.cursor()
            # Count successful sessions total
            cur2.execute("""
                SELECT COUNT(*) as cnt FROM sessions
                WHERE correct_answers >= total_exercises * 0.7
                AND total_exercises >= 5
            """)
            row = cur2.fetchone()
            count = row['cnt'] if row else 0
            # Award postcard on every 3rd successful session
            if count > 0 and count % 3 == 0:
                # Pick next postcard (rotate)
                cur2.execute("""
                    SELECT p.id FROM postcards p
                    WHERE p.is_active = TRUE
                    AND p.id NOT IN (
                        SELECT postcard_id FROM mailbox ORDER BY earned_at DESC LIMIT 1
                    )
                    ORDER BY RAND() LIMIT 1
                """)
                pc = cur2.fetchone()
                if not pc:
                    # All used — pick any active
                    cur2.execute("SELECT id FROM postcards WHERE is_active=TRUE ORDER BY RAND() LIMIT 1")
                    pc = cur2.fetchone()
                if pc:
                    cur2.execute("INSERT INTO mailbox (postcard_id) VALUES (%s)", (pc['id'],))
                    get_mysql().connection.commit()
                    new_postcard = True
            cur2.close()

    return jsonify({'success': True, 'show_reward': show_reward, 'new_postcard': new_postcard})


@api_bp.route('/generate-sentences', methods=['POST'])
def generate_sentences():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT element_value FROM progress
        WHERE element_type IN ('syllabe', 'voyelle') AND status = 'maitrise'
    """)
    mastered = [r['element_value'] for r in cur.fetchall()]
    cur.close()

    if not mastered:
        mastered = ['a', 'é', 'i', 'o', 'u', 'ma', 'la', 'ra', 'sa']

    prompt = """Tu es un assistant pédagogique qui aide une enfant de 13 ans avec un implant cochléaire à apprendre à lire en français.
Tu suis la méthode Apili (syllabique et gestuelle).

Génère 5 phrases courtes et AMUSANTES dans le style d'Apili, avec les personnages Rémi et Éva.
Les phrases doivent utiliser UNIQUEMENT les syllabes déjà maîtrisées: {syls}
Format: une phrase par ligne, sans numérotation.
Les phrases doivent être drôles — c'est le principe central de la méthode Apili.""".format(syls=', '.join(mastered))

    text = claude(prompt)
    sentences = [s.strip() for s in text.split('\n') if s.strip()]
    return jsonify({'sentences': sentences})


@api_bp.route('/progress-summary', methods=['GET'])
def progress_summary():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT element_type, element_value, attempts, correct, status FROM progress ORDER BY element_type, status")
    rows = cur.fetchall()
    cur.close()

    if not rows:
        return jsonify({'summary': 'Pas encore de données de progression.'})

    # Limit to 50 most recent elements to avoid prompt size issues
    rows = rows[:50]
    maitrise = [r['element_value'] for r in rows if r['status'] == 'maitrise']
    difficile = [r['element_value'] for r in rows if r['status'] == 'difficile']
    en_cours = [r['element_value'] for r in rows if r['status'] == 'en_cours']

    prompt = (
        "Tu es un assistant pedagogique. Ecris un resume de 3-4 phrases en francais "
        "pour la maman d'Alia (13 ans, implant cochleaire, methode Apili).\n"
        "Maitrise: " + ", ".join(maitrise[:20]) + "\n"
        "Difficile: " + ", ".join(difficile[:20]) + "\n"
        "En cours: " + ", ".join(en_cours[:20]) + "\n"
        "Sois encourageant et donne un conseil concret pour la prochaine seance."
    )

    try:
        summary = claude(prompt)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'summary': 'Résumé temporairement indisponible. Les données sont bien enregistrées.'})
