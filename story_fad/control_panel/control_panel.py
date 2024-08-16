import wx
from .name_panel import NamePanel
from .occupation_panel import OccupationPanel
from .age_panel import AgePanel
from .button_panel import ButtonPanel
from .result_panel import ResultPanel

class MainControlPanel(wx.Panel):
    
    def __init__(self,root):

        super().__init__(root)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.name_panel = NamePanel(self)
        self.occupation_panel = OccupationPanel(self)
        self.age_panel = AgePanel(self)
        self.button_panel = ButtonPanel(self)
        self.result_panel = ResultPanel(self)
        self.SetSizer(self.sizer)
        self.sizer.Add(self.name_panel,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.sizer.Add(self.occupation_panel,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.sizer.Add(self.age_panel,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.sizer.Add(self.result_panel,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.sizer.AddStretchSpacer(prop=25)
        self.sizer.Add(self.button_panel,proportion=1,flag=wx.BOTTOM|wx.EXPAND)
        self.Show()