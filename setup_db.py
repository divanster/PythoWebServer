import sqlite3

def setup_database():
    connection = sqlite3.connect('users.db')
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
