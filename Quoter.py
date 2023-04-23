from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf


class Quoter:
    def __init__(self):
        self.name = ""

    def download_history_candles(self, stock, interval='1d', count='max'):
        """
        :param stock: ticker
        :param interval: candle interval
        :param count: max 1200 for 1d
        :return: pandas dataframe
        """
        pass

    def get_current_quote(self, stock):
        pass

    """
        interval : str
            Yahoo:
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            Webull:
                Valid intervals: m1, m5, m15, m30, h1, h2, h4, d1, w1
    """

    def get_1min_bar(self, stock, count='max'):
        pass

    def get_2min_bar(self, stock, count='max'):
        pass

    def get_3min_bar(self, stock, count='max'):
        pass

    def get_5min_bar(self, stock, count='max'):
        pass

    def get_15min_bar(self, stock, count='max'):
        pass

    def get_30min_bar(self, stock, count='max'):
        pass

    def get_1h_bar(self, stock, count='max'):
        pass

    def get_2h_bar(self, stock, count='max'):
        pass

    def get_4h_bar(self, stock, count='max'):
        pass

    def get_1d_bar(self, stock, count='max'):
        pass

    def get_1w_bar(self, stock, count='max'):
        pass





