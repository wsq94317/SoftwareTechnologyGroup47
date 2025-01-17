# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainView
###########################################################################

class MainView ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Airbnb Data Analyser", pos = wx.DefaultPosition, size = wx.Size( 1706,645 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.Menu = wx.Menu()
        self.quit_software = wx.MenuItem( self.Menu, wx.ID_ANY, u"Quit Software", wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu.Append( self.quit_software )

        self.return_to_front_page = wx.MenuItem( self.Menu, wx.ID_ANY, u"Return to front page", wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu.Append( self.return_to_front_page )

        self.m_menubar1.Append( self.Menu, u"Menu" )

        self.SetMenuBar( self.m_menubar1 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.MainPanel.Hide()

        bSizer131 = wx.BoxSizer( wx.VERTICAL )


        bSizer131.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bitmap1 = wx.StaticBitmap( self.MainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
        bSizer6.Add( self.m_bitmap1, 0, wx.ALL|wx.SHAPED, 5 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Airbnb Data Analyser", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE|wx.ST_ELLIPSIZE_START|wx.ST_NO_AUTORESIZE )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer9.Add( self.m_staticText8, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer9, 1, wx.ALIGN_CENTER, 5 )


        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Show Data by Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer18.Add( self.m_staticText2, 0, wx.ALL, 5 )


        bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.location_data_btn = wx.Button( self.MainPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.location_data_btn, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText21 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Show Price Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer19.Add( self.m_staticText21, 0, wx.ALL, 5 )


        bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.price_dist_btn = wx.Button( self.MainPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer19.Add( self.price_dist_btn, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText22 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Search Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer20.Add( self.m_staticText22, 0, wx.ALL, 5 )


        bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.kword_btn = wx.Button( self.MainPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer20.Add( self.kword_btn, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText23 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Cleaniess Report", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer21.Add( self.m_staticText23, 0, wx.ALL, 5 )


        bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.cleaniess_btn = wx.Button( self.MainPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.cleaniess_btn, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer21, 1, wx.EXPAND, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText24 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Show Price Trends", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        bSizer22.Add( self.m_staticText24, 0, wx.ALL, 5 )


        bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.price_trends_btn = wx.Button( self.MainPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.price_trends_btn, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer22, 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer1, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer131.Add( bSizer6, 1, wx.EXPAND, 5 )


        bSizer131.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.MainPanel.SetSizer( bSizer131 )
        self.MainPanel.Layout()
        bSizer131.Fit( self.MainPanel )
        bSizer5.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.ShowDataByLoc = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.ShowDataByLoc.Hide()

        bSizer15 = wx.BoxSizer( wx.VERTICAL )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText18 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Check Airbnb Data By Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        self.m_staticText18.SetFont( wx.Font( 25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer26.Add( self.m_staticText18, 0, wx.ALL, 5 )


        bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer15.Add( bSizer26, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Select Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

        m_checkList1Choices = []
        self.m_checkList1 = wx.CheckListBox( self.ShowDataByLoc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
        bSizer8.Add( self.m_checkList1, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer8, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText91 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Start date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91.Wrap( -1 )

        bSizer91.Add( self.m_staticText91, 0, wx.ALL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText911 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText911.Wrap( -1 )

        bSizer10.Add( self.m_staticText911, 0, wx.ALL, 5 )

        m_choice11Choices = []
        self.m_choice11 = wx.Choice( self.ShowDataByLoc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
        self.m_choice11.SetSelection( 0 )
        bSizer10.Add( self.m_choice11, 0, wx.ALL, 5 )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText9111 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Month", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9111.Wrap( -1 )

        bSizer10.Add( self.m_staticText9111, 0, wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self.ShowDataByLoc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer10.Add( self.m_choice1, 0, wx.ALL, 5 )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText9112 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9112.Wrap( -1 )

        bSizer10.Add( self.m_staticText9112, 0, wx.ALL, 5 )

        m_choice12Choices = []
        self.m_choice12 = wx.Choice( self.ShowDataByLoc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice12Choices, 0 )
        self.m_choice12.SetSelection( 0 )
        bSizer10.Add( self.m_choice12, 0, wx.ALL, 5 )


        bSizer91.Add( bSizer10, 1, wx.EXPAND, 5 )


        bSizer12.Add( bSizer91, 1, wx.EXPAND, 5 )

        bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText81 = wx.StaticText( self.ShowDataByLoc, wx.ID_ANY, u"Total query days", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        bSizer111.Add( self.m_staticText81, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self.ShowDataByLoc, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer111.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


        bSizer12.Add( bSizer111, 1, wx.EXPAND, 5 )


        bSizer13.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.return_btn = wx.Button( self.ShowDataByLoc, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer27.Add( self.return_btn, 0, wx.ALL, 5 )


        bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.query_loc_btn = wx.Button( self.ShowDataByLoc, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer27.Add( self.query_loc_btn, 0, wx.ALL, 5 )


        bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer13.Add( bSizer27, 1, wx.EXPAND, 5 )


        bSizer11.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer15.Add( bSizer11, 1, wx.EXPAND, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.ShowDataByLoc.SetSizer( bSizer15 )
        self.ShowDataByLoc.Layout()
        bSizer15.Fit( self.ShowDataByLoc )
        bSizer5.Add( self.ShowDataByLoc, 1, wx.EXPAND |wx.ALL, 5 )

        self.PriceDistributePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.PriceDistributePanel.Hide()

        bSizer151 = wx.BoxSizer( wx.VERTICAL )


        bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer261 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer261.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText181 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Check Price Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText181.Wrap( -1 )

        self.m_staticText181.SetFont( wx.Font( 25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer261.Add( self.m_staticText181, 0, wx.ALL, 5 )


        bSizer261.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer151.Add( bSizer261, 1, wx.EXPAND, 5 )

        bSizer112 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer132 = wx.BoxSizer( wx.VERTICAL )

        bSizer121 = wx.BoxSizer( wx.VERTICAL )

        bSizer911 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText912 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Start date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText912.Wrap( -1 )

        bSizer911.Add( self.m_staticText912, 0, wx.ALL, 5 )

        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9113 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9113.Wrap( -1 )

        bSizer101.Add( self.m_staticText9113, 0, wx.ALL, 5 )

        m_choice111Choices = []
        self.m_choice111 = wx.Choice( self.PriceDistributePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice111Choices, 0 )
        self.m_choice111.SetSelection( 0 )
        bSizer101.Add( self.m_choice111, 0, wx.ALL, 5 )


        bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91111 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Month", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91111.Wrap( -1 )

        bSizer101.Add( self.m_staticText91111, 0, wx.ALL, 5 )

        m_choice13Choices = []
        self.m_choice13 = wx.Choice( self.PriceDistributePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice13Choices, 0 )
        self.m_choice13.SetSelection( 0 )
        bSizer101.Add( self.m_choice13, 0, wx.ALL, 5 )


        bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91121 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91121.Wrap( -1 )

        bSizer101.Add( self.m_staticText91121, 0, wx.ALL, 5 )

        m_choice121Choices = []
        self.m_choice121 = wx.Choice( self.PriceDistributePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice121Choices, 0 )
        self.m_choice121.SetSelection( 0 )
        bSizer101.Add( self.m_choice121, 0, wx.ALL, 5 )


        bSizer911.Add( bSizer101, 1, wx.EXPAND, 5 )


        bSizer121.Add( bSizer911, 1, wx.EXPAND, 5 )

        bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText811 = wx.StaticText( self.PriceDistributePanel, wx.ID_ANY, u"Total query days", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText811.Wrap( -1 )

        bSizer1111.Add( self.m_staticText811, 0, wx.ALL, 5 )

        self.m_textCtrl11 = wx.TextCtrl( self.PriceDistributePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1111.Add( self.m_textCtrl11, 0, wx.ALL, 5 )


        bSizer121.Add( bSizer1111, 1, wx.EXPAND, 5 )


        bSizer132.Add( bSizer121, 1, wx.EXPAND, 5 )

        bSizer271 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.return_btn1 = wx.Button( self.PriceDistributePanel, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer271.Add( self.return_btn1, 0, wx.ALL, 5 )


        bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.search_price_dist_btn = wx.Button( self.PriceDistributePanel, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer271.Add( self.search_price_dist_btn, 0, wx.ALL, 5 )


        bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer132.Add( bSizer271, 1, wx.EXPAND, 5 )


        bSizer112.Add( bSizer132, 1, wx.EXPAND, 5 )


        bSizer112.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer151.Add( bSizer112, 1, wx.EXPAND, 5 )


        bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.PriceDistributePanel.SetSizer( bSizer151 )
        self.PriceDistributePanel.Layout()
        bSizer151.Fit( self.PriceDistributePanel )
        bSizer5.Add( self.PriceDistributePanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.KeyWordSearchPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.KeyWordSearchPanel.Hide()

        bSizer152 = wx.BoxSizer( wx.VERTICAL )


        bSizer152.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer262 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer262.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText182 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Check Airbnb Data By Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText182.Wrap( -1 )

        self.m_staticText182.SetFont( wx.Font( 25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer262.Add( self.m_staticText182, 0, wx.ALL, 5 )


        bSizer262.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer152.Add( bSizer262, 1, wx.EXPAND, 5 )

        bSizer113 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer113.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer133 = wx.BoxSizer( wx.VERTICAL )

        bSizer122 = wx.BoxSizer( wx.VERTICAL )

        bSizer912 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText913 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Start date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText913.Wrap( -1 )

        bSizer912.Add( self.m_staticText913, 0, wx.ALL, 5 )

        bSizer102 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9114 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9114.Wrap( -1 )

        bSizer102.Add( self.m_staticText9114, 0, wx.ALL, 5 )

        m_choice112Choices = []
        self.m_choice112 = wx.Choice( self.KeyWordSearchPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice112Choices, 0 )
        self.m_choice112.SetSelection( 0 )
        bSizer102.Add( self.m_choice112, 0, wx.ALL, 5 )


        bSizer102.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91112 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Month", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91112.Wrap( -1 )

        bSizer102.Add( self.m_staticText91112, 0, wx.ALL, 5 )

        m_choice14Choices = []
        self.m_choice14 = wx.Choice( self.KeyWordSearchPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice14Choices, 0 )
        self.m_choice14.SetSelection( 0 )
        bSizer102.Add( self.m_choice14, 0, wx.ALL, 5 )


        bSizer102.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91122 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91122.Wrap( -1 )

        bSizer102.Add( self.m_staticText91122, 0, wx.ALL, 5 )

        m_choice122Choices = []
        self.m_choice122 = wx.Choice( self.KeyWordSearchPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice122Choices, 0 )
        self.m_choice122.SetSelection( 0 )
        bSizer102.Add( self.m_choice122, 0, wx.ALL, 5 )


        bSizer912.Add( bSizer102, 1, wx.EXPAND, 5 )


        bSizer122.Add( bSizer912, 1, wx.EXPAND, 5 )

        bSizer1112 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText34 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Total Days", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )

        bSizer1112.Add( self.m_staticText34, 0, wx.ALL, 5 )

        self.total_days_input = wx.TextCtrl( self.KeyWordSearchPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1112.Add( self.total_days_input, 0, wx.ALL, 5 )


        bSizer1112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText812 = wx.StaticText( self.KeyWordSearchPanel, wx.ID_ANY, u"Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText812.Wrap( -1 )

        bSizer1112.Add( self.m_staticText812, 0, wx.ALL, 5 )

        self.kword_input = wx.TextCtrl( self.KeyWordSearchPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1112.Add( self.kword_input, 0, wx.ALL, 5 )


        bSizer122.Add( bSizer1112, 1, wx.EXPAND, 5 )


        bSizer133.Add( bSizer122, 1, wx.EXPAND, 5 )

        bSizer272 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer272.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.return_btn2 = wx.Button( self.KeyWordSearchPanel, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer272.Add( self.return_btn2, 0, wx.ALL, 5 )


        bSizer272.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.kword_input_btn = wx.Button( self.KeyWordSearchPanel, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer272.Add( self.kword_input_btn, 0, wx.ALL, 5 )


        bSizer272.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer133.Add( bSizer272, 1, wx.EXPAND, 5 )


        bSizer113.Add( bSizer133, 1, wx.EXPAND, 5 )


        bSizer113.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer152.Add( bSizer113, 1, wx.EXPAND, 5 )


        bSizer152.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.KeyWordSearchPanel.SetSizer( bSizer152 )
        self.KeyWordSearchPanel.Layout()
        bSizer152.Fit( self.KeyWordSearchPanel )
        bSizer5.Add( self.KeyWordSearchPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.TendencyPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.TendencyPanel.Hide()

        bSizer153 = wx.BoxSizer( wx.VERTICAL )


        bSizer153.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer263 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer263.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText183 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Check Price Trends By Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText183.Wrap( -1 )

        self.m_staticText183.SetFont( wx.Font( 25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer263.Add( self.m_staticText183, 0, wx.ALL, 5 )


        bSizer263.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer153.Add( bSizer263, 1, wx.EXPAND, 5 )

        bSizer114 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer114.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer134 = wx.BoxSizer( wx.VERTICAL )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText92 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Select Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText92.Wrap( -1 )

        bSizer81.Add( self.m_staticText92, 0, wx.ALL, 5 )

        m_checkList11Choices = []
        self.m_checkList11 = wx.CheckListBox( self.TendencyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList11Choices, wx.LB_EXTENDED )
        bSizer81.Add( self.m_checkList11, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer134.Add( bSizer81, 1, wx.EXPAND, 5 )

        bSizer123 = wx.BoxSizer( wx.VERTICAL )

        bSizer913 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText914 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Start date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText914.Wrap( -1 )

        bSizer913.Add( self.m_staticText914, 0, wx.ALL, 5 )

        bSizer103 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9115 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9115.Wrap( -1 )

        bSizer103.Add( self.m_staticText9115, 0, wx.ALL, 5 )

        m_choice113Choices = []
        self.m_choice113 = wx.Choice( self.TendencyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice113Choices, 0 )
        self.m_choice113.SetSelection( 0 )
        bSizer103.Add( self.m_choice113, 0, wx.ALL, 5 )


        bSizer103.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91113 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Month", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91113.Wrap( -1 )

        bSizer103.Add( self.m_staticText91113, 0, wx.ALL, 5 )

        m_choice15Choices = []
        self.m_choice15 = wx.Choice( self.TendencyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice15Choices, 0 )
        self.m_choice15.SetSelection( 0 )
        bSizer103.Add( self.m_choice15, 0, wx.ALL, 5 )


        bSizer103.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText91123 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91123.Wrap( -1 )

        bSizer103.Add( self.m_staticText91123, 0, wx.ALL, 5 )

        m_choice123Choices = []
        self.m_choice123 = wx.Choice( self.TendencyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice123Choices, 0 )
        self.m_choice123.SetSelection( 0 )
        bSizer103.Add( self.m_choice123, 0, wx.ALL, 5 )


        bSizer913.Add( bSizer103, 1, wx.EXPAND, 5 )


        bSizer123.Add( bSizer913, 1, wx.EXPAND, 5 )

        bSizer1113 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText813 = wx.StaticText( self.TendencyPanel, wx.ID_ANY, u"Total query days", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText813.Wrap( -1 )

        bSizer1113.Add( self.m_staticText813, 0, wx.ALL, 5 )

        self.m_textCtrl12 = wx.TextCtrl( self.TendencyPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1113.Add( self.m_textCtrl12, 0, wx.ALL, 5 )


        bSizer123.Add( bSizer1113, 1, wx.EXPAND, 5 )


        bSizer134.Add( bSizer123, 1, wx.EXPAND, 5 )

        bSizer273 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer273.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.return_btn3 = wx.Button( self.TendencyPanel, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer273.Add( self.return_btn3, 0, wx.ALL, 5 )


        bSizer273.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.generate_tendency_btn = wx.Button( self.TendencyPanel, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer273.Add( self.generate_tendency_btn, 0, wx.ALL, 5 )


        bSizer273.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer134.Add( bSizer273, 1, wx.EXPAND, 5 )


        bSizer114.Add( bSizer134, 1, wx.EXPAND, 5 )


        bSizer114.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer153.Add( bSizer114, 1, wx.EXPAND, 5 )


        bSizer153.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.TendencyPanel.SetSizer( bSizer153 )
        self.TendencyPanel.Layout()
        bSizer153.Fit( self.TendencyPanel )
        bSizer5.Add( self.TendencyPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.LocationResPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.LocationResPanel.Hide()

        bSizer54 = wx.BoxSizer( wx.VERTICAL )

        self.back_btn = wx.Button( self.LocationResPanel, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer54.Add( self.back_btn, 0, wx.ALL, 5 )

        self.m_staticText35 = wx.StaticText( self.LocationResPanel, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText35.Wrap( -1 )

        self.m_staticText35.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText35.SetMinSize( wx.Size( -1,30 ) )

        bSizer54.Add( self.m_staticText35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.location_res_table = wx.ListCtrl( self.LocationResPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer54.Add( self.location_res_table, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.SHAPED, 5 )


        self.LocationResPanel.SetSizer( bSizer54 )
        self.LocationResPanel.Layout()
        bSizer54.Fit( self.LocationResPanel )
        bSizer5.Add( self.LocationResPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.DirstributionFigurePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.DirstributionFigurePanel.Hide()

        bSizer58 = wx.BoxSizer( wx.VERTICAL )

        self.back_btn1 = wx.Button( self.DirstributionFigurePanel, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer58.Add( self.back_btn1, 0, wx.ALL, 5 )

        self.m_staticText36 = wx.StaticText( self.DirstributionFigurePanel, wx.ID_ANY, u"Price Distribution Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        self.m_staticText36.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer58.Add( self.m_staticText36, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        boxsizer = wx.BoxSizer( wx.VERTICAL )

        self.distribution_figure_container = wx.Panel( self.DirstributionFigurePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        boxsizer.Add( self.distribution_figure_container, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer58.Add( boxsizer, 1, wx.EXPAND, 5 )


        self.DirstributionFigurePanel.SetSizer( bSizer58 )
        self.DirstributionFigurePanel.Layout()
        bSizer58.Fit( self.DirstributionFigurePanel )
        bSizer5.Add( self.DirstributionFigurePanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.KwordResultPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.KwordResultPanel.Hide()

        bSizer53 = wx.BoxSizer( wx.VERTICAL )

        self.back_btn11 = wx.Button( self.KwordResultPanel, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer53.Add( self.back_btn11, 0, wx.ALL, 5 )

        self.m_staticText361 = wx.StaticText( self.KwordResultPanel, wx.ID_ANY, u"Keyword Search Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText361.Wrap( -1 )

        self.m_staticText361.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer53.Add( self.m_staticText361, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        bSizer55 = wx.BoxSizer( wx.VERTICAL )

        bSizer57 = wx.BoxSizer( wx.VERTICAL )

        self.HouseResultPanel = wx.Panel( self.KwordResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer59 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText362 = wx.StaticText( self.HouseResultPanel, wx.ID_ANY, u"Matched Houses Record", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText362.Wrap( -1 )

        self.m_staticText362.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer59.Add( self.m_staticText362, 0, wx.ALL, 5 )

        self.matched_house_table = wx.ListCtrl( self.HouseResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer59.Add( self.matched_house_table, 0, wx.ALL|wx.EXPAND, 5 )


        self.HouseResultPanel.SetSizer( bSizer59 )
        self.HouseResultPanel.Layout()
        bSizer59.Fit( self.HouseResultPanel )
        bSizer57.Add( self.HouseResultPanel, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer55.Add( bSizer57, 1, wx.EXPAND, 5 )

        bSizer581 = wx.BoxSizer( wx.VERTICAL )

        self.CommentResultPanel = wx.Panel( self.KwordResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer60 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText3621 = wx.StaticText( self.CommentResultPanel, wx.ID_ANY, u"Matched Comments Record", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3621.Wrap( -1 )

        self.m_staticText3621.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer60.Add( self.m_staticText3621, 0, wx.ALL, 5 )

        self.matched_comment_table = wx.ListCtrl( self.CommentResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer60.Add( self.matched_comment_table, 0, wx.ALL|wx.EXPAND, 5 )


        self.CommentResultPanel.SetSizer( bSizer60 )
        self.CommentResultPanel.Layout()
        bSizer60.Fit( self.CommentResultPanel )
        bSizer581.Add( self.CommentResultPanel, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer55.Add( bSizer581, 1, wx.EXPAND, 5 )


        bSizer53.Add( bSizer55, 1, wx.EXPAND, 5 )


        self.KwordResultPanel.SetSizer( bSizer53 )
        self.KwordResultPanel.Layout()
        bSizer53.Fit( self.KwordResultPanel )
        bSizer5.Add( self.KwordResultPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.CleanResultPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer531 = wx.BoxSizer( wx.VERTICAL )

        self.back_btn111 = wx.Button( self.CleanResultPanel, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer531.Add( self.back_btn111, 0, wx.ALL, 5 )

        self.m_staticText3611 = wx.StaticText( self.CleanResultPanel, wx.ID_ANY, u"Summary of Cleaniess By User Comment", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3611.Wrap( -1 )

        self.m_staticText3611.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer531.Add( self.m_staticText3611, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.cleaness_report_table = wx.ListCtrl( self.CleanResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
        bSizer531.Add( self.cleaness_report_table, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.SHAPED, 5 )


        self.CleanResultPanel.SetSizer( bSizer531 )
        self.CleanResultPanel.Layout()
        bSizer531.Fit( self.CleanResultPanel )
        bSizer5.Add( self.CleanResultPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.TendencyFigurePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.TendencyFigurePanel.Hide()

        bSizer582 = wx.BoxSizer( wx.VERTICAL )

        self.back_btn12 = wx.Button( self.TendencyFigurePanel, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer582.Add( self.back_btn12, 0, wx.ALL, 5 )

        self.m_staticText363 = wx.StaticText( self.TendencyFigurePanel, wx.ID_ANY, u"Price Tendency Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText363.Wrap( -1 )

        self.m_staticText363.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer582.Add( self.m_staticText363, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        boxsizer1 = wx.BoxSizer( wx.VERTICAL )

        self.tendency_figure_container = wx.Panel( self.TendencyFigurePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        boxsizer1.Add( self.tendency_figure_container, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer582.Add( boxsizer1, 1, wx.EXPAND, 5 )


        self.TendencyFigurePanel.SetSizer( bSizer582 )
        self.TendencyFigurePanel.Layout()
        bSizer582.Fit( self.TendencyFigurePanel )
        bSizer5.Add( self.TendencyFigurePanel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


