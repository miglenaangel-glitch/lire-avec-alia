#!/usr/bin/env python3
"""Daily report generator — runs at 21:00 via cron."""
import sys
import os
sys.path.insert(0, '/var/www/lire-avec-alia')

from datetime import date, datetime, timedelta
import MySQLdb
import MySQLdb.cursors
import requests as http
from dotenv import load_dotenv

load_dotenv('/var/www/lire-avec-alia/.env')

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')
CLAUDE_MODEL = 'claude-sonnet-4-20250514'

def get_db():
    return MySQLdb.connect(
        host=MYSQL_HOST, user=MYSQL_USER,
        passwd=MYSQL_PASSWORD, db=MYSQL_DB,
        charset='utf8mb4',
        cursorclass=MySQLdb.cursors.DictCursor
    )

def claude(prompt):
    resp = http.post(
        'https://api.anthropic.com/v1/messages',
        headers={
            'x-api-key': ANTHROPIC_API_KEY,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json',
        },
        json={
            'model': CLAUDE_MODEL,
            'max_tokens': 800,
            'messages': [{'role': 'user', 'content': prompt}],
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()['content'][0]['text'].strip()

def generate_report():
    today = date.today()
    db = get_db()
    cur = db.cursor()

    # Check if report already exists
    cur.execute("SELECT id FROM daily_reports WHERE report_date = %s", (today,))
    if cur.fetchone():
        print(f"Report for {today} already exists.")
        cur.close(); db.close()
        return

    # Check if Alia worked today
    cur.execute("""
        SELECT COUNT(*) as cnt, SUM(total_exercises) as total,
               SUM(correct_answers) as correct
        FROM sessions
        WHERE DATE(started_at) = %s AND total_exercises > 0
    """, (today,))
    today_sessions = cur.fetchone()
    worked = today_sessions['cnt'] > 0 if today_sessions else False

    if not worked:
        summary = "Alia n'a pas travaillé aujourd'hui. Pas de séance enregistrée."
        cur.execute(
            "INSERT INTO daily_reports (report_date, worked, summary) VALUES (%s, FALSE, %s)",
            (today, summary)
        )
        db.commit()
        print(f"Report saved: no work today.")
        cur.close(); db.close()
        return

    # Get detailed stats
    cur.execute("""
        SELECT element_type, element_value, attempts, correct, status
        FROM progress
        WHERE last_seen >= %s
        ORDER BY element_type, status
    """, (today,))
    progress = cur.fetchall()

    cur.execute("""
        SELECT level, total_exercises, correct_answers
        FROM sessions
        WHERE DATE(started_at) = %s AND total_exercises > 0
    """, (today,))
    sessions = cur.fetchall()

    # Delete reports older than 30 days
    cur.execute("DELETE FROM daily_reports WHERE created_at < DATE_SUB(NOW(), INTERVAL 30 DAY)")
    db.commit()

    # Build context for Claude
    sessions_text = '\n'.join(
        f"- {s['level']}: {s['correct_answers']}/{s['total_exercises']} ({int(s['correct_answers']/s['total_exercises']*100) if s['total_exercises'] else 0}%)"
        for s in sessions
    )
    progress_text = '\n'.join(
        f"- {p['element_value']} ({p['element_type']}): {p['correct']}/{p['attempts']} — {p['status']}"
        for p in progress
    ) if progress else "Pas de données de progression détaillées."

    prompt = f"""Tu es un assistant pédagogique qui aide une enfant de 13 ans avec un implant cochléaire à apprendre à lire en français (méthode Apili).

Voici les données de la journée du {today.strftime('%d/%m/%Y')} :

Séances :
{sessions_text}

Éléments travaillés aujourd'hui :
{progress_text}

Écris un rapport quotidien (5-7 phrases) pour la maman d'Alia, en français, incluant :
1. Ce qu'Alia a travaillé aujourd'hui (niveaux, exercices)
2. Ses réussites (éléments maîtrisés ou bien réussis)
3. Ses difficultés (éléments échoués ou difficiles)
4. Une recommandation concrète pour demain
5. Un mot d'encouragement pour la maman

Sois précis, bienveillant et professionnel."""

    summary = claude(prompt)
    cur.execute(
        "INSERT INTO daily_reports (report_date, worked, summary) VALUES (%s, TRUE, %s)",
        (today, summary)
    )
    db.commit()
    print(f"Report saved for {today}.")
    cur.close()
    db.close()

if __name__ == '__main__':
    generate_report()
