import wx
from wx.lib.scrolledpanel import ScrolledPanel
from .result_panel import ResultPanel

class TransPanelNames(wx.Panel):

    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.account_from_text = wx.StaticText(self,label="From")
        self.account_to_text = wx.StaticText(self,label="To")
        self.amount_text = wx.StaticText(self,label="Amount")
        self.old_balance_origin_text = wx.StaticText(self,label="Old Balance Origin")
        self.new_balance_origin_text = wx.StaticText(self,label="New Balance Origin")
        self.old_balance_dest_text = wx.StaticText(self,label="Old Balance Dest")
        self.new_balance_dest_text = wx.StaticText(self,label="New Balance Dest")
        self.sizer.Add(self.account_from_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.account_to_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.amount_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.old_balance_origin_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.new_balance_origin_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.old_balance_dest_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.new_balance_dest_text,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.Show()

class TransPanelChoiceTable(wx.Panel):
    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.account_from = wx.TextCtrl(self)
        self.account_to = wx.TextCtrl(self)
        self.amount = wx.TextCtrl(self)
        self.old_balance_origin = wx.TextCtrl(self)
        self.new_balance_origin = wx.TextCtrl(self)
        self.old_balance_dest = wx.TextCtrl(self)
        self.new_balance_dest = wx.TextCtrl(self)
        self.sizer.Add(self.account_from,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.account_to,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.amount,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.old_balance_origin,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.new_balance_origin,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.old_balance_dest,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.new_balance_dest,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.Show()

    @property
    def old_balance_origin_retrieve(self) -> int:
        return int(str(self.old_balance_origin.GetLineText()).strip())
    @property
    def new_balance_origin_retrieve(self) -> int:
        return int(str(self.new_balance_origin.GetLineText()).strip())
    @property
    def old_balance_dest_retrieve(self) -> int:
        return int(str(self.old_balance_dest.GetLineText()).strip())
    @property
    def new_balance_dest_retrieve(self) -> int:
        return int(str(self.new_balance_dest.GetLineText()).strip())
    @property
    def amount_retrieve(self) -> int:
        return int(str(self.amount.GetLineText().strip()))
    @property
    def dest_name(self) -> int:
        return str(self.account_to.GetLineText()).strip()
    @property
    def origin_name(self) -> int:
        return str(self.account_from.GetLineText()).strip()

class TransPanel(wx.Panel):

    def __init__(self,root:"TransFraudPanel",id):
        super().__init__(root)
        self.root = root
        self.id = id
        self.sizer = wx.FlexGridSizer(rows=3,cols=1,gap=(1,1))
        self.SetSizer(self.sizer)
        self.sizer.AddGrowableCol(0,proportion=1)
        self.top_panel = TransPanelNames(self)
        self.bottom_panel = TransPanelChoiceTable(self)
        self.sizer.Add(self.top_panel,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.sizer.Add(self.bottom_panel,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.remove_button = wx.Button(self,label="Remove",id=self.id)
        self.sizer.Add(self.remove_button,flag=wx.ALL|wx.EXPAND,proportion=1,border=1)
        self.Show()

    @property
    def old_balance_origin_retrieve(self) -> int:
        return self.bottom_panel.old_balance_origin_retrieve
    @property
    def new_balance_origin_retrieve(self) -> int:
        return self.new_balance_origin_retrieve
    @property
    def old_balance_dest_retrieve(self) -> int:
        return self.old_balance_dest_retrieve
    @property
    def new_balance_dest_retrieve(self) -> int:
        return self.new_balance_dest_retrieve
    @property
    def amount_retrieve(self) -> int:
        return self.amount_retrieve
    @property
    def dest_name(self) -> int:
        return self.dest_name
    @property
    def origin_name(self) -> int:
        return self.origin_name

    @property
    def id_retrieve(self):
        return self.id

    def remove_self(self,event=None):
        self.Hide()
        self.root.RemoveChild(self)
        self.root.Layout()
        del self.root.trans_dict[self.id]
        del self

class TransFraudPanel(wx.Panel):

    def __init__(self, root):
        super().__init__(root)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.__current_id = 0
        self.trans_dict = {}
        self.add_panel()
        self.add_button = wx.Button(self,label="Add Transaction")
        self.evaluate_button = wx.Button(self,label="Evaluate")
        self.sizer.Add(self.add_button,flag=wx.BOTTOM|wx.EXPAND,border=5)
        self.sizer.Add(self.evaluate_button,flag=wx.BOTTOM|wx.EXPAND,border=5)
        self.Bind(wx.EVT_BUTTON,self.add_panel,self.add_button)
        self.result_panel = ResultPanel(self)
        self.sizer.Add(self.result_panel,flag=wx.BOTTOM|wx.EXPAND,border=5)
        self.FitInside()
        self.Layout()
        self.Show()
        
    
    def add_panel(self,event=None):
        if self.__current_id < 8:
            self.tmp_panel = TransPanel(self,self.__current_id)
            self.sizer.Insert(self.__current_id,self.tmp_panel,flag=wx.TOP|wx.EXPAND,border=1,proportion=0)
            self.trans_dict[self.__current_id] = self.tmp_panel
            self.Bind(wx.EVT_BUTTON,self.tmp_panel.remove_self,self.tmp_panel.remove_button)
            self.Center()
            self.Layout()
            self.__current_id += 1

