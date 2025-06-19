# This file defines the Quoter class, which is the base class for all quoters.
import yfinance as yf


def get_market_index_real_time_price():
    symbols = ["^IXIC", "^GSPC", "^DJI"]  # Nasdaq, S&P500, Dow Jones

    indices = yf.Tickers(symbols)
    latest_prices = {}

    for symbol in symbols:
        index = indices.tickers[symbol]
        latest_data = index.history(period="1d")

        if not latest_data.empty:
            latest_price = latest_data["Close"].iloc[-1]
            latest_prices[symbol] = latest_price
        else:
            latest_prices[symbol] = None

    return latest_prices


class Quoter:
    def __init__(self):
        self.name = "Quoter"

    def get_current_quote(self, stock):
        pass

    def get_1min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_3min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_5min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_15min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_30min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_4h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1d_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1w_bar(self, stock, count='max', extend_trading=False):
        pass
