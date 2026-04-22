import sqlite3

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS senders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_sender(email, password):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO senders (email, password) VALUES (?, ?)",
        (email, password)
    )

    conn.commit()
    conn.close()


def get_senders():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT email, password FROM senders")
    rows = cur.fetchall()

    conn.close()

    return [{"email": r[0], "password": r[1]} for r in rows]
