import datetime
import time

import pandas
import pandas as pd
import logging
import os
import json

""" Data saving """


def save_to_csv(stock: str, stock_data_frame: pandas.DataFrame):
    stock_data_frame.to_csv(f'{stock}.csv', index=True)


def save_to_xls(stock: str, stock_data_frame: pandas.DataFrame):
    stock_data_frame.to_excel(f'{stock}.xlsx', index=True)


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


""" Set up trading history json file """


def write_data_to_json(filename: str, trading_data: dict):
    with open(filename, "a") as f:
        f.write(json.dumps(trading_data) + "\n")
