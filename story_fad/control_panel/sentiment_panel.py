import wx
from .control_panel import MainControlPanel


class SentimentPanel(wx.Panel):

    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.input = wx.TextCtrl(self)
        self.control = MainControlPanel(self)
        self.sizer.Add(self.input,flag=wx.EXPAND|wx.ALL,border=10,proportion=3)
        self.sizer.Add(self.control,flag=wx.EXPAND|wx.ALL,border=10,proportion=1)
        self.Show()