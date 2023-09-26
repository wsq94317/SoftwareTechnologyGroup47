import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.csv_path = {
            "calendar_dec" : "../datasets/calendar_dec18.csv",
            "listing_dec" : "../datasets/listings_dec18.csv",
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
                surburb_name TEXT,
                country TEXT
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

        def convert_price(pirce_str):
            try:
                return float(str(pirce_str).replace('$',"").replace(',',''))
            except Exception:
                return float(0)


        for table_name, csv_path in self.csv_path.items():
            df = pd.read_csv(csv_path)

            if table_name == "calendar_dec":
                # Convert "t" or "f" to boolean

                df['available'].fillna('f', inplace=True)
                unknown_values = set(df['available'].unique()) - {'t', 'f'}
                for value in unknown_values:
                    df['available'].replace(value, 'f', inplace=True)
                df['available'] = df['available'].map({'t': True, 'f': False})

                # if the price is empty, fill a default value to avoid error
                df['price'].fillna('$0.00')
                # Convert price from "$10.00" format to float
                df['price'] = df['price'].apply(convert_price)

            elif table_name == "listing_dec":
                # Splitting the smart_location into surburb_name and country
                # fill null value before split data by ','
                # df['smart_location'].fillna('Unknown, Unknown', inplace=True)

                # df[['surburb_name', 'country']] = df['smart_location'].str.split(',', expand=True)

                df['smart_location'].fillna('Unknown, Unknown', inplace=True)

                # Split 'smart_location' into two temporary columns
                df_temp = df['smart_location'].str.split(',', expand=True)
                if df_temp.shape[1] == 2:
                    df_temp.columns = ['surburb_name_temp', 'country_temp']
                elif df_temp.shape[1] > 2:
                    df_temp.columns = ['surburb_name_temp', 'country_temp'] + [f"extra_{i}" for i in
                                                                               range(df_temp.shape[1] - 2)]
                    print("Warning: 'smart_location' column has more than one comma in some rows. Extra columns added.")
                else:
                    raise ValueError(
                        f"'smart_location' column split resulted in {df_temp.shape[1]} columns. Expected at least 2.")
                df['surburb_name'], df['country'] = df_temp['surburb_name_temp'], df_temp['country_temp']
                del df_temp

                try:
                    # Insert the surburb_name and country into Surburb table and get the corresponding IDs
                    df[['surburb_name', 'country']].drop_duplicates().to_sql('Surburb', self.database,
                                                                             if_exists='append', index=False)
                except Exception as e:
                    print(f"Error inserting data into Surburb table: {e}")


                try:
                    # Merge df
                    surburb_df = pd.read_sql("SELECT * FROM Surburb", self.database)
                    df = df.merge(surburb_df, on=['surburb_name', 'country'])
                except Exception as e:
                    print(f"Error reading Surburb table or merging data: {e}")

                try:
                    # Drop unnecessary columns
                    df.drop(columns=['smart_location', 'surburb_name', 'country'], inplace=True)
                except KeyError as e:
                    print(f"Error dropping columns: {e}")

            df.to_sql(table_name, self.database, if_exists='append', index=False)



    def get_database(self):
        return self.cursor

    def close(self):
        if self.database:
            self.database.close()