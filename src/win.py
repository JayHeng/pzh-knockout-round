# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class knockoutWin
###########################################################################

class knockoutWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Knockout", pos = wx.DefaultPosition, size = wx.Size( 1039,504 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_win = wx.BoxSizer( wx.VERTICAL )

		wSizer_func = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_setup = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_textCtrl_playerList = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,300 ), wx.TE_MULTILINE )
		self.m_textCtrl_playerList.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer2.Add( self.m_textCtrl_playerList, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 5,-1 ), 0 )
		self.m_staticText28.Wrap( -1 )

		wSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_button_editPlayer = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit Player", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer2.Add( self.m_button_editPlayer, 0, wx.ALL, 5 )

		self.m_staticText281 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 5,-1 ), 0 )
		self.m_staticText281.Wrap( -1 )

		wSizer2.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.m_staticText2812 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 5,-1 ), 0 )
		self.m_staticText2812.Wrap( -1 )

		wSizer2.Add( self.m_staticText2812, 0, wx.ALL, 5 )

		self.m_button_createKnockout = wx.Button( self.m_panel1, wx.ID_ANY, u"Create Knockout", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer2.Add( self.m_button_createKnockout, 0, wx.ALL, 5 )

		self.m_staticText2811 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 5,-1 ), 0 )
		self.m_staticText2811.Wrap( -1 )

		wSizer2.Add( self.m_staticText2811, 0, wx.ALL, 5 )

		self.m_staticText2813 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 5,-1 ), 0 )
		self.m_staticText2813.Wrap( -1 )

		wSizer2.Add( self.m_staticText2813, 0, wx.ALL, 5 )

		self.m_button_clearKnockout = wx.Button( self.m_panel1, wx.ID_ANY, u"Clear Knockout", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer2.Add( self.m_button_clearKnockout, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( wSizer2 )
		self.m_panel1.Layout()
		wSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Player", False )

		bSizer_setup.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer_func.Add( bSizer_setup, 1, wx.EXPAND, 5 )

		bSizer_knockout = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 840,1 ), 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer_knockout.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"        A1 vs A2" ), wx.VERTICAL )

		self.m_textCtrl_top16a1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer1.Add( self.m_textCtrl_top16a1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16a2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer1.Add( self.m_textCtrl_top16a2, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( sbSizer1 )
		self.m_panel7.Layout()
		sbSizer1.Fit( self.m_panel7 )
		bSizer4.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"        B1 vs B2" ), wx.VERTICAL )

		self.m_textCtrl_top16b1 = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer11.Add( self.m_textCtrl_top16b1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16b2 = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer11.Add( self.m_textCtrl_top16b2, 0, wx.ALL, 5 )


		self.m_panel8.SetSizer( sbSizer11 )
		self.m_panel8.Layout()
		sbSizer11.Fit( self.m_panel8 )
		bSizer4.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel9 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, u"        C1 vs C2" ), wx.VERTICAL )

		self.m_textCtrl_top16c1 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer12.Add( self.m_textCtrl_top16c1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16c2 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer12.Add( self.m_textCtrl_top16c2, 0, wx.ALL, 5 )


		self.m_panel9.SetSizer( sbSizer12 )
		self.m_panel9.Layout()
		sbSizer12.Fit( self.m_panel9 )
		bSizer4.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"        D1 vs D2" ), wx.VERTICAL )

		self.m_textCtrl_top16d1 = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer13.Add( self.m_textCtrl_top16d1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16d2 = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer13.Add( self.m_textCtrl_top16d2, 0, wx.ALL, 5 )


		self.m_panel10.SetSizer( sbSizer13 )
		self.m_panel10.Layout()
		sbSizer13.Fit( self.m_panel10 )
		bSizer4.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		wSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel12 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		sbSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl_top16a = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer10.Add( self.m_textCtrl_top16a, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_staticText3.Wrap( -1 )

		sbSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl_top16b = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer10.Add( self.m_textCtrl_top16b, 0, wx.ALL, 5 )


		self.m_panel12.SetSizer( sbSizer10 )
		self.m_panel12.Layout()
		sbSizer10.Fit( self.m_panel12 )
		bSizer6.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel13 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,18 ), 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer111.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl_top16c = wx.TextCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer111.Add( self.m_textCtrl_top16c, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,55 ), 0 )
		self.m_staticText5.Wrap( -1 )

		sbSizer111.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl_top16d = wx.TextCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer111.Add( self.m_textCtrl_top16d, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( sbSizer111 )
		self.m_panel13.Layout()
		sbSizer111.Fit( self.m_panel13 )
		bSizer6.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel4.SetSizer( bSizer6 )
		self.m_panel4.Layout()
		bSizer6.Fit( self.m_panel4 )
		wSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel14 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer121 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel14, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( sbSizer121.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,65 ), 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer121.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl_top16ab = wx.TextCtrl( sbSizer121.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer121.Add( self.m_textCtrl_top16ab, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer121.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,160 ), 0 )
		self.m_staticText7.Wrap( -1 )

		sbSizer121.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl_top16cd = wx.TextCtrl( sbSizer121.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer121.Add( self.m_textCtrl_top16cd, 0, wx.ALL, 5 )


		self.m_panel14.SetSizer( sbSizer121 )
		self.m_panel14.Layout()
		sbSizer121.Fit( self.m_panel14 )
		bSizer7.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer7 )
		self.m_panel5.Layout()
		bSizer7.Fit( self.m_panel5 )
		wSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer131 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel16, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( sbSizer131.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,130 ), 0 )
		self.m_staticText8.Wrap( -1 )

		sbSizer131.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_bitmap_top16winner = wx.StaticBitmap( sbSizer131.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,100 ), 0 )
		sbSizer131.Add( self.m_bitmap_top16winner, 0, wx.ALL, 5 )


		self.m_panel16.SetSizer( sbSizer131 )
		self.m_panel16.Layout()
		sbSizer131.Fit( self.m_panel16 )
		bSizer8.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer8 )
		self.m_panel6.Layout()
		bSizer8.Fit( self.m_panel6 )
		wSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel51 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel141 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1211 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel141, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( sbSizer1211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,65 ), 0 )
		self.m_staticText61.Wrap( -1 )

		sbSizer1211.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_textCtrl_top16ef = wx.TextCtrl( sbSizer1211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer1211.Add( self.m_textCtrl_top16ef, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( sbSizer1211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,160 ), 0 )
		self.m_staticText71.Wrap( -1 )

		sbSizer1211.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_textCtrl_top16gh = wx.TextCtrl( sbSizer1211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		sbSizer1211.Add( self.m_textCtrl_top16gh, 0, wx.ALL, 5 )


		self.m_panel141.SetSizer( sbSizer1211 )
		self.m_panel141.Layout()
		sbSizer1211.Fit( self.m_panel141 )
		bSizer71.Add( self.m_panel141, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel51.SetSizer( bSizer71 )
		self.m_panel51.Layout()
		bSizer71.Fit( self.m_panel51 )
		wSizer3.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel41 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel121 = wx.Panel( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer101 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel121, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		sbSizer101.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl_top16e = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer101.Add( self.m_textCtrl_top16e, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_staticText31.Wrap( -1 )

		sbSizer101.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl_top16f = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer101.Add( self.m_textCtrl_top16f, 0, wx.ALL, 5 )


		self.m_panel121.SetSizer( sbSizer101 )
		self.m_panel121.Layout()
		sbSizer101.Fit( self.m_panel121 )
		bSizer61.Add( self.m_panel121, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel131 = wx.Panel( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1111 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel131, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText41 = wx.StaticText( sbSizer1111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,18 ), 0 )
		self.m_staticText41.Wrap( -1 )

		sbSizer1111.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_textCtrl_top16g = wx.TextCtrl( sbSizer1111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer1111.Add( self.m_textCtrl_top16g, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( sbSizer1111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,55 ), 0 )
		self.m_staticText51.Wrap( -1 )

		sbSizer1111.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_textCtrl_top16h = wx.TextCtrl( sbSizer1111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer1111.Add( self.m_textCtrl_top16h, 0, wx.ALL, 5 )


		self.m_panel131.SetSizer( sbSizer1111 )
		self.m_panel131.Layout()
		sbSizer1111.Fit( self.m_panel131 )
		bSizer61.Add( self.m_panel131, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel41.SetSizer( bSizer61 )
		self.m_panel41.Layout()
		bSizer61.Fit( self.m_panel41 )
		wSizer3.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel31 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel71 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel71, wx.ID_ANY, u"        E1 vs E2" ), wx.VERTICAL )

		self.m_textCtrl_top16e1 = wx.TextCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer14.Add( self.m_textCtrl_top16e1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16e2 = wx.TextCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer14.Add( self.m_textCtrl_top16e2, 0, wx.ALL, 5 )


		self.m_panel71.SetSizer( sbSizer14 )
		self.m_panel71.Layout()
		sbSizer14.Fit( self.m_panel71 )
		bSizer41.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel81 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer112 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"        F1 vs F2" ), wx.VERTICAL )

		self.m_textCtrl_top16f1 = wx.TextCtrl( sbSizer112.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer112.Add( self.m_textCtrl_top16f1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16f2 = wx.TextCtrl( sbSizer112.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer112.Add( self.m_textCtrl_top16f2, 0, wx.ALL, 5 )


		self.m_panel81.SetSizer( sbSizer112 )
		self.m_panel81.Layout()
		sbSizer112.Fit( self.m_panel81 )
		bSizer41.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel91 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer122 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel91, wx.ID_ANY, u"        G1 vs G2" ), wx.VERTICAL )

		self.m_textCtrl_top16g1 = wx.TextCtrl( sbSizer122.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer122.Add( self.m_textCtrl_top16g1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16g2 = wx.TextCtrl( sbSizer122.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer122.Add( self.m_textCtrl_top16g2, 0, wx.ALL, 5 )


		self.m_panel91.SetSizer( sbSizer122 )
		self.m_panel91.Layout()
		sbSizer122.Fit( self.m_panel91 )
		bSizer41.Add( self.m_panel91, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel101 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer132 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel101, wx.ID_ANY, u"        H1 vs H2" ), wx.VERTICAL )

		self.m_textCtrl_top16h1 = wx.TextCtrl( sbSizer132.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer132.Add( self.m_textCtrl_top16h1, 0, wx.ALL, 5 )

		self.m_textCtrl_top16h2 = wx.TextCtrl( sbSizer132.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		sbSizer132.Add( self.m_textCtrl_top16h2, 0, wx.ALL, 5 )


		self.m_panel101.SetSizer( sbSizer132 )
		self.m_panel101.Layout()
		sbSizer132.Fit( self.m_panel101 )
		bSizer41.Add( self.m_panel101, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel31.SetSizer( bSizer41 )
		self.m_panel31.Layout()
		bSizer41.Fit( self.m_panel31 )
		wSizer3.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( wSizer3 )
		self.m_panel2.Layout()
		wSizer3.Fit( self.m_panel2 )
		self.m_notebook2.AddPage( self.m_panel2, u"Top 16", False )

		bSizer_knockout.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		wSizer_func.Add( bSizer_knockout, 1, wx.EXPAND, 5 )


		bSizer_win.Add( wSizer_func, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_button_editPlayer.Bind( wx.EVT_BUTTON, self.callbackEditPlayer )
		self.m_button_createKnockout.Bind( wx.EVT_BUTTON, self.callbackCreateKnockout )
		self.m_button_clearKnockout.Bind( wx.EVT_BUTTON, self.callbackClearKnockout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackEditPlayer( self, event ):
		event.Skip()

	def callbackCreateKnockout( self, event ):
		event.Skip()

	def callbackClearKnockout( self, event ):
		event.Skip()


###########################################################################
## Class playerWin
###########################################################################

class playerWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 146,185 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel42 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer9 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_textCtrl_playerId = wx.TextCtrl( self.m_panel42, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl_playerId.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer9.Add( self.m_textCtrl_playerId, 0, wx.ALL, 5 )

		self.m_button_add = wx.Button( self.m_panel42, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer9.Add( self.m_button_add, 0, wx.ALL, 5 )

		self.m_button_remove = wx.Button( self.m_panel42, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer9.Add( self.m_button_remove, 0, wx.ALL, 5 )


		self.m_panel42.SetSizer( wSizer9 )
		self.m_panel42.Layout()
		wSizer9.Fit( self.m_panel42 )
		self.m_notebook4.AddPage( self.m_panel42, u"Player ID", False )

		wSizer6.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( wSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_add.Bind( wx.EVT_BUTTON, self.callbackAdd )
		self.m_button_remove.Bind( wx.EVT_BUTTON, self.callbackRemove )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackAdd( self, event ):
		event.Skip()

	def callbackRemove( self, event ):
		event.Skip()


