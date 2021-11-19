import sqlite3

DATABASE_NAME = "db_employee.db"


def get_database_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn
