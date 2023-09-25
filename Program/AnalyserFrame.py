import wx
from database_manager import DatabaseManager
from main_view import MainView as mv
from main_view import ResultFrame as rf

class AnalyserApp(mv):
    def __init__(self):
        super().__init__(None)
        # # 1. load data from Database manager
        # db_manager = DatabaseManager()
        # db = db_manager.get_database()
        # if not db:
        #     return

        # init widget panel switcher
        self.active_widget_index = 0
        self.MainPanel.Show()
        self.ShowDataByLoc.Hide()
        self.PriceDistributePanel.Hide()
        self.KeyWordSearchPanel.Hide()
        self.TendencyPanel.Hide()
        self.widget_panel = [self.MainPanel,self.ShowDataByLoc,self.PriceDistributePanel,self.KeyWordSearchPanel,self.TendencyPanel]
        self.Layout()

    def set_active_widget_index(self,index):
        if self.active_widget_index == index or index < 0 or index > 4:
            return
        self.widget_panel[self.active_widget_index].Hide()
        self.Layout()
        self.active_widget_index = index
        self.widget_panel[self.active_widget_index].Show()
        self.Layout()

    def back_to_home(self, event):
        self.set_active_widget_index(0)

    def on_location_btn_clicked(self,event):
        self.set_active_widget_index(1)

    def on_price_dist_btn_clicked(self,event):
        self.set_active_widget_index(2)

    def on_kword_btn_clicked(self,event):
        self.set_active_widget_index(3)

    def on_cleaniess_btn_clicked(self):
        pass

    def on_price_trends_btn_clicked(self):
        self.set_active_widget_index(4)
