import pandas
import logging
import os
import json

""" 
Data I/O: 
"""


# Set up pandas data output:
def save_to_csv(directory: str, filename, stock_data_frame: pandas.DataFrame):
    # directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_csv(os.path.join(directory, f"{filename}.csv"), index=True)


def save_to_xls(directory: str, filename, stock_data_frame: pandas.DataFrame):
    # directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_excel(os.path.join(directory, f"{filename}.csv"), index=True)


def save_to_json(directory: str, filename, stock_data_frame: pandas.DataFrame):
    # directory = f"../data/{stock}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    stock_data_frame.to_json(os.path.join(directory, f"{filename}.json"), index=True)


# Set up app running log
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


# Write trading history/log json file
def write_trading_log_json(filename: str, trading_data: dict):
    with open(filename, "a") as f:
        f.write(json.dumps(trading_data) + "\n")
