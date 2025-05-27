import sqlite3

db_file = "short_url.db"

def create_db ():
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

def insert_url(long_url, short_url):
    conection = sqlite3.connect(db_file)
    cursor = conection.cursor()
    try:
        cursor.execute(
            'INSERT INTO urls (long_url, short_url) VALUES (?, ?)', (long_url, short_url)
        )
        conection.commit()
    except sqlite3.IntegrityError:
        conection.close()
        return False
    conection.close()
    return True

def check_url(short_url):
    conection = sqlite3.connect(db_file)
    cursor = conection.cursor()
    cursor.execute(
        'SELECT long_url FROM urls WHERE short_url = ?', (short_url,)
    )
    exists=cursor.fetchone()
    if exists:
        return exists[0]
    return None

def update_hits(short_url):
    conection=sqlite3.connect(db_file)
    cursor=conection.cursor()
    cursor.execute(
        'UPDATE urls SET hits = hits + 1 WHERE short_url = ?', (short_url,)
    )
    conection.commit()
    conection.close()

def get_all_urls():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM urls')
    registros = cursor.fetchall()
    conn.close()
    return registros