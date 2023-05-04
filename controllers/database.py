import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """Initialize the database object with the path to the database file."""
        self.db_file = db_file
        self.conn = None
        self.connect()
        self.create_tables()

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

    def close(self):
        """Close the connection to the SQLite database."""
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None):
        """Execute an SQL query and return the results."""
        if not self.conn:
            self.connect()
        cur = self.conn.cursor() # type:ignore
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        rows = cur.fetchall()
        return rows

    def create_tables(self):
        """Create the users, session, configurations, and audit_logs tables if they do not exist."""
        sql_create_users_table = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """
        sql_create_session_table = """
            CREATE TABLE IF NOT EXISTS session (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
        """
        sql_create_configurations_table = """
            CREATE TABLE IF NOT EXISTS configurations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL,
                value TEXT NOT NULL
            );
        """
        sql_create_audit_logs_table = """
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                action TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
        """
        self.execute(sql_create_users_table)
        self.execute(sql_create_session_table)
        self.execute(sql_create_configurations_table)
        self.execute(sql_create_audit_logs_table)
