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
    if session and session['total_exercises'] >= 5:
        accuracy = session['correct_answers'] / session['total_exercises']
        show_reward = accuracy >= Config.REWARD_MIN_ACCURACY

    return jsonify({'success': True, 'show_reward': show_reward})


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

    progress_text = '\n'.join(
        "{val} ({typ}): {c}/{a} — {s}".format(
            val=r['element_value'], typ=r['element_type'],
            c=r['correct'], a=r['attempts'], s=r['status']
        )
        for r in rows
    )

    prompt = """Voici les données de progression d'Alia pour cette semaine:
{data}

Écris un bref résumé (3-4 phrases) pour sa maman, en français, expliquant:
- Ce qu'Alia maîtrise bien
- Ce qui lui pose encore des difficultés
- Un conseil concret pour la prochaine séance
Sois encourageant et précis.""".format(data=progress_text)

    return jsonify({'summary': claude(prompt)})
