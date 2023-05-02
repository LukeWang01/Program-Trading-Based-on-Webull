import datetime

from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo
from utils.dataIO import save_to_csv, save_to_xls, save_to_json, logging_error

""" Download stock history data """
yh_quoter = Quoter_Yahoo()
wb_quoter = Quoter_Webull()


def download_max_history_candles(stock, count='max', save_format='csv'):
    """
        :param stock: ticker
        :param count: max 1200 for 1d
        :param save_format: 'csv' or 'xls'
        :return: pandas dataframe
        """

    stock = stock.upper()
    response_1h_bar = yh_quoter.get_1h_bar(stock=stock, count=count, extend_trading=True)
    response_1d_bar = yh_quoter.get_1d_bar(stock=stock, count=count, extend_trading=False)

    save_dir = f'../data/{stock}/'

    if response_1h_bar.empty or response_1d_bar.empty:
        logging_error('Invalid ticker or interval')
    else:
        if save_format == 'csv':
            save_to_csv(save_dir, f'{stock}_1h', response_1h_bar)
            save_to_csv(save_dir, f'{stock}_1d', response_1d_bar)
        elif save_format == 'xls':
            save_to_xls(save_dir, f'{stock}_1h', response_1h_bar)
            save_to_xls(save_dir, f'{stock}_1h', response_1d_bar)
        elif save_format == 'json':
            save_to_json(save_dir, f'{stock}_1h', response_1h_bar)
            save_to_json(save_dir, f'{stock}_1h', response_1d_bar)


def update_intraday_data_history(stock):
    # run every weekend

    stock = stock.upper()
    current_date = datetime.datetime.today().strftime('%Y%m%d')

    save_dir = f'../data/{stock}/intraday/'

    # get 1min bar: yahoo quoter has more data
    response_1min_bar = yh_quoter.get_1min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_1min', response_1min_bar)
    print(f'{stock}_{current_date}_1min')

    # get 2min bar: yahoo quoter has more data
    response_2min_bar = yh_quoter.get_2min_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_2min', response_2min_bar)
    print(f'{stock}_{current_date}_2min')

    # get 5min bar: webull quoter has more data
    response_5min_bar = wb_quoter.get_5min_bar(stock=stock, count='max', extend_trading=True)
    response_5min_bar = response_5min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                          'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_5min', response_5min_bar)
    print(f'{stock}_{current_date}_5min')

    # get 15min bar: webull quoter has more data
    response_15min_bar = wb_quoter.get_15min_bar(stock=stock, count='max', extend_trading=True)
    response_15min_bar = response_15min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                            'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_15min', response_15min_bar)
    print(f'{stock}_{current_date}_15min')

    # get 30min bar: webull quoter has more data
    response_30min_bar = wb_quoter.get_30min_bar(stock=stock, count='max', extend_trading=True)
    response_30min_bar = response_30min_bar.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low',
                                                            'close': 'Close', 'volume': 'Volume', 'vwap': 'VWAP'})
    save_to_csv(save_dir, f'{stock}_{current_date}_30min', response_30min_bar)
    print(f'{stock}_{current_date}_30min')

    # get 1h bar: yahoo quoter has more data
    response_1h_bar = yh_quoter.get_1h_bar(stock=stock, count='max', extend_trading=True)
    save_to_csv(save_dir, f'{stock}_{current_date}_1h', response_1h_bar)
    print(f'{stock}_{current_date}_1h')


# define stock list here:
stock_lst = ['qqq', 'tqqq', 'sqqq', 'soxx', 'soxl', 'soxs', 'spy', 'spxl', 'spxs', 'aapl', 'tsla', 'tsll', 'spx', 'ndx']

for stock in stock_lst:
    update_intraday_data_history(stock)
    download_max_history_candles(stock)
    print(stock)
