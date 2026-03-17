import sqlite3

def connect():
    return sqlite3.connect("interns.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        department TEXT
    )
    """)

    # algorithm optimization (index)
    cursor.execute(
        "CREATE INDEX IF NOT EXISTS idx_department ON interns(department)"
    )

    conn.commit()
    conn.close()