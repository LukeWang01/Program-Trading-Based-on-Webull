import datetime

from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo
from utils.dataIO import save_to_csv, save_to_xls, save_to_json, logging_error

""" 
Download stock history data:

1. Define stock list below, type the tickers you want to download
2. Run this script
3. Data will be saved in ../data/ticker_name/

OR, you can modify the functions to save whatever you want.

Note: 
    1min, 2min, 1h, 1d data are from Yahoo, 5min, 15min, 30min data are from Webull.
    Download max history data by default, it may take about 2 minutes, please be patient.

"""


stock_lst = ['qqq', 'tqqq', 'sqqq', 'soxx', 'soxl', 'soxs', 'spy', 'spxl', 'spxs', 'aapl', 'tsla', 'tsll', 'spx', 'ndx']


yh_quoter = Quoter_Yahoo()
wb_quoter = Quoter_Webull()


def update_intraday_data_history(stock):
    # run every weekend

    stock = stock.upper()
    current_date = datetime.datetime.today().strftime('%Y%m%d')

    save_dir = f'../data/{stock}/intraday/'

    # get 1min bar: yahoo quoter has more data
    response_1min_bar = yh_quoter.get_1min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_1min', response_1min_bar)
    print(f'{stock}_{current_date}_1min, done')

    # get 2min bar: yahoo quoter has more data
    response_2min_bar = yh_quoter.get_2min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_2min', response_2min_bar)
    print(f'{stock}_{current_date}_2min, done')

    # get 5min bar: webull quoter has more data
    response_5min_bar = wb_quoter.get_5min_bar(stock=stock, count='max', extend_trading=True)
    response_5min_bar = response_5min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                          'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_5min', response_5min_bar)
    print(f'{stock}_{current_date}_5min, done')

    # get 15min bar: webull quoter has more data
    response_15min_bar = wb_quoter.get_15min_bar(stock=stock, count='max', extend_trading=True)
    response_15min_bar = response_15min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                            'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_15min', response_15min_bar)
    print(f'{stock}_{current_date}_15min, done')

    # get 30min bar: webull quoter has more data
    response_30min_bar = wb_quoter.get_30min_bar(stock=stock, count='max', extend_trading=True)
    response_30min_bar = response_30min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                            'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_30min', response_30min_bar)
    print(f'{stock}_{current_date}_30min, done')

    # get 1h bar: yahoo quoter has more data
    response_1h_bar = yh_quoter.get_1h_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_1h', response_1h_bar)
    print(f'{stock}_{current_date}_1h, done')


for s in stock_lst:
    update_intraday_data_history(s)
    print(s)

