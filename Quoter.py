from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf


class Quoter:
    def __init__(self):
        self.name = ""
        self.webull_quote = webull
        self.yf_quote = yf.Ticker

    def get_latest_quote(self, stock, interval="5min", counts=1):
        pass

    def get_1min_bar(self):
        pass

