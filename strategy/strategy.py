from webull import webull
import time
import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta as pta
from quoter.quoter import Quoter
from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo
from utils.util import write_trading_log_json


class Strategy:
    def __init__(self, indicator='rsi', quoter='yahoo'):
        # define your own strategy name, and indicator
        self.strategy_name = 'example_strategy'
        self.indicator = indicator
        self.trading_log_filename = 'trade_history'

        # set market data quoter
        # default is yh_quoter, fast and stable
        self.yh_quoter = None
        self.wb_quoter = None
        if quoter == 'yahoo':
            self.yh_quoter = Quoter_Yahoo()
        elif quoter == 'webull':
            self.wb_quoter = Quoter_Webull()

        # set portfolio:
        # create trading strategy initialization attributes
        self.init_asset = 1000000
        self.init_cash = 1000000
        self.init_stock = ''
        self.init_portfolio = {'cash': self.init_cash, 'stock': self.init_stock, 'asset': self.init_asset}

        # set oder history
        self.order_history = []
        self.current_order = {}

        # create trading strategy attributes
        self.cash = self.init_cash
        self.stock = self.init_stock
        self.asset = self.init_asset
        self.portfolio = {'cash': self.cash, 'stock': self.stock, 'asset': self.asset}

        # create trading strategy parameters
        self.buy = False
        self.sell = False
        self.hold = False
        self.buy_price = 0
        self.sell_price = 0
        self.hold_price = 0

        # create trading strategy indicators, default is 0, you can define your own indicators
        self.ema = 0
        self.sma = 0
        self.adx = 0
        self.obv = 0
        self.bbands = 0
        self.aroon = 0
        self.atr = 0
        self.cci = 0
        self.cmo = 0
        self.coppock = 0
        self.dpo = 0
        self.dmi = 0
        self.ichimoku = 0
        self.kst = 0
        self.macd = 0
        self.mfi = 0
        self.mom = 0
        self.pivots = 0
        self.ppo = 0
        self.psl = 0
        self.roc = 0
        self.rsi = 0
        self.rvi = 0
        self.stoch = 0
        self.tsi = 0
        self.uo = 0
        self.willr = 0
        self.vwap = 0
        self.vwma = 0
        self.vwmacd = 0
        self.zlema = 0


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

    def update(self):
        pass

    def strategy_input(self, stock, interval_level, stock_data=None):
        pass

    def strategy_output(self):
        # output a dict of decision
        pass

    def strategy_decision(self, stock):
        """
        Example strategy, based on RSI, from Webull and chatGPT.
        Buy when RSI < 30 and Sell when RSI > 70.
        Only for reference, please build your own strategy based on this file
        :return:
        """
        # get stock data
        stock_data = self.yh_quoter.get_1min_bar(stock=stock, count=100)
        # stock_data = self.wb_quoter.get_1min_bar(stock=stock, count=100)

        # calculate RSI
        self.rsi = pta.rsi(stock_data['close'], length=14)

        # make decision
        if stock_data['rsi'].iloc[-1] < 30:
            # buy
            pass
        elif stock_data['rsi'].iloc[-1] > 70:
            # sell
            pass
        else:
            # hold
            pass
        pass

    def save_current_order(self, datetime, order_id, action, order_type, stock, price, order_quantity, amount, status):

        self.current_order = {'datetime': datetime, 'order_id': order_id, 'action': action, 'order_type': order_type,
                                'stock': stock, 'price': price, 'order_quantity': order_quantity, 'amount': amount,
                                'status': status, 'strategy': self.strategy_name}
        self.order_history.append(self.current_order)
        write_trading_log_json(f"{self.trading_log_filename}.json", self.current_order)

    def strategy_rules(self, stock):
        pass

    def make_decision_1m(self, stock):
        pass

    def make_decision_5m(self, stock):
        pass

    def make_decision_15m(self, stock):
        pass

    def make_decision_1h(self, stock):
        self.calculate_rsi(self.check_1h_bar(stock=stock))

    def make_decision_1d(self, stock):
        pass

    def check_1m_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_1min_bar(stock=stock, count='max', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_1min_bar(stock=stock, count='max', extend_trading=False)

    def check_2m_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_2min_bar(stock=stock, count='max', extend_trading=False)
        elif self.wb_quoter:
            # no 1 hour bar for webull
            return None

    def check_5m_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_5min_bar(stock=stock, count='max', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_5min_bar(stock=stock, count='max', extend_trading=False)

    def check_15m_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_15min_bar(stock=stock, count='max', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_15min_bar(stock=stock, count='max', extend_trading=False)

    def check_30m_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_30min_bar(stock=stock, count='max', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_30min_bar(stock=stock, count='max', extend_trading=False)

    def check_1h_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_1h_bar(stock=stock, count='1y', extend_trading=False)
        elif self.wb_quoter:
            # no 1 hour bar from webull
            return None

    def check_1d_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_1d_bar(stock=stock, count='1y', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_1d_bar(stock=stock, count='max', extend_trading=False)

    def check_1w_bar(self, stock):
        if self.yh_quoter:
            return self.yh_quoter.get_1w_bar(stock=stock, count='1y', extend_trading=False)
        elif self.wb_quoter:
            return self.wb_quoter.get_1w_bar(stock=stock, count='max', extend_trading=False)

    def calculate_rsi(self, stock_data: pd.DataFrame):
        if self.yh_quoter:
            return pta.rsi(stock_data['Close'], length=14)
        elif self.wb_quoter:
            return pta.rsi(stock_data['close'], length=14)
        else:
            return None


