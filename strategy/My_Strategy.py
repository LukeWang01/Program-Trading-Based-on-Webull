from strategy.Strategy import Strategy
import talib
from utils import play_sound
from utils.dataIO import is_market_hours


class My_Strategy(Strategy):
    """
    Class Name must be the same as the file name
    """

    def __init__(self):
        super().__init__()
        self.strategy_name = 'My_Strategy'
        self.cash_balance = 0
        self.market_value = 0
        self.dayBuyingPower = 0
        self.overnightBuyingPower = 0
        self.net_account_value = 0

    """ 
    You only need to define the strategy_decision() function, and click run strategy button on the App.
    Other functions are defined in the parent class, Strategy.py, you can use them directly.
    Define your own strategy here:
    """

    def strategy_decision(self):
        """This is a simple example strategy from chatGPT, you can overwrite it in your own strategy"""
        # You can extract the code to several functions, and call them in strategy_decision()

        # -------------------------
        # Strategy starts here:
        # 0. define the stock ticker you are going to trade
        stock = 'TQQQ'

        # 1. get the stock data from quoter, return a pandas dataframe
        data = self.quoter.get_15min_bar(stock=stock, extend_trading=True)

        # 2. calculate the indicator
        data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

        # 3. check the strategy condition,
        # for example, simply buy when rsi < 30, sell when rsi > 70
        current_rsi = data['RSI'][-1]
        action = None
        if current_rsi < 30:
            # print for your reference
            print(f"{stock}: current_rsi: {current_rsi}, price: {data['Close'][-1]}")
            print('buy point start')
            print('-------------------------')
            action = 'buy'

        elif current_rsi > 70:
            print(f"{stock}: current_rsi: {current_rsi}, price: {data['Close'][-1]}")
            print('sell point start')
            print('-------------------------')
            action = 'sell'

        else:
            print('no action needed')
            print('-------------------------')

        # 4. place order if needed, using the trader object to place order
        action_res = ''
        if action == 'buy':
            if is_market_hours():
                action_res = self.parent.trader.order_market_buy(stock, quantity=1)
            else:
                price = self.parent.trader.get_bid_price(stock)
                action_res = self.parent.trader.order_limit_buy_day(stock, price, quantity=1)
                # for GTC order, use self.parent.trader.order_limit_buy_gtc(stock, price, qty)

            play_sound.order_placed()

        elif action == 'sell':
            if is_market_hours():
                action_res = self.parent.trader.order_market_sell(stock, quantity=1)
            else:
                price = self.parent.trader.get_ask_price(stock)
                action_res = self.parent.trader.order_limit_sell_day(stock, price, quantity=1)

            play_sound.order_placed()
        else:
            # do whatever you want
            pass

        # Strategy ends here
        # -----------------------------
        # Set the info you need to show in the GUI
        info = f"""
        {data.index[-1].strftime("%Y-%m-%d %H:%M:%S")}, Stock: {stock}\n
        Price: {round(data['Close'][-1], 2)} RSI: {round(data['RSI'][-1], 2)} 15min\n
               """
        self.update_quoter_stream(info)
        self.update_strategy_stream(action_res)

        if action == 'buy' or action == 'sell':
            # save the trading history
            self.save_strategy_actions(action_res)
            self.update_strategy_profile()
            # Send the trading action email and notification to the GUI
            self.send_notification(action_res)
