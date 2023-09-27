import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.csv_path = {
            "Calendar" : "../datasets/calendar_dec18.csv",
            "House" : "../datasets/listings_dec18.csv",
            "Reviews" : "../datasets/reviews_dec18.csv"
        }
        self.database_path = "database/airbnbdata.db"
        self.init_database()

    def connect_database(self):
        try:
            self.database = sqlite3.connect(self.database_path)
            self.cursor = self.database.cursor()
        except sqlite3.Error as e:
            print(f"Database error {e}")
            return
        except Exception as e:
            print(f"General error {e}")
            return

    def init_database(self):
        self.connect_database()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        if not self.cursor.fetchone():
            self.create_table()

        if self.are_tables_empty():
            self.fetch_data_from_csv()

        self.close()


    def create_table(self):
        self.database.execute(
            """CREATE TABLE IF NOT EXISTS Surburb (
                surburb_id INTEGER PRIMARY KEY AUTOINCREMENT,
                surburb_name TEXT,
                city TEXT,
                country TEXT,
                zipcode TEXT
            )"""
        )

        self.database.execute(
            """CREATE TABLE IF NOT EXISTS Reviews (
                listing_id INTEGER,
                id INTEGER PRIMARY KEY,
                reviewer_id INTEGER,
                reviewer_name TEXT,
                comments TEXT,
                FOREIGN KEY (listing_id) REFERENCES House(id)
            )"""
        )

        self.database.execute(
            '''CREATE TABLE IF NOT EXISTS Calendar (
               listing_id INTEGER,
               date DATE,
               available BOOLEAN,
               price FLOAT,
               FOREIGN KEY (listing_id) REFERENCES House(id),
               PRIMARY KEY (listing_id, date)
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
                surburb_id INTEGER,
                FOREIGN KEY (surburb_id) REFERENCES Surburb(surburb_id)
            )'''
        )


    def fetch_data_from_csv(self):
        def convert_price(pirce_str):
            try:
                return float(str(pirce_str).replace('$',"").replace(',',''))
            except Exception:
                return float(0.00)

        for table_name, csv_path in self.csv_path.items():
            df = pd.read_csv(csv_path,low_memory=False)

            if table_name == "Calendar":
                # Fill empty value and Convert t or f to boolean
                df['available'].fillna('f', inplace=True)
                unknown_values = set(df['available'].unique()) - {'t', 'f'}
                for value in unknown_values:
                    df['available'].replace(value, 'f', inplace=True)
                df['available'] = df['available'].map({'t': True, 'f': False})

                # if the price is empty, fill a default value to avoid error
                df['price'].fillna('$0.00')
                # Convert price from "$10.00" format to float
                df['price'] = df['price'].apply(convert_price)

            elif table_name == "House":
                # Splitting the smart_location into surburb_name and country
                # fill null value before split data by ','
                # df['smart_location'].fillna('Unknown, Unknown', inplace=True)

                # df[['surburb_name', 'country']] = df['smart_location'].str.split(',', expand=True)


                # Handle missing value
                df['neighbourhood'].fillna('Unknown', inplace=True)
                df['city'].fillna('Unknown', inplace=True)
                df['zipcode'].fillna('Unknown', inplace=True)

                # Create new DataFrame column
                df['surburb_name'] = df['neighbourhood']

                try:
                    # Insert the surburb_name, city, and zipcode into Surburb table and get the corresponding IDs
                    df[['surburb_name', 'city', 'zipcode']].drop_duplicates().to_sql('Surburb', self.database,
                                                                                              if_exists='append',
                                                                                              index=False)
                except Exception as e:
                    print(f"Error inserting data into Surburb table: {e}")

                try:
                    # Merge df
                    surburb_df = pd.read_sql("SELECT * FROM Surburb", self.database)
                    df = df.merge(surburb_df, on=['surburb_name', 'city', 'zipcode'])
                except Exception as e:
                    print(f"Error reading Surburb table or merging data: {e}")


                # Filtered csv data to save to the datatable
                columns = ["id", "name", "summary", "space", "description", "experiences_offered", "neighborhood_overview", "notes", "transit", "access", "interaction", "house_rules", "surburb_id"]
                df = df[columns]
            elif table_name=="Reviews":
                columns = ["listing_id", "id", "reviewer_id", "reviewer_name", "comments"]
                df = df[columns]

            df.to_sql(table_name, self.database, if_exists='append', index=False)
            self.database.commit()

    def are_tables_empty(self):
        tables = ["Surburb", "Reviews", "Calendar", "House"]
        for table in tables:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = self.cursor.fetchone()[0]
            if count > 0:
                return False
        return True

    def close(self):
        if self.database:
            self.database.close()


    def get_surburb_list(self):
        surburb_list = dict()
        self.connect_database()
        ret = self.cursor.execute(f"SELECT surburb_name from Surburb GROUP BY surburb_name")
        for item in ret:
            surburb_list[item[0]] = list()
        for item in surburb_list.keys():
            ret = self.cursor.execute("SELECT surburb_id from Surburb WHERE surburb_name = ?", (item,))
            for ele in ret:
                surburb_list[item].append(ele[0])
