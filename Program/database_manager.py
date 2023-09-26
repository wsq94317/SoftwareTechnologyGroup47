import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.csv_path = {
            "calendar_dec" : "../datasets/calendar_dec18.csv",
            "listing_dec" : "../datasets/listing_dec18.csv",
            "reviews_dec" : "../datasets/calendar_dec18.csv"
        }
        self.database_path = "database/airbnbdata.db"

        self.init_database()

    def init_database(self):
        try:
            self.database = sqlite3.connect(self.database_path)
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
        self.database.execute(
            """CREATE TABLE IF NOT EXISTS Surburb (
                surburb_id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT UNIQUE
            )"""
        )

        self.database.execute(
            '''CREATE TABLE IF NOT EXISTS Calendar (
               listing_id INTEGER,
               date TEXT,
               available TEXT,
               price TEXT
           )'''
        )

        self.database.execute(
            '''CREATE TABLE IF NOT EXISTS Reviews (
                listing_id INTEGER,
                id INTEGER PRIMARY KEY,
                date TEXT,
                reviewer_id INTEGER,
                reviewer_name TEXT,
                comments TEXT
            )'''
        )

        self.database.execute(
            '''CREATE TABLE IF NOT EXISTS House (
                id INTEGER PRIMARY KEY,
                name TEXT,
                summary TEXT,
                space TEXT,
                description TEXT,
                experiences_offered TEXT,
                neighborhood_overview TEXT,
                notes TEXT,
                transit TEXT,
                access TEXT,
                interaction TEXT,
                house_rules TEXT,
                location INTEGER,
                FOREIGN KEY (location) REFERENCES Surburb(surburb_id)
            )'''
        )

        for table_name, csv_path in self.csv_path.items():
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, self.database, if_exists='append', index = False)



    def get_database(self):
        return self.cursor

    def close(self):
        if self.database:
            self.database.close()