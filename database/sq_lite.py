import sqlite3


class SQLiteConnection:
    """establishes connection with db"""
    def __init__(self, db_name, max_retries=5):
        self.db_name = db_name
        self.max_retries = max_retries
        self.conn = None

    def __enter__(self):
        retries = 0
        while retries < self.max_retries:
            try:
                self.conn = sqlite3.connect(self.db_name)
                return self.conn
            except sqlite3.Error as e:
                print("SQLite error:", e)
                retries += 1
                if retries < self.max_retries:
                    print(f"Retrying connection ({retries}/{self.max_retries})...")
                else:
                    print("Max retry attempts reached. Unable to establish a connection.")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print("SQLite error:", e)
