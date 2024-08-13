import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        
        self.InitUI()
        
    def InitUI(self):
        # Main panel
        self.panel = wx.Panel(self)
        
        # Main sizer
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Left side (Text box)
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.main_sizer.Add(self.text_ctrl, proportion=3, flag=wx.EXPAND | wx.ALL, border=5)
        
        # Right side (Scrollable Panel with selectable panels and text input fields)
        self.right_panel = wx.ScrolledWindow(self.panel, style=wx.VSCROLL)
        self.right_panel.SetScrollRate(5, 5)
        self.right_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # First sub-panel (with text input fields)
        self.sub_panel_1 = wx.Panel(self.right_panel)
        self.sub_panel_1_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.text_field_1 = wx.TextCtrl(self.sub_panel_1)
        self.text_field_2 = wx.TextCtrl(self.sub_panel_1)

        self.result_text = wx.StaticText(self.sub_panel_1,label="Result :")
        self.result_font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.result_text.SetFont(self.result_font)
        self.sub_panel_1_sizer.Add(self.result_text,flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        self.sub_panel_1_sizer.Add(wx.StaticText(self.sub_panel_1, label="Name and Surname:"), flag=wx.LEFT | wx.TOP, border=5)
        self.sub_panel_1_sizer.Add(self.text_field_1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
        
        self.sub_panel_1_sizer.Add(wx.StaticText(self.sub_panel_1, label="Occupation:"), flag=wx.LEFT | wx.TOP, border=5)
        self.sub_panel_1_sizer.Add(self.text_field_2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
        
        # Second sub-panel (placeholder for more content)
        
        self.text_field_3 = wx.TextCtrl(self.sub_panel_1)
        self.text_field_4 = wx.TextCtrl(self.sub_panel_1)

        self.sub_panel_1_sizer.Add(wx.StaticText(self.sub_panel_1, label="Occupation Year:"), flag=wx.LEFT | wx.TOP, border=5)
        self.sub_panel_1_sizer.Add(self.text_field_3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

        self.sub_panel_1_sizer.Add(wx.StaticText(self.sub_panel_1, label="Age:"), flag=wx.LEFT | wx.TOP, border=5)
        self.sub_panel_1_sizer.Add(self.text_field_4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
    
        self.sub_panel_1.SetSizer(self.sub_panel_1_sizer)

        # Add sub-panels to the right sizer
        self.right_sizer.Add(self.sub_panel_1, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        
        # Add a "Generate" button at the bottom of the right side
        self.generate_button = wx.Button(self.right_panel, label="Generate")
        self.right_sizer.Add(self.generate_button, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.eval_button = wx.Button(self.right_panel, label="Evaluate")
        self.right_sizer.Add(self.eval_button, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        
        self.right_panel.SetSizer(self.right_sizer)
        
        # Add the right panel to the main sizer
        self.main_sizer.Add(self.right_panel, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        
        # Set the sizer for the main panel
        self.panel.SetSizer(self.main_sizer)
        
        self.SetTitle('wxWidgets App Example')
        self.Centre()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
