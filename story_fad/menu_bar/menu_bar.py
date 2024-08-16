import wx
from enum import Enum
from .entity_sentiment_menu import EntitySentimentMenu
from .fraud_menu import FraudMenu
from .sentiment_menu import SentimentMenu


class MenuBar(wx.MenuBar):

    def __init__(self):

        super().__init__()
        self.entity_sentiment_menu = EntitySentimentMenu()
        self.Append(self.entity_sentiment_menu,"Entity Sentiment")
        self.fraud_menu = FraudMenu()
        self.Append(self.fraud_menu,"Fraud Detection")
        self.sentiment_menu = SentimentMenu()
        self.Append(self.sentiment_menu,"Sentiment Detection")
        self.Show()