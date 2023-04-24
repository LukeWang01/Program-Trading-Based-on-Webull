from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf
from utils.util import *


class Quoter:
    def __init__(self):
        self.name = ""
        self.quoter_wb = webull()

    """

                Yahoo:
                    Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                    Intraday data cannot extend last 60 days
                Webull:
                    Valid intervals: m1, m5, m15, m30, d1;  (h1, h2, h4, w1 are currently not working)
                    max_count:
                        m1:     1200
                        m5:     1200
                        m15:    1200
                        m30:    1049
                        d1:     1200
                    interval : str
                    quote returns a pandas dataframe
        """

    def download_history_candles(self, stock, interval='1d', count='max', format='csv'):
        """
        :param stock: ticker
        :param interval: candle interval
        :param count: max 1200 for 1d
        :param format: 'csv' or 'xls'
        :return: pandas dataframe
        """
        if interval in ['2m', '5m', '15m', '30m']:
            cnt = 1200 if count == 'max' else count
            if interval == '30m':
                cnt = 1049
            interval = interval[::-1]
            response = self.quoter_wb.get_bars(stock, interval=interval, count=cnt, extendTrading=1)

        elif interval in ['1d', '5d', '1wk', '1mo', '3mo']:
            response = yf.Ticker(stock).history(period='10y', interval=interval, actions=False)
        else:
            response = False
        if not response:
            if format == 'csv':
                save_to_csv(stock, response)
            elif format == 'xls':
                save_to_xls(stock, response)
        else:
            logging_error('Invalid ticker or interval')

    def get_current_quote(self, stock):
        pass

    def get_1min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_3min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_5min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_15min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_30min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_4h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1d_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1w_bar(self, stock, count='max', extend_trading=False):
        pass
