import sqlite3
from datetime import datetime, timedelta

def query_location_data( suburb_list, date, total_days):
    # 连接数据库
    database = sqlite3.connect("database/airbnbdata.db")

    # 计算查询的结束日期
    end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

    # 构建日期查询语句，使用 BETWEEN 条件匹配日期范围
    date_query = """SELECT DISTINCT c.listing_id FROM Calendar c
    WHERE c.date BETWEEN ? AND ?;"""

    # 构建日期查询参数，只包括开始日期和结束日期
    date_params = [date, end_date]

    # 执行日期查询
    date_cursor = database.execute(date_query, date_params)

    # 获取日期查询结果
    date_result = date_cursor.fetchall()

    # 分批查询地区数据
    batch_size = 500  # 你可以根据需要调整批次大小
    suburb_result = []

    for i in range(0, len(date_result), batch_size):
        batch_date_result = date_result[i:i + batch_size]
        # 构建地区查询语句
        suburb_query = """SELECT h.* FROM House h 
        WHERE h.id IN (
            SELECT DISTINCT c.listing_id FROM Calendar c
            WHERE c.listing_id IN ({})
        )
        AND h.surburb_id IN (
            SELECT s.surburb_id FROM Surburb s
            WHERE s.surburb_name IN (?)
        )
        AND h.surburb_id IN (
            SELECT s.surburb_id FROM Surburb s
            WHERE s.surburb_name IN (?)
        );""".format(', '.join(['?'] * len(batch_date_result)), ', '.join(['?'] * len(suburb_list)))

        # 构建地区查询参数，包括日期列表和郊区列表
        suburb_params = [param[0] for param in batch_date_result] + suburb_list + suburb_list

        # 执行地区查询
        suburb_cursor = database.execute(suburb_query, suburb_params)

        # 获取地区查询结果
        suburb_result.extend(suburb_cursor.fetchall())

    # 关闭数据库连接
    database.close()

    # 返回地区查询结果
    return suburb_result




# 假设你有一个名为 suburb_list 的郊区名称列表
suburb_list = ["Avalon"]
date = "2019-10-06"  # 替换为你的开始日期
total_days = 20  # 查询的天数

# 调用函数查询数据
result = query_location_data( suburb_list, date, total_days)

# 打印查询结果
count=0
for row in result:
    count+=1
print(count)

