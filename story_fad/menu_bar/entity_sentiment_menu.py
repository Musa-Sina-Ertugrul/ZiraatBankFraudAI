import wx
class EntitySentimentMenu(wx.Menu):
    
    def __init__(self):
        super().__init__()
        self.open = wx.MenuItem(self,id=wx.ID_NEW,text="Open",helpString="Opens Entity Sentiment Analysis Tool")
        self.Append(self.open)
        
    @property
    def menu_item_id(self):
        return self.open.Id
