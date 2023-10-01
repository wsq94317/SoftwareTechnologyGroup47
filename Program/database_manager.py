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

        # Build the date query using the BETWEEN condition to match date range
        date_query = """SELECT DISTINCT c.listing_id FROM Calendar c
                        WHERE c.available = ? AND c.date BETWEEN ? AND ?;"""

        # Build date query parameters, including start date and end date
        date_params = [1, date, end_date]

        # Execute the date query
        date_cursor = self.cursor.execute(date_query, date_params)

        # Get the date query result
        date_result = date_cursor.fetchall()

        # Batch size for querying
        batch_size = 1000

        # Initialize the result list
        suburb_result = []

        # Process date results in batches
        for i in range(0, len(date_result), batch_size):
            batch_date_result = date_result[i:i + batch_size]

            # Build the suburb query to find listings matching dates and connect to Suburb table to get suburb names
            suburb_query = """SELECT h.* FROM House h
                             INNER JOIN Surburb s ON h.surburb_id = s.surburb_id
                             WHERE h.id IN ({})
                             AND s.surburb_name = ? ;""".format(', '.join(['?'] * len(batch_date_result)))

            # Build suburb query parameters, including date list and suburb name
            suburb_params = tuple([param[0] for param in batch_date_result] + [suburb_list])

            # Execute the suburb query
            suburb_cursor = self.cursor.execute(suburb_query, suburb_params)

            # Get and extend the suburb query results to the result list
            suburb_result.extend(suburb_cursor.fetchall())

        # Return the suburb query result
        print(suburb_result)

        # Close the database connection
        self.close()

    def query_price_distribution_data(self,date, total_days):
        # Connect to the database
        self.connect_database()

        # Calculate the end date for the query
        end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

        # Build the price query
        price_query = """SELECT price FROM Calendar
                         WHERE date BETWEEN ? AND ?;"""

        # Execute the price query
        price_cursor = self.cursor.execute(price_query, (date, end_date))

        # Extract price data and filter out null values
        prices = [row[0] for row in price_cursor.fetchall() if row[0] is not None]

        # Close the database connection
        self.close()

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
        plt.show()

        # Return the plot
        return plt

    def query_kword_data(self, date, total_days, keyword):
        self.connect_database()


        # Calculate end date
        end_date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=total_days)

        # Fetch available house IDs from Calendar table within the date range
        query = f"SELECT DISTINCT listing_id FROM Calendar WHERE date BETWEEN '{date}' AND '{end_date}' AND available = '1'"
        self.cursor.execute(query)
        available_house_ids = [row[0] for row in self.cursor.fetchall()]

        # Fetch listing IDs from Reviews table that match the keyword
        query_reviews = f"SELECT DISTINCT listing_id FROM Reviews WHERE comments LIKE '%{keyword}%'"
        self.cursor.execute(query_reviews)
        review_matched_ids = [row[0] for row in self.cursor.fetchall()]

        # Combine the IDs from Calendar and Reviews
        combined_ids = list(set(available_house_ids + review_matched_ids))

        # Fetch data from the House table into a pandas DataFrame
        query = "SELECT * FROM House"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(data, columns=columns)

        # Filter the dataframe based on combined house IDs
        df = df[df['id'].isin(combined_ids)]

        # Columns to search in for the keyword
        columns_to_search = ['name', 'summary', 'description', 'neighborhood_overview', 'notes', 'transit', 'access',
                             'interaction', 'house_rules']

        # Search for the keyword in the specified columns
        matched_rows = df[df[columns_to_search].apply(
            lambda x: x.str.contains(keyword, na=False, flags=re.IGNORECASE, regex=True)).any(axis=1)].copy()

        # Function to get columns with keyword and their values
        def get_keyword_data(row):
            keyword_data = {}
            for col in columns_to_search:
                if re.search(keyword, str(row[col]), flags=re.IGNORECASE):
                    keyword_data[col] = row[col]
            return keyword_data

        # Apply the function to each row of matched_rows
        matched_rows.loc[:, 'keyword_data'] = matched_rows.apply(get_keyword_data, axis=1)

        # Rename the 'id' column to 'listing_id' in matched_rows DataFrame
        matched_rows = matched_rows.rename(columns={'id': 'listing_id'})

        # Fetch comments for the matched listing IDs
        matched_listing_ids = matched_rows['listing_id'].tolist()
        query_comments = f"SELECT listing_id, comments FROM Reviews WHERE listing_id IN ({','.join(map(str, matched_listing_ids))})"
        self.cursor.execute(query_comments)
        matched_comments = self.cursor.fetchall()

        # Create a new DataFrame for comments
        comments_df = pd.DataFrame(matched_comments, columns=['listing_id', 'comments'])

        self.close()

        # Return the two DataFrames
        return matched_rows, comments_df

    def fetch_clean_related_comments(self):

        self.connect_database()


        # 定义清洁度关键字列表
        clean_keyword = ["clean", "tidy", "spotless", "dusty", "dirty", "sanitized",
                         "hygienic", "messy", "immaculate", "unwashed", "soiled", "fresh",
                         "neat", "disinfected", "grimy", "stained", "polished", "swept",
                         "mopped"]

        # 定义函数，检查文本中是否包含清洁度关键字
        def contain_clean(text):
            for keyword in clean_keyword:
                if re.search(keyword, str(text), flags=re.IGNORECASE):
                    return True
            return False

        # 从Reviews表中获取所有评论及其对应的房源ID
        query = "SELECT listing_id, comments FROM Reviews"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        # 将数据转换为pandas DataFrame
        df = pd.DataFrame(data, columns=['listing_id', 'comments'])

        # 应用contain_clean函数
        df['matches'] = df['comments'].apply(contain_clean)

        # 对每个房源计算与清洁度有关的评论数量
        clean_comments_count = df[df['matches']].groupby('listing_id').size().reset_index(name='clean_comments_count')

        # 对每个房源计算总评论数
        total_comments_count = df.groupby('listing_id').size().reset_index(name='total_comments_count')

        # 从House表中获取房源的其他信息
        query_house = "SELECT id, name, space, description FROM House"
        self.cursor.execute(query_house)
        house_data = self.cursor.fetchall()
        house_df = pd.DataFrame(house_data, columns=['listing_id', 'name', 'space', 'description'])

        # 合并三个DataFrame以获取完整的结果
        merged_df = pd.merge(house_df, total_comments_count, on='listing_id', how='inner')
        merged_df = pd.merge(merged_df, clean_comments_count, on='listing_id', how='left').fillna(0)

        self.close()

        # 返回合并后的DataFrame
        return merged_df

    def query_tendency_data(self,surburb_list,date,total_days):
        print(surburb_list,date,total_days)
        pass

