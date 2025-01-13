import os
import sqlite3

DB_PATH = "karate.db"


def init_db():
    """Initialize the SQLite database and create tables if needed."""
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    experience TEXT,
                    trial_date TEXT NOT NULL,
                    trial_time TEXT NOT NULL
                )
            """
            )
            conn.commit()
        print(f"Database initialized at: {DB_PATH}")
    else:
        print("Database already exists.")


def get_db_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)
