
from Quoter import Quoter


class Quoter_Yahoo(Quoter):
    def __init__(self):
        super().__init__()
        self.name = "Yahoo Platform"

    """
    interval : str
                    Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                    Intraday data cannot extend last 60 days
    """
    def get_current_quote(self, stock):
        pass
