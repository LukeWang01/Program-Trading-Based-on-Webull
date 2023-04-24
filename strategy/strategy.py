from webull import webull
import time
import pandas as pd
import numpy as np
import yfinance as yf
from quoter.quoter import Quoter
from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo


class Strategy:
    def __init__(self):
        # define your own strategy name, and indicator
        self.strategy_name = ''
        self.indicator = ''

        # set quoter
        self.wb_quoter = Quoter_Webull()
        self.yh_quoter = Quoter_Yahoo()

    """
    Response time: 
        wb_quoter:  around 300 - 800 ms
        yh_quoter:  around 200 - 400 ms
        
    Intraday:
    < 15 min:   yh_quoter will get more data
    > 15 min:   Quoter_Webull will get more data
    = 1h:       yh_quoter will get more data
    
    >= 1d:      yh_quoter will get more data
    """
    def strategy_decision(self, stock):
        """
        Example strategy, based on RSI, from webull and chatGPT.
        Buy when RSI < 30 and Sell when RSI > 70.
        Only for reference, please build your own strategy based on this file
        :return:
        """
        pass

    def strategy_rules(self):
        pass

    def make_decision_1m(self):
        pass

    def make_decision_5m(self):
        pass

    def make_decision_15m(self):
        pass

    def make_decision_1h(self):
        pass

    def make_decision_1d(self):
        pass

    def check_1m_bar(self):
        pass

    def check_2m_bar(self):
        pass

    def check_5m_bar(self):
        pass

    def check_15m_bar(self):
        pass

    def check_30m_bar(self):
        pass

    def check_1h_bar(self):
        pass

    def check_1d_bar(self):
        pass

    def check_1w_bar(self):
        pass

