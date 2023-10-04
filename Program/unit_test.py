import pytest
from database_manager import DatabaseManager
import matplotlib.pyplot as plt
import os


class TestDatabaseManager:
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

    @pytest.mark.parametrize("suburb_list, date, total_days,expected_result ", [
        ([""], "2019-08-01", 0, []),

    ])
    def test_query_location_data_date_invlid(self, suburb_list, date, total_days, expected_result):
        # 调用要测试的函数
        db_manager = DatabaseManager("database/airbnbdata.db")
        result = db_manager.query_location_data(suburb_list, date, total_days)

        # 断言结果是否符合预期
        assert result == expected_result

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

    # 测试 date 参数
    @pytest.mark.parametrize("date, expected_houses_length, expected_comments_length", [
        ("2023-01-01", 0, 8879),
        ("2019-08-03", 7786, 8879),
    ])
    def test_query_kword_data_by_date(self, date, expected_houses_length, expected_comments_length):
        total_days = 10
        keyword = "pool"

        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)

        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    # 测试 total_days 参数
    @pytest.mark.parametrize("total_days, expected_houses_length, expected_comments_length", [
        (10, 0, 7159),
        (7, 0, 7159),
    ])
    def test_query_kword_data_by_total_days(self, total_days, expected_houses_length, expected_comments_length):
        date = "2018-03-01"
        keyword = "wifi"

        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)

        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    # 测试 keyword 参数
    @pytest.mark.parametrize("keyword, expected_houses_length, expected_comments_length", [
        ("Sydney", 21116, 74976),
        ("pet", 5980, 6297),
    ])
    def test_query_kword_data_by_keyword(self, keyword, expected_houses_length, expected_comments_length):
        date = "2019-08-15"
        total_days = 6

        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)

        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    @pytest.mark.parametrize("date, total_days, expected_houses_length, expected_comments_length", [
        ("2018-05-01", 10, 0, 27432),
        ("2019-04-03", 7, 19842, 27432),
    ])
    def test_query_kword_data_by_date_and_total_days(self, date, total_days, expected_houses_length, expected_comments_length):
        keyword = "park"
        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)
        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    @pytest.mark.parametrize("date, keyword, expected_houses_length, expected_comments_length", [
        ("2019-09-09", "pool", 7786, 8879),
        ("2018-09-09", "city", 0, 41791),
    ])
    def test_query_kword_data_by_date_and_keyword(self, date, keyword, expected_houses_length, expected_comments_length):
        total_days = 14
        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)
        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    @pytest.mark.parametrize("total_days, keyword, expected_houses_length, expected_comments_length", [
        (1, "cold", 0, 2930),
        (9, "delicious", 0, 2092),
    ])
    def test_query_kword_data_by_total_days_and_keyword(self, total_days, keyword, expected_houses_length, expected_comments_length):
        date = "2018-03-26"
        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)
        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    @pytest.mark.parametrize("date, total_days, keyword, expected_houses_length, expected_comments_length", [
        ("2019-12-24", 20, "computer", 0, 166),
        ("2018-01-08", 8, "kid", 0, 6089),

    ])
    def test_query_kword_data(self, date, total_days, keyword, expected_houses_length, expected_comments_length):
        db_manager = DatabaseManager("database/airbnbdata.db")
        houses, comments = db_manager.query_kword_data(date, total_days, keyword)
        assert houses is not None
        assert comments is not None
        assert len(houses) == expected_houses_length
        assert len(comments) == expected_comments_length

    def test_fetch_clean_related_comments(self):
        db_manager = DatabaseManager("database/airbnbdata.db")
        result = db_manager.fetch_clean_related_comments()

        assert result is not None
        assert isinstance(result, list)

        if result:
            first_entry = result[0]
            assert isinstance(first_entry, tuple)
            assert len(first_entry) == 4  # Assuming there are always 4 elements in the tuple

    def test_init_method(self):

        db_manager = DatabaseManager("database/airbnbdata.db")

        assert os.path.exists("database")

        assert db_manager.database_path == "database/airbnbdata.db"

        expected_csv_path = {
            "Calendar" : "../datasets/calendar_dec18.csv",
            "House" : "../datasets/listings_dec18.csv",
            "Reviews" : "../datasets/reviews_dec18.csv"
        }
        assert db_manager.csv_path == expected_csv_path

        assert db_manager.database is not None

    def test_connect_database_success(self):

        db_manager = DatabaseManager("database/airbnbdata.db")


        db_manager.connect_database()

        assert db_manager.database is not None
        assert db_manager.cursor is not None









if __name__ == "__main__":
    pytest.main()








