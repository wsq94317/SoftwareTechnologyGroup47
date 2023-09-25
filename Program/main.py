import wx

from database_manager import DatabaseManager
from main_view import MainView
# import wx

def main():
    # # 1. load data from Database manager
    # db_manager = DatabaseManager()
    # db = db_manager.get_database()
    # if not db:
    #     return

    app = wx.App()
    frame = MainView(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()