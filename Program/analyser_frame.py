import wx
from database_manager import DatabaseManager
from main_view import MainView as mv
from datetime import datetime
from main_view import ResultFrame as rf

class AnalyserApp(mv):
    def __init__(self):
        super().__init__(None)
        # 1. load data from Database manager
        self.db_manager = DatabaseManager()

        self.surburb_dict = self.db_manager.get_surburb_list()
        self.min_year,self.max_year = self.db_manager.get_year_range()
        # initialise views
        self.init_location_view()
        self.init_price_distribution_view()
        self.init_keyword_search_view()
        self.init_tendency_view()

        # init widget panel switcher
        self.active_widget_index = 0
        self.MainPanel.Show()
        self.ShowDataByLoc.Hide()
        self.PriceDistributePanel.Hide()
        self.KeyWordSearchPanel.Hide()
        self.TendencyPanel.Hide()
        self.widget_panel = [self.MainPanel,self.ShowDataByLoc,self.PriceDistributePanel,self.KeyWordSearchPanel,self.TendencyPanel]
        self.Layout()

        self.register_delegates()

    def register_delegates(self):
        #Connect Events
        self.location_data_btn.Bind( wx.EVT_BUTTON, self.on_location_btn_clicked )
        self.kword_btn.Bind( wx.EVT_BUTTON, self.on_kword_btn_clicked )
        self.price_dist_btn.Bind( wx.EVT_BUTTON, self.on_price_dist_btn_clicked )
        self.cleaniess_btn.Bind( wx.EVT_BUTTON, self.on_cleaniess_btn_clicked )
        self.price_trends_btn.Bind( wx.EVT_BUTTON, self.on_price_trends_btn_clicked )

        self.return_btn.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn1.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn2.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn3.Bind(wx.EVT_BUTTON,self.back_to_home)

        self.kword_input_btn.Bind(wx.EVT_BUTTON,self.on_kword_input_btn_clicked)
        self.query_loc_btn.Bind(wx.EVT_BUTTON,self.on_query_loc_btn_clicked)
        self.query_loc_btn1.Bind(wx.EVT_BUTTON,self.on_price_distribution_btn_clicked)
        self.generate_tendency_btn.Bind(wx.EVT_BUTTON,self.on_tendency_btn_clicked)

    def init_location_view(self):
        if not self.surburb_dict or not self.max_year or not self.min_year:
            return
        self.m_checkList1.Set(list(self.surburb_dict.keys()))
        self.m_choice11.Set([str(x) for x in range(int(self.min_year), int(self.max_year)+1)])
        self.m_choice1.Set([str(x) for x in range(1,13)])
        self.m_choice12.Set([str(x) for x in range(1,32)])

    def init_price_distribution_view(self):
        if not self.max_year or not self.min_year:
            return
        self.m_choice111.Set([str(x) for x in range(int(self.min_year), int(self.max_year)+1)])
        self.m_choice13.Set([str(x) for x in range(1,13)])
        self.m_choice121.Set([str(x) for x in range(1,32)])

    def init_keyword_search_view(self):
        if not self.max_year or not self.min_year:
            return
        self.m_choice112.Set([str(x) for x in range(int(self.min_year), int(self.max_year)+1)])
        self.m_choice14.Set([str(x) for x in range(1,13)])
        self.m_choice122.Set([str(x) for x in range(1,32)])

    def init_tendency_view(self):
        if not self.surburb_dict or not self.max_year or not self.min_year:
            return
        self.m_checkList11.Set(list(self.surburb_dict.keys()))
        self.m_choice113.Set([str(x) for x in range(int(self.min_year), int(self.max_year)+1)])
        self.m_choice15.Set([str(x) for x in range(1,13)])
        self.m_choice123.Set([str(x) for x in range(1,32)])
        pass

    def set_active_widget_index(self,index):
        if self.active_widget_index == index or index < 0 or index > 4:
            return
        self.widget_panel[self.active_widget_index].Hide()
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

    def on_cleaniess_btn_clicked(self,event):
        pass

    def on_price_trends_btn_clicked(self,event):
        self.set_active_widget_index(4)


    def on_query_loc_btn_clicked(self,event):
        # Get selected surburb
        checked_items = self.m_checkList1.GetCheckedItems()
        selected_suburbs = [self.m_checkList1.GetString(i) for i in checked_items]
        if len(selected_suburbs )== 0:
            wx.MessageBox("You have not select any surburb, please select at least one surburb to query data!")
            return

        # Get selected date
        year = self.m_choice11.GetStringSelection()
        month = self.m_choice1.GetStringSelection()
        day = self.m_choice12.GetStringSelection()

        # validate date input
        try:
            valid_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            test = datetime.strptime(valid_date,"%Y-%m-%d")
        except ValueError:
            wx.MessageBox("Selected date is invalid. Please choose a valid date")
            return

        # Get total of days
        total_days = self.m_textCtrl1.GetValue()
        if not total_days or total_days == "":
            wx.MessageBox(f"Invalid total days: Input is empty", "Error", wx.OK | wx.ICON_ERROR)
            return
        #validate total_days input
        try:
            total_days = int(total_days)
            if not (0< total_days<365):
                raise ValueError("Total days should be numbers and should between 1 and 365")
        except ValueError as e:
            wx.MessageBox(f"Invalid total days: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.db_manager.query_location_data(selected_suburbs,valid_date,total_days)

    def on_price_distribution_btn_clicked(self,event):
        # Get selected date
        year = self.m_choice111.GetStringSelection()
        month = self.m_choice13.GetStringSelection()
        day = self.m_choice121.GetStringSelection()

        # validate date input
        try:
            valid_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            test = datetime.strptime(valid_date, "%Y-%m-%d")
        except ValueError:
            wx.MessageBox("Selected date is invalid. Please choose a valid date")
            return

        # Get total of days
        total_days = self.m_textCtrl11.GetValue()
        if not total_days or total_days == "":
            wx.MessageBox(f"Invalid total days: Input is empty", "Error", wx.OK | wx.ICON_ERROR)
            return

        # validate total_days input
        try:
            total_days = int(total_days)
            if not (0 < total_days < 365):
                raise ValueError("Total days should be numbers and should between 1 and 365")
        except ValueError as e:
            wx.MessageBox(f"Invalid total days: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.db_manager.query_price_distribution_data(valid_date,total_days)



    def on_kword_input_btn_clicked(self,event):
        # Get selected date
        year = self.m_choice112.GetStringSelection()
        month = self.m_choice14.GetStringSelection()
        day = self.m_choice122.GetStringSelection()

        # validate date input
        try:
            valid_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            test = datetime.strptime(valid_date, "%Y-%m-%d")
        except ValueError:
            wx.MessageBox("Selected date is invalid. Please choose a valid date")
            return

        # Get total of days
        total_days = self.total_days_input.GetValue()
        if not total_days or total_days == "":
            wx.MessageBox(f"Invalid total days: Input is empty", "Error", wx.OK | wx.ICON_ERROR)
            return
        # validate total_days input
        try:
            total_days = int(total_days)
            if not (0 < total_days < 365):
                raise ValueError("Total days should be numbers and should between 1 and 365")
        except ValueError as e:
            wx.MessageBox(f"Invalid total days: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return

        kword = self.kword_input.GetValue()
        if not kword or kword == "":
            wx.MessageBox(f"Invalid keyword input: Input is empty!", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.db_manager.query_kword_data(valid_date,total_days,kword)

        pass

    def on_tendency_btn_clicked(self,event):
        # Get selected surburb
        checked_items = self.m_checkList11.GetCheckedItems()
        selected_suburbs = [self.m_checkList11.GetString(i) for i in checked_items]
        if len(selected_suburbs) == 0:
            wx.MessageBox("You have not select any surburb, please select at least one surburb to query data!")
            return

        # Get selected date
        year = self.m_choice113.GetStringSelection()
        month = self.m_choice15.GetStringSelection()
        day = self.m_choice123.GetStringSelection()

        # validate date input
        try:
            valid_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            test = datetime.strptime(valid_date, "%Y-%m-%d")
        except ValueError:
            wx.MessageBox("Selected date is invalid. Please choose a valid date")
            return

        # Get total of days
        total_days = self.m_textCtrl12.GetValue()

        if not total_days or total_days == "":
            wx.MessageBox(f"Invalid total days: Input is empty", "Error", wx.OK | wx.ICON_ERROR)
            return

        # validate total_days input
        try:
            total_days = int(total_days)
            if not (0 < total_days < 365):
                raise ValueError("Total days should be numbers and should between 1 and 365")
        except ValueError as e:
            wx.MessageBox(f"Invalid total days: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.db_manager.query_tendency_data(selected_suburbs,valid_date,total_days)


