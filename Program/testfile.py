import pandas as pd
from datetime import datetime, timedelta
import sqlite3
database = sqlite3.connect("database/airbnbdata.db")
consur = database.cursor()


import re


# 连接数据库
database = sqlite3.connect("database/airbnbdata.db")
cursor = database.cursor()
cursor.execute("SELECT C.date, AVG(C.price) as average_price, S.surburb_name FROM Calendar C JOIN House H ON C.listing_id = H.id JOIN Surburb S ON H.surburb_id = S.surburb_id GROUP BY C.date, S.surburb_name ORDER BY C.date")
res = cursor.fetchall()
print(res)

# def search_keyword_and_dates(df, keyword, start_date, duration):
#     """
#     Search for a keyword and date range in the dataframe.
#
#     Args:
#     - df (pd.DataFrame): The dataframe to search in.
#     - keyword (str): The keyword to search for.
#     - start_date (str): The start date in format 'YYYY-MM-DD'.
#     - duration (int): Number of days of stay.
#
#     Returns:
#     - pd.DataFrame: A dataframe containing rows that match the keyword and date range.
#     """
#
#     # Calculate end date
#     end_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=duration)
#
#     # Fetch available house IDs from Calendar table within the date range
#     query = f"SELECT DISTINCT listing_id FROM Calendar WHERE date BETWEEN '{start_date}' AND '{end_date}' AND available = '1'"
#     consur.execute(query)
#     available_house_ids = [row[0] for row in consur.fetchall()]
#
#
#     # **Fetch listing IDs from Reviews table that match the keyword**
#     query_reviews = f"SELECT DISTINCT listing_id FROM Reviews WHERE comments LIKE '%{keyword}%'"
#     consur.execute(query_reviews)
#     review_matched_ids = [row[0] for row in consur.fetchall()]
#
#     # **Combine the IDs from Calendar and Reviews**
#     combined_ids = list(set(available_house_ids + review_matched_ids))
#
#
#     # Filter the dataframe based on available house IDs
#     df = df[df['id'].isin(available_house_ids)]
#
#     # Columns to search in for the keyword
#     columns_to_search = ['name', 'summary', 'description', 'neighborhood_overview', 'notes', 'transit', 'access', 'interaction', 'house_rules']
#
#     # Search for the keyword in the specified columns
#     matched_rows = df[df[columns_to_search].apply(lambda x: x.str.contains(keyword, na=False, flags=re.IGNORECASE, regex=True)).any(axis=1)]
#
#     # **Fetch comments for the matched listing IDs**
#     matched_listing_ids = matched_rows['id'].tolist()
#     query_comments = f"SELECT listing_id, comments FROM Reviews WHERE listing_id IN ({','.join(map(str, matched_listing_ids))})"
#     consur.execute(query_comments)
#     matched_comments = consur.fetchall()
#
#     print("\nMatched comments:")
#     for listing_id, comment in matched_comments:
#         print(f"Listing ID: {listing_id}, Comment: {comment}")
#
#
#     return matched_rows
#
# # Fetch data from the House table into a pandas DataFrame
# query = "SELECT * FROM House"
# consur.execute(query)
# data = consur.fetchall()
# columns = [desc[0] for desc in consur.description]
# df = pd.DataFrame(data, columns=columns)
#
# # Test the function
# keyword = "Sydney"  # Replace with your desired keyword
# start_date = "2018-12-07"  # Replace with your desired start date
# duration = 5  # Replace with your desired duration in days
#
# results = search_keyword_and_dates(df, keyword, start_date, duration)
#
# if results.empty:
#     print("No matching results found.")
# else:
#     print(results)
#
#
#
#
#
#
#
# # consur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # tables = consur.fetchall()
# # print(tables)
# #
# #
# # for table in tables:
# #     table_name = table[0]
# #     consur.execute(f"SELECT COUNT(*) FROM {table_name};")
# #     count = consur.fetchone()[0]
# #     print(f"Table {table_name} has {count} records.")
#
#
# # 执行查询
# consur.execute("SELECT * FROM Calendar WHERE listing_id = 12351 AND date BETWEEN '2019-07-18' AND '2019-08-01' AND available = 1")
# results = consur.fetchall()
#
# # 打印结果
# for row in results:
#     print(row)











