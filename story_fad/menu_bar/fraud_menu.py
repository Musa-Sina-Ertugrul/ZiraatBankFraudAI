import wx

class FraudMenu(wx.Menu):
    
    def __init__(self):
        super().__init__()
        self.open = wx.MenuItem(self,id=wx.ID_NEW,text="Open",helpString="Opens Fraud Analysis Tool")
        self.Append(self.open)

    @property
    def menu_open_id(self):
        return self.open.Id