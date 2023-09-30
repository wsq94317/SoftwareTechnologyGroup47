import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def query_price_distribution_data(date, total_days):
    # 连接数据库
    database = sqlite3.connect("database/airbnbdata.db")

    # 计算结束日期
    end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

    # 构建价格查询语句
    price_query = """SELECT price FROM Calendar
                     WHERE date BETWEEN ? AND ?;"""

    # 执行价格查询
    price_cursor = database.execute(price_query, (start_date, end_date))

    # 提取价格数据，并过滤掉空值
    prices = [row[0] for row in price_cursor.fetchall() if row[0] is not None]

    print(max(prices))

    # 关闭数据库连接
    database.close()

    price_bins = [price for price in range(100, 15000, 500)]

    # 绘制直方图
    plt.hist(prices, bins=price_bins, edgecolor='k')
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("price_distribution.png")

    return plt

# 示例用法
start_date = "2019-05-30"
num_days = 10
prices = query_price_distribution_data(start_date, num_days)
plt.show()



