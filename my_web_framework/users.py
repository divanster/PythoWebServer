import sqlite3
import hashlib
import os


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '../examples/users.db')
    return sqlite3.connect(db_path)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(username, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        connection.commit()
    except sqlite3.IntegrityError:
        return False, "User already exists."
    finally:
        connection.close()
    return True, "User added successfully."


def authenticate(username, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    hashed_password = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    connection.close()
    return user is not None
