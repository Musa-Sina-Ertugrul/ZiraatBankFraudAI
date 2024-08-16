import wx
import pandas as pd
import numpy as np

class OccupationPanel(wx.Panel):

    def __init__(self,root):

        super().__init__(root)
        self.sizer= wx.FlexGridSizer(rows=5,cols=1,gap=(10,10))
        self.sizer.AddGrowableCol(0,proportion=1)
        self.SetSizer(self.sizer)
        self.font = wx.Font(12,family=wx.FONTFAMILY_MODERN,style=wx.FONTSTYLE_ITALIC,weight=wx.FONTWEIGHT_BOLD)
        self.occupation_text = wx.StaticText(self,label="Occupation")
        self.occupation_text.SetFont(self.font)
        self.sizer.Add(self.occupation_text,flag=wx.EXPAND|wx.ALL,proportion=1)
        self.job_list = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/job_list.csv")["names"].convert_dtypes(convert_string=True).to_list()
        self.occupation_menu = wx.Choice(self,choices = list(set(self.job_list)))
        self.sizer.Add(self.occupation_menu,flag=wx.EXPAND|wx.ALL,proportion=1)
        self.occupation_year_text = wx.StaticText(self,label="Occupation Year")
        self.occupation_year_text.SetFont(self.font)
        self.sizer.Add(self.occupation_year_text,flag=wx.EXPAND|wx.ALL,proportion=1)
        self.occupation_year_input = wx.TextCtrl(self)
        self.sizer.Add(self.occupation_year_input,flag=wx.EXPAND|wx.ALL,proportion=1)
        self.Show()
