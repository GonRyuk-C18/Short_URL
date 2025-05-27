import unittest
import sqlite3
from database.database import create_db,insert_url, check_url, update_hits, get_all_urls
import random
import string
from short_url import app

class short_url_test(unittest.TestCase):


    def test_check_url(self):
        short="".join(random.choices(string.ascii_letters + string.digits, k=6))
        print(short)
        insert_url("https://www.google.com/search?q=python+is+life", short)
        long_url= check_url(short)
        self.assertEqual(long_url, "https://www.google.com/search?q=python+is+life")



if __name__ == '__main__':
    unittest.main()

