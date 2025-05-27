import unittest
import sqlite3
from database.database import create_db, check_url, update_hits
from short_url import app

class short_url_test(unittest.TestCase):
        def setUpClass(cls):
            cls.db_name="test_database.db"
            conection=sqlite3.connect(cls.db_name)
            cursor=conection.cursor()
            cursor.execute(
                '''
                CREATE TABEL IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                long_url TEXT NOT NULL,
                short_url TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                hits INTEGER DEFAULT 0,
                )
                '''
            )
            conection.commit()
            conection.close()
            
