import sqlite3
from datetime import datetime, timedelta

def location_data(suburb_name, date, total_days):
    # 连接数据库
    database = sqlite3.connect("../database/airbnbdata.db")

    # 计算查询的结束日期
    end_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=total_days)).strftime("%Y-%m-%d")

    # 构建日期查询语句，使用 BETWEEN 条件匹配日期范围
    date_query = """SELECT DISTINCT c.listing_id FROM Calendar c
                    WHERE c.available = ? AND c.date BETWEEN ? AND ?;"""


    # 构建日期查询参数，只包括开始日期和结束日期
    date_params = [1,date, end_date]

    # 执行日期查询
    date_cursor = database.execute(date_query, date_params)

    # 获取日期查询结果
    date_result = date_cursor.fetchall()

    print(len(date_result))
    # 分批查询的批次大小
    batch_size = 1000

    # 初始化结果列表
    suburb_result = []
    # 分批处理日期结果
    for i in range(0, len(date_result), batch_size):
        batch_date_result = date_result[i:i + batch_size]

        # 构建地区查询语句，查找匹配日期的房源，并连接到Surburb表以获取郊区名称
        suburb_query = """SELECT h.* FROM House h
                         INNER JOIN Surburb s ON h.surburb_id = s.surburb_id
                         WHERE h.id IN ({})
                         AND s.surburb_name = ? ;""".format(', '.join(['?'] * len(batch_date_result)))

        # 构建地区查询参数，包括日期列表和郊区名称
        suburb_params = tuple([param[0] for param in batch_date_result] + [suburb_name])

        # 执行地区查询
        suburb_cursor = database.execute(suburb_query, suburb_params)

        # 获取地区查询结果并扩展到结果列表
        suburb_result.extend(suburb_cursor.fetchall())

    # 关闭数据库连接
    database.close()

    # 返回地区查询结果
    return suburb_result

# 假设您选择的起始日期和查询的总天数不同
suburb_name = "Avalon"
date = "2019-02-01"  # 替换为您的开始日期
total_days = 0  # 查询的天数

# 调用函数查询数据
result = location_data(suburb_name, date, total_days)

# 打印查询结果
count = len(result)
print(count)
print(result)



