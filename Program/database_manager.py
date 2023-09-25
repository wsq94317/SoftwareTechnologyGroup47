import sqlite3

class DatabaseManager:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.init_database()

    def init_database(self):
        try:
            self.database = sqlite3.connect("./database/airbnbdata.db")
            self.cursor = self.database.cursor()
        except sqlite3.Error as e:
            print(f"Database error {e}")
            return
        except Exception as e:
            print(f"General error {e}")
            return

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='listings';")

        if not self.cursor.fetchone():
            self.fetch_data_from_csv()

    def fetch_data_from_csv(self):
        pass

    def get_database(self):
        return self.cursor

    def close(self):
        if self.database:
            self.database.close()