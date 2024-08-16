import wx

class ResultPanel(wx.Panel):

    def __init__(self,root):

        super().__init__(root)
        self.sizer = wx.FlexGridSizer(cols=1,rows=1,gap=(10,10))
        self.sizer.AddGrowableCol(0,proportion=1)
        self.font = wx.Font(12,family=wx.FONTFAMILY_MODERN,style=wx.FONTSTYLE_ITALIC,weight=wx.FONTWEIGHT_BOLD)
        self.output = wx.StaticText(self,label="Result : ")
        self.SetSizer(self.sizer)
        self.output.SetFont(self.font)
        self.sizer.Add(self.output,proportion=1,flag=wx.TOP|wx.EXPAND,border=10)
        self.Show()

    @property
    def text(self):
        return self.output.GetLabelText()
    
    @text.setter
    def text(self,input:str):
        self.output.SetLabelText("Result : " + input)
