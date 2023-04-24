import datetime
import time
import pandas as pd
import logging
import os
import json

""" Data saving """


def save_to_csv(stock, stock_data_frame):
    stock_data_frame.to_csv(f'{stock}.csv', index=True)


def save_to_xls(stock, stock_data_frame):
    stock_data_frame.to_excel(f'{stock}.xlsx', index=True)


""" 
Set up app running log 
"""


def set_up_app_logging():
    # set up logging
    log_file = os.path.join(os.getcwd(), 'app_running.log')
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def logging_info(message):
    set_up_app_logging()
    logging.info(f'>>> {message}')  # write log


def logging_warning(message):
    set_up_app_logging()
    logging.warning(f'>>> {message}')  # write log


def logging_error(message):
    set_up_app_logging()
    logging.error(f'>>> {message}')  # write log


def logging_critical(message):
    set_up_app_logging()
    logging.critical(f'>>> {message}')  # write log


""" Set up trading history json file """


def write_trading_history(trading_data):
    with open("trading_history.json", "a") as f:
        f.write(json.dumps(trading_data) + "\n")
