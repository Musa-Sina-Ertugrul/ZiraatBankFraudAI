import wx
import wx.grid
from .button_panel import ButtonPanel
from .control_panel import MainControlPanel

class EntityControlPanel(wx.Panel):

    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.control_panel = MainControlPanel(self)
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(numCols=2,numRows=10)
        self.sizer.Add(self.grid,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.sizer.Add(self.control_panel,proportion=1,flag=wx.BOTTOM|wx.EXPAND,border=10)
        self.Show()

class EntityPanel(wx.Panel):

    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.input = wx.TextCtrl(self)
        self.sizer.Add(self.input,proportion=3,flag=wx.ALL|wx.EXPAND,border=10)
        self.entity_control_panel = EntityControlPanel(self)
        self.sizer.Add(self.entity_control_panel,proportion=1,flag=wx.RIGHT|wx.EXPAND,border=10)
        self.Show()
    



