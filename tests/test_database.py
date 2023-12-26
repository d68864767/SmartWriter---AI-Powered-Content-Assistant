```python
import unittest
import sqlite3
from sqlite3 import Error
from database import create_connection, close_connection, create_table, save_content, get_content

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = create_connection()
        create_table(self.conn)

    def tearDown(self):
        close_connection(self.conn)

    def test_create_connection(self):
        self.assertIsNotNone(self.conn, "Failed to create database connection.")

    def test_create_table(self):
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='content'")
        self.assertIsNotNone(c.fetchone(), "Failed to create table 'content'.")

    def test_save_content(self):
        save_content("Test content", 1)
        c = self.conn.cursor()
        c.execute("SELECT * FROM content WHERE user_id=?", (1,))
        self.assertIsNotNone(c.fetchone(), "Failed to save content.")

    def test_get_content(self):
        save_content("Test content", 1)
        rows = get_content(1)
        self.assertEqual(len(rows), 1, "Failed to get content.")
        self.assertEqual(rows[0][1], "Test content", "Content retrieved is not the same as content saved.")

if __name__ == '__main__':
    unittest.main()
```
