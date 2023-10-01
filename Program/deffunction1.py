import sqlite3
from datetime import datetime, timedelta

def query_location_data(suburb_list, date, total_days):
    # Connect to the database
    database = sqlite3.connect("../database/airbnbdata.db")

    # Calculate the end date for the query
    end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

    # Build the date query using the BETWEEN condition to match date range
    date_query = """SELECT DISTINCT c.listing_id FROM Calendar c
                    WHERE c.available = ? AND c.date BETWEEN ? AND ?;"""

    # Build date query parameters, including start date and end date
    date_params = [1, date, end_date]

    # Execute the date query
    date_cursor = database.execute(date_query, date_params)

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
        suburb_cursor = database.execute(suburb_query, suburb_params)

        # Get and extend the suburb query results to the result list
        suburb_result.extend(suburb_cursor.fetchall())

    # Close the database connection
    database.close()

    # Return the suburb query result
    print(suburb_result)




# 假设您选择的起始日期和查询的总天数不同
surburb_list = "Avalon"
date = "2019-02-01"  # 替换为您的开始日期
total_days = 0  # 查询的天数

# 调用函数查询数据
result = query_location_data(surburb_list, date, total_days)





