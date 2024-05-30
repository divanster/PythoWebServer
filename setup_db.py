import sqlite3
import os


def setup_database():
    db_path = os.path.join(os.path.dirname(__file__), 'examples/users.db')
    connection = sqlite3.connect(db_path)  # Ensure the correct path
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


if __name__ == '__main__':
    setup_database()
