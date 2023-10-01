import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def query_price_distribution_data(date, total_days):
    # Connect to the database
    database = sqlite3.connect("database/airbnbdata.db")

    # Calculate the end date for the query
    end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

    # Build the price query
    price_query = """SELECT price FROM Calendar
                     WHERE date BETWEEN ? AND ?;"""

    # Execute the price query
    price_cursor = database.execute(price_query, (start_date, end_date))

    # Extract price data and filter out null values
    prices = [row[0] for row in price_cursor.fetchall() if row[0] is not None]

    # Print statistics about the prices
    print("Maximum Price:", max(prices))
    print("Number of Prices:", len(prices))
    print("Minimum Price:", min(prices))

    # Close the database connection
    database.close()

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

    # Return the plot
    return plt


# 示例用法
start_date = "2019-05-11"
num_days = 9
prices = query_price_distribution_data(start_date, num_days)
plt.show()



