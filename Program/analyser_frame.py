import wx
from database_manager import DatabaseManager
from main_view import MainView as mv
from datetime import datetime
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class AnalyserApp(mv):
    def __init__(self):
        super().__init__(None)
        # 1. load data from Database manager
        self.db_manager = DatabaseManager()
        img_path = "./resource/icon.jpg"
        bitmap = wx.Bitmap(img_path, wx.BITMAP_TYPE_JPEG)
        self.m_bitmap1.SetBitmap(bitmap)
        # avoid multiple initialisation grid panel
        self.house_grid_created = False

        self.surburb_dict = self.db_manager.get_surburb_list()

        self.min_year,self.max_year = self.db_manager.get_year_range()
        # initialise views
        self.init_location_view()
        self.init_price_distribution_view()
        self.init_keyword_search_view()
        self.init_tendency_view()

        # init widget panel switcher
        self.init_widget_switcher()

        #Connect Events
        self.register_delegates()

    def register_delegates(self):
        self.location_data_btn.Bind( wx.EVT_BUTTON, self.on_location_btn_clicked )
        self.kword_btn.Bind( wx.EVT_BUTTON, self.on_kword_btn_clicked )
        self.price_dist_btn.Bind( wx.EVT_BUTTON, self.on_price_dist_btn_clicked )
        self.cleaniess_btn.Bind( wx.EVT_BUTTON, self.on_cleaniess_btn_clicked )
        self.price_trends_btn.Bind( wx.EVT_BUTTON, self.on_price_trends_btn_clicked )

        self.Bind(wx.EVT_MENU, self.on_quit_software_btn_clicked, self.quit_software)
        self.Bind(wx.EVT_MENU, self.back_to_home, self.return_to_front_page)

        self.return_btn.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn1.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn2.Bind(wx.EVT_BUTTON,self.back_to_home)
        self.return_btn3.Bind(wx.EVT_BUTTON,self.back_to_home)

        self.back_btn.Bind(wx.EVT_BUTTON,self.on_back_btn_clicked)
        self.back_btn1.Bind(wx.EVT_BUTTON,self.on_back_btn_clicked)
        self.back_btn11.Bind(wx.EVT_BUTTON,self.on_back_btn_clicked)
        self.back_btn111.Bind(wx.EVT_BUTTON,self.on_back_btn_clicked)
        self.back_btn12.Bind(wx.EVT_BUTTON,self.on_back_btn_clicked)


        self.kword_input_btn.Bind(wx.EVT_BUTTON,self.on_kword_input_btn_clicked)
        self.query_loc_btn.Bind(wx.EVT_BUTTON,self.on_query_loc_btn_clicked)
        self.search_price_dist_btn.Bind(wx.EVT_BUTTON,self.on_price_distribution_btn_clicked)
        self.generate_tendency_btn.Bind(wx.EVT_BUTTON,self.on_tendency_btn_clicked)

    def init_widget_switcher(self):
        self.active_widget_index = 0
        self.last_page_index = 0
        self.MainPanel.Show()
        self.ShowDataByLoc.Hide()
        self.PriceDistributePanel.Hide()
        self.KeyWordSearchPanel.Hide()
        self.TendencyPanel.Hide()
        self.LocationResPanel.Hide()
        self.DirstributionFigurePanel.Hide()
        self.KwordResultPanel.Hide()
        self.CleanResultPanel.Hide()
        self.TendencyFigurePanel.Hide()
        self.widget_panel = [self.MainPanel,self.ShowDataByLoc,self.PriceDistributePanel,self.KeyWordSearchPanel,self.TendencyPanel,self.LocationResPanel,self.DirstributionFigurePanel,self.KwordResultPanel,self.CleanResultPanel,self.TendencyFigurePanel]
        self.Layout()

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

    def refresh_price_figure(self,fig):
        # clean existing components
        for child in self.distribution_figure_container.GetChildren():
            child.Destroy()

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.distribution_figure_container.SetSizer(sizer)
        canvas = FigureCanvas(self.distribution_figure_container, -1, fig)

        sizer.Add(canvas, 1, wx.EXPAND)

        self.distribution_figure_container.Layout()
        self.set_active_widget_index(6)
        self.Layout()


    def refresh_location_res_table(self,df):
        if len(df) == 0:
            wx.MessageBox("No Result Matched!")
            return
        self.set_active_widget_index(5)
        self.location_res_table.DeleteAllItems()
        # self.location_res_table.AppendTextColumn("Listing ID")
        # self.location_res_table.AppendTextColumn("NAME")
        # self.location_res_table.AppendTextColumn("Summary")
        # self.location_res_table.AppendTextColumn("Space")
        # self.location_res_table.AppendTextColumn("Description")
        # self.location_res_table.AppendTextColumn("Experience Offered")
        # self.location_res_table.AppendTextColumn("Neighbourhood Overview")
        # self.location_res_table.AppendTextColumn("Notes")
        # self.location_res_table.AppendTextColumn("Transit")
        # self.location_res_table.AppendTextColumn("Access")
        # self.location_res_table.AppendTextColumn("Interaction")
        # self.location_res_table.AppendTextColumn("House Rules")
        # self.location_res_table.AppendTextColumn("Surburb Name")
        # self.location_res_table.AppendTextColumn("City")
        # self.location_res_table.AppendTextColumn("Country")
        # self.location_res_table.AppendTextColumn("Zipcode")
        # for item in df:
        #     self.location_res_table.AppendItem([text for text in item])
        # self.location_res_table.Refresh()
        columns = [
            "Listing ID", "NAME", "Summary", "Space", "Description",
            "Experience Offered", "Neighbourhood Overview", "Notes", "Transit",
            "Access", "Interaction", "House Rules", "Surburb Name",
            "City", "Country", "Zipcode"
        ]

        for col, header in enumerate(columns):
            self.location_res_table.InsertColumn(col, header)

        for item in df:
            index = self.location_res_table.InsertItem(self.location_res_table.GetItemCount(), str(item[0]))
            for col, text in enumerate(item[1:], 1):
                self.location_res_table.SetItem(index, col, str(text))

        self.location_res_table.Refresh()


    def set_active_widget_index(self,index):
        if self.active_widget_index == index or index < 0:
            return
        self.last_page_index = self.active_widget_index
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
        res = self.db_manager.fetch_clean_related_comments()
        if not res or len(res) == 0:
            wx.MessageBox("No Result Founded!")
            return

        self.refresh_clean_result(res)


    def on_price_trends_btn_clicked(self,event):
        self.set_active_widget_index(4)

    def on_quit_software_btn_clicked(self,event):
        self.Close(True)


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

        result_data = self.db_manager.query_location_data(selected_suburbs,valid_date,total_days)
        self.refresh_location_res_table(result_data)



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

        fig = self.db_manager.query_price_distribution_data(valid_date,total_days)
        if not fig or type(fig) == 'NoneType':
            wx.MessageBox("No Result Matched!")
            return
        self.refresh_price_figure(fig)




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

        houses,comments = self.db_manager.query_kword_data(valid_date,total_days,kword)
        self.refresh_kword_result_panel(houses,comments)

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

        fig_list = self.db_manager.query_tendency_data(selected_suburbs,valid_date,total_days)
        self.refresh_tendency_result(fig_list)

    def on_back_btn_clicked(self,event):
        self.set_active_widget_index(self.last_page_index if self.last_page_index else 0)

    def refresh_kword_result_panel(self,house,comments):
        if  not house and not comments:
            wx.MessageBox("No result matched!")
            return

        display_columns = [
            "listing_id", "name", "summary", "space", "description", "experiences_offered",
            "neighborhood_overview", "notes", "transit", "access", "interaction",
            "house_rules", "surburb_id", "city", "country", "zipcode"
        ]

        self.set_active_widget_index(7)
        if not house:
            self.HouseResultPanel.Hide()
        else:
            self.HouseResultPanel.Show()
            # First clear the table
            self.matched_house_table.DeleteAllItems()


            if self.matched_house_table.GetColumnCount() == 0:
                self.matched_house_table.InsertColumn(0,"Listing ID")
                self.matched_house_table.InsertColumn(1, "House Name")
                self.matched_house_table.InsertColumn(2, "House Summary")
                self.matched_house_table.InsertColumn(3, "House Space")
                self.matched_house_table.InsertColumn(4, "House Description")
                self.matched_house_table.InsertColumn(5, "Experience Offered")
                self.matched_house_table.InsertColumn(6, "Neighbourhood Overview")
                self.matched_house_table.InsertColumn(7, "Notes")
                self.matched_house_table.InsertColumn(8,"House Transit")
                self.matched_house_table.InsertColumn(9, "House Access")
                self.matched_house_table.InsertColumn(10, "House Interaction")
                self.matched_house_table.InsertColumn(11, "House Rules")
                self.matched_house_table.InsertColumn(12, "Suburb Name")
                self.matched_house_table.InsertColumn(13, "City")
                self.matched_house_table.InsertColumn(14, "Country")
                self.matched_house_table.InsertColumn(15, "Zipcode")

            for row in house:
                pos = self.matched_house_table.InsertItem(1000000,str(row[0]))
                for col_num, col_val in enumerate(row):
                    self.matched_house_table.SetItem(pos, col_num, str(col_val))

        if not comments:
            self.CommentResultPanel.Hide()
        else:
            self.CommentResultPanel.Show()

            self.matched_comment_table.DeleteAllItems()

            if not comments:
                self.CommentResultPanel.Hide()
            else:
                self.CommentResultPanel.Show()

                self.matched_comment_table.DeleteAllItems()

                if self.matched_comment_table.GetColumnCount() == 0:
                    self.matched_comment_table.InsertColumn(0, "Listing ID")
                    self.matched_comment_table.InsertColumn(1, "Reviewer Name")
                    self.matched_comment_table.InsertColumn(2, "Comments")

                # Add comments data to the wxListCtrl
                for row in comments:
                    pos = self.matched_comment_table.InsertItem(1000000, str(row[0]))
                    self.matched_comment_table.SetItem(pos, 1, str(row[1]))
                    self.matched_comment_table.SetItem(pos, 2,str(row[2]))


    def refresh_clean_result(self, res):
        self.set_active_widget_index(8)

        if self.cleaness_report_table.GetColumnCount() == 0:
            columns = ["House ID", "House Name", "Total Comments", "Amount of comments mention about cleaniess","Percentage of cleaniess comments"]
            for col_name in columns:
                self.cleaness_report_table.InsertColumn(columns.index(col_name), col_name)

        self.cleaness_report_table.DeleteAllItems()

        for row in res:
            index = self.cleaness_report_table.InsertItem(1000000, str(row[0]))  # Start inserting at a large index for appending
            for col_num, value in enumerate(row):
                self.cleaness_report_table.SetItem(index, col_num, str(value))

            if row[2] != 0:
                percentage = (row[3] / row[2]) * 100
            else:
                percentage = 0
            self.cleaness_report_table.SetItem(index, 4, f"{percentage:.2f}%")

    def refresh_tendency_result(self,figure_list):
        if not figure_list or len(figure_list) == 0:
            wx.MessageBox("No Result Matches selected surburb!")
            return
        self.set_active_widget_index(9)
        for child in self.tendency_figure_container.GetChildren():
            child.Destroy()

        scrolled_window = wx.ScrolledWindow(self.tendency_figure_container, -1)
        scrolled_window.SetScrollRate(5,5)

        sizer = wx.BoxSizer(wx.VERTICAL)


        for figure in figure_list:
            canvas = FigureCanvas(scrolled_window, -1, figure)
            sizer.Add(canvas, 1, wx.EXPAND)


        # self.tendency_figure_container.SetSizer(sizer)
        # self.tendency_figure_container.Layout()
        scrolled_window.SetSizer(sizer)
        scrolled_window.Layout()
        scrolled_window.FitInside()

        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        panel_sizer.Add(scrolled_window,1, wx.EXPAND)
        self.tendency_figure_container.SetSizer(panel_sizer)
        self.tendency_figure_container.Layout()