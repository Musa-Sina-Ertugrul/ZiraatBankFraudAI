import wx

class NamePanel(wx.Panel):

    def __init__(self,root):

        super().__init__(root)
        self.sizer=wx.FlexGridSizer(gap=(10,10),rows=2,cols=1)
        self.font = wx.Font(12,family=wx.FONTFAMILY_MODERN,style=wx.FONTSTYLE_ITALIC,weight=wx.FONTWEIGHT_BOLD)
        self.text = wx.StaticText(self,label="Name and Surname")
        self.text.SetFont(self.font)
        self.input = wx.TextCtrl(self)
        self.SetSizer(self.sizer)
        self.sizer.Add(self.text,flag=wx.ALL|wx.EXPAND,proportion=1)
        self.sizer.Add(self.input,flag=wx.ALL|wx.EXPAND,proportion=1)
        self.sizer.AddGrowableCol(0,proportion=1)
        self.Show()