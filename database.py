```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        return conn
    except Error as e:
        print(e)

def close_connection(conn):
    conn.close()

def create_table(conn):
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS content (
                                        id integer PRIMARY KEY,
                                        text text NOT NULL,
                                        user_id integer NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def save_content(text, user_id):
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        try:
            sql_insert_content = ''' INSERT INTO content(text,user_id)
                                    VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql_insert_content, (text, user_id))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            close_connection(conn)
    else:
        print("Error! cannot create the database connection.")

def get_content(user_id):
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        try:
            sql_select_content = ''' SELECT * FROM content WHERE user_id=? '''
            cur = conn.cursor()
            cur.execute(sql_select_content, (user_id,))
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)
        finally:
            close_connection(conn)
    else:
        print("Error! cannot create the database connection.")
```
