import wx 
import uistylelang as uis

class ButtonPanel(wx.Panel):

    def __init__(self,root):

        super().__init__(root)
        self.sizer = wx.FlexGridSizer(cols=1,rows=2,gap=(10,10))
        self.sizer.AddGrowableCol(0,proportion=1)
        self.SetSizer(self.sizer)
        self.generate_button = wx.Button(self,label="Generate Base Text")
        self.sizer.Add(self.generate_button,flag=wx.CENTER|wx.BOTTOM | wx.EXPAND,proportion=1,border=10)
        self.evaluate_button = wx.Button(self,label="Evaluate Text")
        self.sizer.Add(self.evaluate_button,flag=wx.CENTER|wx.BOTTOM| wx.EXPAND,proportion=1,border=10)

        self.Show()
    