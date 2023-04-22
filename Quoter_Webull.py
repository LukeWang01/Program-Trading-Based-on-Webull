from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf
from webull_api.Quoter import Quoter


class Quoter_Webull(Quoter):
    def __init__(self):
        super().__init__()
        self.name = "Webull Platform"

    def get_current_quote(self, stock):
        pass

