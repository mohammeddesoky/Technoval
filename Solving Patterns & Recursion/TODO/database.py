import sqlite3

def connect():
    conn = sqlite3.connect("tasks.db")
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()