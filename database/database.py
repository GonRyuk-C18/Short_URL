import sqlite3


def create_db ():
    db_file = "short_url.db"
    conection = sqlite3.connect(db_file)
    cursor = conection.cursor()
    cursor.execute('''CREATE TABLE  IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    long_url TEXT NOT NULL,
    short_url TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hits INTEGER DEFAULT 0)''')

    conection.commit()
    conection.close()
