import time
import pandas as pd
import numpy as np
import pandas_ta as pta
import schedule

from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo
from utils.dataIO import write_trading_log_json, get_current_time, logging_info
from utils.send_email import send_emails


class Strategy:
    """
    Class Name must be the same as the file name
    """
    def __init__(self, quoter='yahoo'):
        # define your own strategy name, and indicator
        self.strategy_name = 'strategy template class'
        self.strategy_actions_history = 'strategy_actions_history'
        self.parent = None  # parent is the main program, app.py

        # set market data quoter
        # default is yh_quoter, fast and stable
        self.quoter = None
        if quoter == 'yahoo':
            self.quoter = Quoter_Yahoo()
        elif quoter == 'webull':
            self.quoter = Quoter_Webull()

        self.cash_balance = 0
        self.market_value = 0
        self.dayBuyingPower = 0
        self.overnightBuyingPower = 0
        self.net_account_value = 0

        # schedule the strategy to run
        # self.strategy_scheduler()
        self.strategy_load_notification()

    """
    Response time: 
        wb_quoter:  around 300 - 800 ms
        yh_quoter:  around 50 - 400 ms (fairly stable)
        
    Intraday (exclude pre-market and after-market):
    < 15 min:   yh_quoter will get more data
    > 15 min:   Quoter_Webull will get more data
    = 1h:       yh_quoter will get more data
    >= 1d:      yh_quoter will get more data
    
    Intraday (include pre-market and after-market):
    < 15 min:   yh_quoter will get more data
    > 15 min:   yh_quoter will get more data
    = 1h:       yh_quoter will get more data
    >= 1d:      yh_quoter will get more data
    
    """

    # ******
    # Functions below need to overwrite in your own strategy class
    def strategy_decision(self):
        pass

    # ******
    # Functions below do not need to be modified, free to check and call
    def strategy_load_notification(self):
        logging_info(f"Strategy: {self.strategy_name} Status: Initialized")

    def save_strategy_actions(self, action_res):
        if action_res:
            write_trading_log_json('trader/trading_actions.json', action_res)

    def update_strategy_profile(self):
        # after placing order, update the strategy profile
        # you can define attributes depends on your strategy
        self.parent.trader.update_account_info()
        self.cash_balance = self.parent.trader.cash_balance
        self.market_value = self.parent.trader.market_value
        self.dayBuyingPower = self.parent.trader.dayBuyingPower
        self.overnightBuyingPower = self.parent.trader.overnightBuyingPower
        self.net_account_value = self.parent.trader.net_account_value

    def send_notification(self, action_res):
        # send_emails(from_, to, bcc: list, msg_subject, msg_body, login_email, login_password):
        # set the email and password in the app GUI

        # 1. send via email
        if self.parent.enable_email_notify and self.parent.is_email_setup():
            from_ = self.parent.sender_email
            to = self.parent.receiver_email_1
            bcc = self.parent.receiver_email_2_bcc.split(' ')
            msg_subject = f"Strategy: {self.strategy_name}, Action made for {action_res['stock_info']}"

            msg_body = ''
            for key, value in action_res.items():
                msg_body += f"{key}: {value} \n"

            login_email = self.parent.sender_email
            login_password = self.parent.sender_password
            send_emails(from_, to, bcc, msg_subject, msg_body, login_email, login_password)

            # save the email to txt file in local as well
            msg_to_txt = f'{get_current_time()}\n' \
                         f'From: {from_}\n' \
                         f'To: {to}\n' \
                         f'Subject: {msg_subject}\n\n' \
                         f'{msg_body}\n\n'
            self.write_message_to_txt(msg_to_txt)
            logging_info(f"Strategy: {self.strategy_name} Status: Email sent")

        # 2. send via discord bot
        # TODO: add discord bot notification
        # please refer to discord_bot folder for more details

    def write_message_to_txt(self, msg):
        with open('message_list.txt', 'a') as file:
            file.write(msg)
        self.parent.frames['Message'].update_message_list()

    def update_quoter_stream(self, info):
        self.parent.frames['StrategyMonitor'].set_quoter_stream(info)

    def update_strategy_stream(self, info):
        if info != '':
            dict_str = "\n".join([f"{key}: {value}" for key, value in info.items()])
            self.parent.frames['StrategyMonitor'].set_strategy_stream(dict_str)

    def get_current_position(self):
        return self.parent.trader._webull.get_account()['positions']

    def check_1m_bar(self, stock):
        if self.quoter:
            return self.quoter.get_1min_bar(stock=stock, count='max', extend_trading=False)

    def check_2m_bar(self, stock):
        if self.quoter:
            return self.quoter.get_2min_bar(stock=stock, count='max', extend_trading=False)

    def check_5m_bar(self, stock):
        if self.quoter:
            return self.quoter.get_5min_bar(stock=stock, count='max', extend_trading=False)

    def check_15m_bar(self, stock):
        if self.quoter:
            return self.quoter.get_15min_bar(stock=stock, count='max', extend_trading=False)

    def check_30m_bar(self, stock):
        if self.quoter:
            return self.quoter.get_30min_bar(stock=stock, count='max', extend_trading=False)

    def check_1h_bar(self, stock):
        if self.quoter:
            return self.quoter.get_1h_bar(stock=stock, count='1y', extend_trading=False)

    def check_1d_bar(self, stock):
        if self.quoter:
            return self.quoter.get_1d_bar(stock=stock, count='1y', extend_trading=False)

    def check_1w_bar(self, stock):
        if self.quoter:
            return self.quoter.get_1w_bar(stock=stock, count='1y', extend_trading=False)
