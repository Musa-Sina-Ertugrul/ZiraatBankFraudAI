import wx

class AgePanel(wx.Panel):

    def __init__(self,root):

        super().__init__(root)

        self.sizer = wx.FlexGridSizer(rows=2,cols=1,gap=(10,10))
        self.SetSizer(self.sizer)
        self.text = wx.StaticText(self,label="Age")
        self.font = wx.Font(12,family=wx.FONTFAMILY_MODERN,style=wx.FONTSTYLE_ITALIC,weight=wx.FONTWEIGHT_BOLD)
        self.text.SetFont(self.font)
        self.sizer.AddGrowableCol(0,proportion=1)
        self.sizer.Add(self.text,flag=wx.ALL|wx.EXPAND,proportion=1)
        self.input = wx.TextCtrl(self)
        self.sizer.Add(self.input,flag=wx.ALL|wx.EXPAND,proportion=1)
        self.Show()