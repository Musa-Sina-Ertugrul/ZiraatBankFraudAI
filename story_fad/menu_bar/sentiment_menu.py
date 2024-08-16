import wx

class SentimentMenu(wx.Menu):

    def __init__(self):
        super().__init__()
        self.open = wx.MenuItem(self,text="Open",id=wx.ID_NEW)
        self.Append(self.open)

    @property
    def menu_open_id(self):
        return self.open.Id