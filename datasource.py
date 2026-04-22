import sqlite3
import requests
from config import API_KEY

DB_NAME = "emails.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT,
            used INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def fetch_from_api(count=10):
    url = "https://randommer.io/api/Email/Generate"

    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "number": count
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data
    except:
        return []
    

def save_to_db(emails):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for email in emails:
        cursor.execute(
            "INSERT INTO emails (email, password) VALUES (?, ?)",
            (email, "default_pass")
        )

    conn.commit()
    conn.close()


def get_emails(limit=10):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT email, password FROM emails WHERE used=0 LIMIT ?",
        (limit,)
    )

    rows = cursor.fetchall()

    # помечаем как использованные
    cursor.execute(
        "UPDATE emails SET used=1 WHERE id IN (SELECT id FROM emails LIMIT ?)",
        (limit,)
    )

    conn.commit()
    conn.close()

    return rows


def get_or_generate(limit=10):
    emails = get_emails(limit)

    if len(emails) < limit:
        new_emails = fetch_from_api(limit)
        save_to_db(new_emails)
        emails = get_emails(limit)

    return emails
