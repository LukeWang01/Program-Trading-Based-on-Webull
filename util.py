import datetime
import time
import pandas as pd


def save_to_csv(stock, stock_data_frame):
    stock_data_frame.to_csv(f'{stock}.csv', index=True)


def save_xls(stock, stock_data_frame):
    stock_data_frame.to_excel(f'{stock}.xlsx', index=True)

