import pytest
from database_manager import DatabaseManager
import matplotlib.pyplot as plt
import sqlite3
TEST_DATABASE_PATH = 'database/airbnbdata.db'
class TestDatabaseManager:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # 在测试用例运行之前，创建一个测试数据库连接
        test_db = sqlite3.connect(TEST_DATABASE_PATH)
        test_cursor = test_db.cursor()

        # 在测试用例运行之后，关闭数据库连接并删除测试数据库文件
        yield test_cursor

        test_cursor.close()
        test_db.close()
        import os
        os.remove(TEST_DATABASE_PATH)

    # 测试连接数据库方法
    def test_connect_database(self):
        # 创建一个数据库连接实例
        database_instance = DatabaseManager("database/airbnbdata.db")  # 使用正确的类名

        # 尝试连接数据库
        database_instance.connect_database()

        # 断言数据库连接是否成功
        assert database_instance.database is not None
        assert database_instance.cursor is not None
        # 测试连接错误的数据库路径


    @pytest.mark.parametrize("suburb1, suburb2", [
        ("Artarmon", "Ashfield"),  # 指定测试参数
    ])
    def test_get_surburb_list(self, suburb1, suburb2):
        # 创建数据库管理类的实例
        db_manager = DatabaseManager("database/airbnbdata.db")

        # 调用要测试的函数
        surburb_list = db_manager.get_surburb_list()

        # 断言结果是否符合预期
        assert isinstance(surburb_list, dict)
        assert suburb1 in surburb_list
        assert suburb2 in surburb_list

    @pytest.mark.parametrize("suburb1, suburb2, invalid_suburb", [
        ("Artarmon", "Ashfield", "InvalidSuburb"),  # 包括一个无效的 suburb
    ])
    def test_get_surburb_list_invalid(self,suburb1, suburb2, invalid_suburb):
        # 创建数据库管理类的实例
        db_manager = DatabaseManager("database/airbnbdata.db")

        # 调用要测试的函数，并包括一个无效的 suburb＿
        surburb_list = db_manager.get_surburb_list()

        # 断言结果是否符合预期
        assert isinstance(surburb_list, dict)
        assert suburb1 in surburb_list
        assert suburb2 in surburb_list
        # 验证无效的 suburb 不在结果中
        assert invalid_suburb not in surburb_list

    @pytest.mark.parametrize("min_year, max_year", [
        ("2017", "2020"),  # 指定测试参数
    ])
    def test_get_year_range(self, min_year, max_year):
        # 创建数据库管理类的实例
        db_manager = DatabaseManager("database/airbnbdata.db")

        # 调用要测试的函数
        actual_min_year, actual_max_year = db_manager.get_year_range()

        # 断言结果是否符合预期
        assert isinstance(actual_min_year, str)
        assert isinstance(actual_max_year, str)
        assert actual_min_year <= actual_max_year

        # Test for getting an error in the year range

    @pytest.mark.parametrize("total_days, expected_result_length", [
        (7, 216),  # 这里将多个参数放在一个元组内
    ])
    def test_query_location_data_total_days(self, total_days, expected_result_length):
        suburb_list = ["Alexandria"]  # 用于测试的固定 suburb_list
        date = "2019-01-01"  # 用于测试的固定 date

        db_manager = DatabaseManager("database/airbnbdata.db")
        # 调用要测试的函数
        result = db_manager.query_location_data(suburb_list, date, total_days)

        # 断言结果是否符合预期
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == expected_result_length

    @pytest.mark.parametrize("suburb_list, expected_result_length", [
        (["Alexandria"], 216),
        (["Sydney"], 0),
        (["Bondi"], 1026),
 ])
    def test_query_location_data_suburb_list(self,suburb_list, expected_result_length):
        date = "2019-01-01"
        total_days = 7

        db_manager=DatabaseManager("database/airbnbdata.db")
        # 调用要测试的函数
        result = db_manager.query_location_data(suburb_list, date, total_days)

        # 断言结果是否符合预期
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == expected_result_length

    @pytest.mark.parametrize("suburb_list, date, expected_result_length", [
        (["Alexandria"], "2019-01-01" ,216),  # 第一个测试用例
        (["Sydney"], "2019-03-15", 0),  # 第二个测试用例
        (["Bondi"], "2019-07-10", 1026),  # 第三个测试用例
        # 添加更多测试用例，以覆盖不同情况
    ])
    def test_query_location_data_date(self, suburb_list, date, expected_result_length):
        total_days = 7
        db_manager = DatabaseManager("database/airbnbdata.db")
        # 调用要测试的函数
        result = db_manager.query_location_data(suburb_list, date, total_days)

        # 断言结果是否符合预期
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == expected_result_length

    @pytest.mark.parametrize("suburb_list, date, total_days, expected_result_length", [
        (["Alexandria"], "2019-01-01",7, 216),
        (["Sydney"], "2019-03-15",2, 0),
        (["Bondi"], "2019-07-10",3, 1026),

    ])
    def test_query_location_data_date_all(self, suburb_list, date, total_days, expected_result_length):
        # 调用要测试的函数
        db_manager = DatabaseManager("database/airbnbdata.db")
        result = db_manager.query_location_data(suburb_list, date, total_days)

        # 断言结果是否符合预期
        assert result is not None
        assert isinstance(result, list)
        assert len(result) == expected_result_length

    @pytest.mark.parametrize("date", ["2019-01-01"])
    def test_query_price_distribution_data(self, date):
        total_days = 1
        db_manager = DatabaseManager("database/airbnbdata.db")
        result = db_manager.query_price_distribution_data(date, total_days)
        assert result is not None
        assert isinstance(result, plt.Figure)
        assert len(result.get_axes()) > 0

    @pytest.mark.parametrize("total_days",[1])
    def test_query_price_distribution_data(self, total_days):
        date = "2019-01-01"
        db_manager = DatabaseManager("database/airbnbdata.db")
        result = db_manager.query_price_distribution_data(date, total_days)
        assert result is not None
        assert isinstance(result, plt.Figure)
        assert len(result.get_axes()) > 0

if __name__ == "__main__":
    pytest.main()








