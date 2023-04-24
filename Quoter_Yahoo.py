from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf
from Quoter import Quoter
from util import *


class Quoter_Yahoo(Quoter):
    def __init__(self):
        super().__init__()
        self.name = "Yahoo Platform"

    """
        Limit:  a maximum of 10 requests per second per user
                2,000 requests per hour per IP (or up to a total of 48,000 requests a day)
                
        Response time: around 200 - 400 ms
        
        Yahoo:
            interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
        interval : str
        return: pandas dataframe
    """
    def get_1min_bar(self, stock, count='max', extend_trading=False):

        data_yf = yf.Ticker(stock).history(period='5d', interval='1m', actions=False, prepost=extend_trading)
