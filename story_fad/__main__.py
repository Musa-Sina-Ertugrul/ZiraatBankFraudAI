import wx
from control_panel import MainControlPanel,EntityPanel,SentimentPanel,TransFraudPanel
from menu_bar import MenuBar

class FraudPanel(wx.Panel):

    def __init__(self,root):
        super().__init__(root)
        self.fraud_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.fraud_sizer)
        self.fraud_control_panel = MainControlPanel(self)
        self.fraud_text = wx.TextCtrl(self)
        self.fraud_sizer.Add(self.fraud_text,proportion=3,flag=wx.ALL|wx.EXPAND,border=10)
        self.fraud_sizer.Add(self.fraud_control_panel,proportion=1,flag=wx.ALL|wx.EXPAND,border=10)

class MainFrame(wx.Frame):

    def __init__(self):

        super().__init__(parent=None,title="FradAI")
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.entity_sentiment_panel = EntityPanel(self)
        self.fraud_panel = FraudPanel(self)
        self.sentiment_panel = SentimentPanel(self)
        self.trans_fraud_panel = TransFraudPanel(self)
        self.sizer.Add(self.sentiment_panel,1,wx.EXPAND)
        self.sizer.Add(self.entity_sentiment_panel, 1, wx.EXPAND)
        self.sizer.Add(self.fraud_panel, 1, wx.EXPAND)
        self.sizer.Add(self.trans_fraud_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.menu_bar = MenuBar()
        self.SetMenuBar(self.menu_bar)
        self.entity_sentiment_panel.Hide()
        self.sentiment_panel.Hide()
        self.trans_fraud_panel.Hide()
        self.fraud_panel.Show()
        self.menu_bar.fraud_menu.Bind(wx.EVT_MENU, self.change_panel_to_fraud)
        self.menu_bar.entity_sentiment_menu.Bind(wx.EVT_MENU, self.change_panel_to_entity_sent)
        self.menu_bar.sentiment_menu.Bind(wx.EVT_MENU,self.change_panel_to_sent)
        self.menu_bar.trans_fraud_menu.Bind(wx.EVT_MENU,self.change_panel_to_trans_fraud)
        self.Layout()
        self.Show()
    
    def change_panel_to_fraud(self,event):
        if not self.fraud_panel.IsShown():
            self.trans_fraud_panel.Hide()
            self.entity_sentiment_panel.Hide()
            self.sentiment_panel.Hide()
            self.fraud_panel.Show()
        self.Layout()

    def change_panel_to_entity_sent(self,event):
        if not self.entity_sentiment_panel.IsShown():
            self.trans_fraud_panel.Hide()
            self.fraud_panel.Hide()
            self.sentiment_panel.Hide()
            self.entity_sentiment_panel.Show()
        self.Layout()

    def change_panel_to_sent(self,event):
        if not self.sentiment_panel.IsShown():
            self.trans_fraud_panel.Hide()
            self.fraud_panel.Hide()
            self.entity_sentiment_panel.Hide()
            self.sentiment_panel.Show()
        self.Layout()

    def change_panel_to_trans_fraud(self,event):
        if not self.trans_fraud_panel.IsShown():
            self.fraud_panel.Hide()
            self.entity_sentiment_panel.Hide()
            self.sentiment_panel.Hide()
            self.trans_fraud_panel.Show()
        self.Layout()
    

if __name__ == '__main__':
    app = wx.App()
    main_frame = MainFrame()
    app.MainLoop()
