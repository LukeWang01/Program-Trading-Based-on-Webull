import time
import pandas as pd
import numpy as np
import pandas_ta as pta

from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo
from strategy.strategy import Strategy
from utils.dataIO import write_trading_log_json


""" Define your own strategy here """


class Your_Strategy(Strategy):
    def __init__(self):
        super().__init__()

    def update(self):
        tmp = self.wb_quoter

