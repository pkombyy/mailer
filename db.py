import sqlite3

def connect_db():
    conn = sqlite3.connect('bot_database.db')
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            is_admin BOOLEAN
        )
    ''')
    
    # Таблица сообщений
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            recipient_email TEXT,
            url TEXT,
            sender_id INTEGER,
            status TEXT,
            FOREIGN KEY (sender_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()