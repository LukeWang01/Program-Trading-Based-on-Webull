import datetime
import time

import pandas
import pandas as pd
import logging
import os
import json

from webull import webull

from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo

""" Data saving """


def save_to_csv(stock: str, filename, stock_data_frame: pandas.DataFrame):
    directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_csv(os.path.join(directory, f"{filename}.csv"), index=True)


def save_to_xls(stock: str, filename, stock_data_frame: pandas.DataFrame):
    directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_excel(os.path.join(directory, f"{filename}.csv"), index=True)


def save_to_json(stock: str, filename, stock_data_frame: pandas.DataFrame):
    directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_json(os.path.join(directory, f"{filename}.json"), index=True)


""" 
Set up app running log 
"""


def set_up_app_logging():
    # set up logging
    log_file = os.path.join(os.getcwd(), 'app_running.log')
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def logging_info(message: str):
    set_up_app_logging()
    logging.info(f'>>> {message}')  # write log


def logging_warning(message: str):
    set_up_app_logging()
    logging.warning(f'>>> {message}')  # write log


def logging_error(message: str):
    set_up_app_logging()
    logging.error(f'>>> {message}')  # write log


def logging_critical(message: str):
    set_up_app_logging()
    logging.critical(f'>>> {message}')  # write log


""" Set up trading history/log json file """


def write_trading_log_json(filename: str, trading_data: dict):
    with open(filename, "a") as f:
        f.write(json.dumps(trading_data) + "\n")


""" Downlaod stock history data """


def download_max_history_candles(stock, count='max', save_format='csv', extend_trading=False):
    """
        :param stock: ticker
        :param count: max 1200 for 1d
        :param save_format: 'csv' or 'xls'
        :param extend_trading:
        :return: pandas dataframe
        """

    yh_quoter = Quoter_Yahoo()
    stock = stock.upper()
    response_1h_bar = yh_quoter.get_1h_bar(stock=stock, count=count, extend_trading=extend_trading)
    response_1d_bar = yh_quoter.get_1d_bar(stock=stock, count=count, extend_trading=extend_trading)

    if response_1h_bar and response_1d_bar:
        if save_format == 'csv':
            save_to_csv(stock, f'{stock}_1h', response_1h_bar)
            save_to_csv(stock, f'{stock}_1d', response_1d_bar)
        elif save_format == 'xls':
            save_to_xls(stock, f'{stock}_1h', response_1h_bar)
            save_to_xls(stock, f'{stock}_1h', response_1d_bar)
        elif save_format == 'json':
            save_to_json(stock, f'{stock}_1h', response_1h_bar)
            save_to_json(stock, f'{stock}_1h', response_1d_bar)
    else:
        logging_error('Invalid ticker or interval')


def update_intraday_data(stock):
    # run every weekend
    yh_quoter = Quoter_Yahoo()
    wb_quoter = Quoter_Webull()

    # get 1min bar:
    response_1min_bar = yh_quoter.get_1min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(stock, f'{stock}_1min', response_1min_bar)

    # get 2min bar:
    response_2min_bar = yh_quoter.get_2min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(stock, f'{stock}_2min', response_2min_bar)

    # get 5min bar:
    response_5min_bar = wb_quoter.get_5min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(stock, f'{stock}_5min', response_5min_bar)

    # get 15min bar:
    response_15min_bar = wb_quoter.get_15min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(stock, f'{stock}_15min', response_15min_bar)

    # get 30min bar:
    response_30min_bar = wb_quoter.get_30min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(stock, f'{stock}_30min', response_30min_bar)
    
