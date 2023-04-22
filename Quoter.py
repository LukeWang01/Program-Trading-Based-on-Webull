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

    def get_1min_bar(self, stock, count='max'):
        pass

    def get_5min_bar(self):
        pass
