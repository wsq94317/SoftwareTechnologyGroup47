import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import re

class DatabaseManager:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.csv_path = {
            "Calendar" : "../datasets/calendar_dec18.csv",
            "House" : "../datasets/listings_dec18.csv",
            "Reviews" : "../datasets/reviews_dec18.csv"
        }
        if not os.path.exists("database"):
            os.makedirs("database")
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
        data = self.cursor.execute(f"SELECT surburb_name from Surburb GROUP BY surburb_name")
        for item in data:
            surburb_list[item[0]] = list()
        for item in surburb_list.keys():
            data = self.cursor.execute("SELECT surburb_id from Surburb WHERE surburb_name = ?", (item,))
            for ele in data:
                surburb_list[item].append(ele[0])
        self.close()
        return surburb_list

    def get_year_range(self):
        self.connect_database()
        self.cursor.execute("SELECT MIN(strftime('%Y', date)), MAX(strftime('%Y', date)) FROM Calendar")
        min_year, max_year = self.cursor.fetchone()
        self.close()
        return min_year,max_year

    def query_location_data(self,suburb_list, date, total_days):
        # Connect to the database
        self.connect_database()

        # Calculate the end date for the query
        end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

        # Create placeholders for date range and suburb list
        params = [date, end_date] + suburb_list

        # Construct the SQL query
        suburb_query = """
            SELECT h.id, h.name, h.summary,h.space,h.description, h.experiences_offered, h.neighborhood_overview, h.notes, h.transit,h.access, h.interaction, h.house_rules, s.surburb_name, s.city,s.country,s.zipcode  FROM House h
            INNER JOIN Surburb s ON h.surburb_id = s.surburb_id
            WHERE EXISTS (
                SELECT 1 FROM Calendar c
                WHERE c.listing_id = h.id
                AND c.date BETWEEN ? AND ?
            )
            AND s.surburb_name IN ({})
        """.format(','.join(['?'] * len(suburb_list)))

        # Execute the query
        suburb_cursor = self.cursor.execute(suburb_query, params)

        # Fetch the results
        suburb_result = suburb_cursor.fetchall()

        # Close the database connection
        self.close()

        # Return the results
        return suburb_result

    def query_price_distribution_data(self,date, total_days):
        # Connect to the database
        self.connect_database()

        # Calculate the end date for the query
        end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

        # Build the price query
        price_query = """SELECT price FROM Calendar
                         WHERE date BETWEEN ? AND ? AND price<>0;"""

        # Execute the price query
        price_cursor = self.cursor.execute(price_query, (date, end_date))

        # Extract price data and filter out null values
        prices = [row[0] for row in price_cursor.fetchall() if row[0] is not None]

        # Close the database connection
        self.close()

        if len(prices) == 0:
            return

        # Find the minimum and maximum values in the prices list
        min_price = min(prices)
        max_price = max(prices)

        # Calculate the bin width for the histogram
        bin_width = (max_price - min_price) / 10

        # Create price bins
        price_bins = [min_price + i * bin_width for i in range(11)]

        # Convert the bins to integers (if needed)
        price_bins = [int(bin) for bin in price_bins]

        # Plot a histogram of the prices
        plt.hist(prices, bins=price_bins, edgecolor='k')
        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig("price_distribution.png")

        # Add text labels above each bar showing the count
        n, bins, patches = plt.hist(prices, bins=price_bins, edgecolor='k')
        for i, count in enumerate(n):
            if count > 0:
                plt.text(bins[i] + (bins[i + 1] - bins[i]) / 2, count, str(int(count)), ha='center', va='bottom')

        # Display the plot
        # plt.show()
        fig = plt.gcf()

        # Return the plot
        return fig

    def query_kword_data(self, date, total_days, keyword):
        self.connect_database()

        # Calculate end date
        end_date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=total_days)

        # Fetch available house IDs from Calendar table within the date range
        query = (f"SELECT DISTINCT C.listing_id, H.name, H.summary, H.space, H.description, H.experiences_offered, "
                 f"H.neighborhood_overview, H.notes, H.transit, H.access, H.interaction, H.house_rules, S.surburb_name, S.city, S.country, S.zipcode "
                 f"FROM Calendar AS C "
                 f"LEFT JOIN House AS H on C.listing_id = H.id "
                 f"LEFT JOIN Surburb AS S ON H.surburb_id = S.surburb_id "
                 f"WHERE date BETWEEN '{date}' AND '{end_date}'"
                 f"AND (H.name LIKE '%{keyword}%' or "
                 f"H.summary LIKE '%{keyword}%' or "
                 f" H.space LIKE '%{keyword}%' or "
                 f"H.description LIKE '%{keyword}%' or "
                 f"H.experiences_offered LIKE '%{keyword}%' or "
                 f"H.neighborhood_overview LIKE '%{keyword}%' or "
                 f" H.notes LIKE '%{keyword}%' or "
                 f" H.transit LIKE '%{keyword}%' or "
                 f" H.access LIKE '%{keyword}%' or "
                 f" H.interaction LIKE '%{keyword}%' or "
                 f" H.house_rules LIKE '%{keyword}%' or "
                 f"S.surburb_name LIKE '%{keyword}%' or "
                 f" S.city LIKE '%{keyword}%' or "
                 f" S.country LIKE '%{keyword}%' or "
                 f"S.zipcode LIKE '%{keyword}%') ")

        self.cursor.execute(query)
        houses = self.cursor.fetchall()

        # Fetch listing IDs from Reviews table that match the keyword
        query_reviews = f"SELECT listing_id, reviewer_name, comments FROM Reviews WHERE comments LIKE '%{keyword}%'"
        self.cursor.execute(query_reviews)
        comments = self.cursor.fetchall()
        self.close()

        # Return the two DataFrames
        return houses, comments

    def fetch_clean_related_comments(self):
        self.connect_database()
        # 定义清洁度关键字列表
        clean_keyword = ["clean", "tidy", "spotless", "dusty", "dirty", "sanitized",
                         "hygienic", "messy", "immaculate", "unwashed", "soiled", "fresh",
                         "neat", "disinfected", "grimy", "stained", "polished", "swept",
                         "mopped"]
        likes_query = [f"R.comments LIKE '%{keyword}%'" for keyword in clean_keyword]
        conditions = " OR ".join(likes_query)

        query = (f"SELECT H.id, H.Name, COUNT(R.id) as total_comments, SUM(Case when {conditions} then 1 else 0 end) as matched_count "
                 f"from House as H "
                 f"Left Join Reviews as R ON H.id = R.listing_id "
                 f"Group by H.id "
                 f"Having matched_count > 0 ")

        self.cursor.execute(query)
        res = self.cursor.fetchall()
        self.close()
        return res

    def query_tendency_data(self,surburb_list,date,total_days):
        print(surburb_list,date,total_days)
        pass

