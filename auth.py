```python
import hashlib
import binascii
import os
from database import create_connection, close_connection

def create_user_table(conn):
    try:
        sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_user_table)
    except Error as e:
        print(e)

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def save_user(username, password):
    conn = create_connection()
    if conn is not None:
        create_user_table(conn)
        try:
            hashed_password = hash_password(password)
            sql_insert_user = ''' INSERT INTO users(username,password)
                                VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql_insert_user, (username, hashed_password))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            close_connection(conn)
    else:
        print("Error! cannot create the database connection.")

def authenticate_user(username, password):
    conn = create_connection()
    if conn is not None:
        create_user_table(conn)
        try:
            sql_select_user = ''' SELECT * FROM users WHERE username=? '''
            cur = conn.cursor()
            cur.execute(sql_select_user, (username,))
            rows = cur.fetchall()
            if len(rows) > 0:
                stored_password = rows[0][2]
                return verify_password(stored_password, password)
            else:
                return False
        except Error as e:
            print(e)
        finally:
            close_connection(conn)
    else:
        print("Error! cannot create the database connection.")
```
