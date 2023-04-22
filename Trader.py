from webull import webull
import datetime


class Trader:

    def __init__(self):
        """
        :param username: phone or email
        :param password:
        """
        # Log in authentication:
        self.username = ''
        self.password = ''
        self.device_name = ''

        # Trading token authentication:
        self.PID = ''

        # init webull api
        self._webull = webull()

        # Authentication additional:
        self.did = ''
        self.access_token = ''
        self.uuid = ''
        self.account_id = ''

    def set_trader_info(self, username, password, pid, device_name):
        self.username = username
        self.password = password
        self.PID = pid
        self.device_name = device_name
        return True

    def set_auth_did(self, did):
        self.did = did

    def set_auth_access_token(self, access_token):
        self.access_token = access_token

    def set_auth_uuid(self, uuid):
        self.uuid = uuid

    def get_account_id(self):
        return self.account_id

    def did_init_manually(self, did):
        self._webull._did = did

    def set_time_out(self, timeout):
        self._webull.timeout = int(timeout)

    def access_token_init_manually(self, access_token):
        self._webull._access_token = access_token

    def log_in(self, username, password, pid, device_name):
        res = self.set_trader_info(username, password, pid, device_name)
        if res:
            response = self._webull.is_logged_in()
            if not response:
                try:
                    login_result = self._webull.login(self.username, self.password, device_name=self.device_name, save_token=True)
                    self._webull._access_token = self.access_token
                    response = self._webull.is_logged_in()
                    if response:
                        self.account_id = self._webull.get_account_id()
                        print('-----------------------------------')
                        print('>>>>>>   Log in successful   <<<<<<')
                        print(f'>>>   Your login ID: {self.account_id}   <<<')
                    else:
                        print('-----------------------------------')
                        print('>>> Log in failed, authentication failed, check info below: ')
                        print(login_result)
                        return False
                except ValueError:
                    print('>>>>>>    Log in failed, please check username or password')
                    return False
            else:
                print('-----------------------------------')
                print('>>>>>>   Already Logged In   <<<<<<')
                print(f'>>>   Your login ID: {self.account_id}   <<<')
                return True
        else:
            print('-----------------------------------')
            print('>>>>>> Authentication Info Setup Failed <<<<<<')
            return False

    def log_out(self):
        response = self._webull.logout()
        print('-----------------------------------')
        print('>>> Logout requested <<<')
        print(response)

    def enable_trading(self):
        response = self._webull.get_trade_token(self.PID)
        print('-----------------------------------')
        print('>>> Enable trading requested <<<')
        if response:
            print('Trading enabled, authentication passed')
            return True
        else:
            if self._webull.is_logged_in():
                print('Authentication failed, check PID again')
                return False
            else:
                print('Authentication failed, please login again')
                return False

    def get_stock_quote(self, stock):
        res = {}
        try:
            quote_response = self._webull.get_quote(stock)
            ask_price_1 = quote_response['askList'][0]['price']
            bid_price_1 = quote_response['bidList'][0]['price']
            res['buy_one_price'] = bid_price_1
            res['sell_one_price'] = ask_price_1
            print('-----------------------------------')
            print('>>> Stock ticker: ', stock)
            print('>>> First bid price/ buy one price:  ', bid_price_1)
            print('>>> First ask price/ sell one price:  ', ask_price_1)
            return res
        except ValueError or KeyError:
            print('>>> Please pass a valid stock ticker <<<')
            return False

    def get_buy_one_price(self, stock):
        # get first bid price
        res = self.get_stock_quote(stock)
        if res:
            print('-----------------------------------')
            print('>>> Stock: ', stock, 'First bid price/ buy one price:', res['buy_one_price'])
            return res['buy_one_price']
        else:
            return False

    def get_sell_one_price(self, stock):
        # get first ask price
        res = self.get_stock_quote(stock)
        if res:
            print('-----------------------------------')
            print('>>> Stock: ', stock, 'First ask price/ sell one price: ', res['sell_one_price'])
            return res['sell_one_price']
        else:
            return False

    def order_market_buy(self, stock, qty):
        # Buy, market order, buy 1 price, daily:
        response = self._webull.place_order(stock=stock, action='BUY', enforce='DAY', orderType='MKT', quant=qty)
        price = self.get_sell_one_price(stock)
        self.print_order_details(response, stock, price, qty, 'BUY', 'MKT')

    def order_market_sell(self, stock, qty):
        # Sell, market order, sell 1 price, daily:
        response = self._webull.place_order(stock=stock, action='SELL', enforce='DAY', orderType='MKT', quant=qty)
        price = self.get_buy_one_price(stock)
        self.print_order_details(response, stock, price, qty, 'SELL', 'MKT')

    def order_limit_buy_day(self, stock, price, qty):
        # Buy, limit price order, buy 1 price, daily:
        response = self._webull.place_order(stock=stock, action='BUY', price=price, enforce='DAY', orderType='LMT', quant=qty)
        self.print_order_details(response, stock, price, qty, 'BUY', 'DAY')

    def order_limit_sell_day(self, stock, price, qty):
        # Sell, limit price order, sell 1 price, daily:
        response = self._webull.place_order(stock=stock, action='SELL', price=price, enforce='DAY', orderType='LMT', quant=qty)
        self.print_order_details(response, stock, price, qty, 'SELL', 'DAY')

    def order_limit_buy_gtc(self, stock, price, qty):
        # Buy, limit price order, buy 1 price, daily:
        response = self._webull.place_order(stock=stock, action='BUY', price=price, enforce='GTC', orderType='LMT', quant=qty)
        self.print_order_details(response, stock, price, qty, 'BUY', 'GTC')

    def order_limit_sell_gtc(self, stock, price, qty):
        # Sell, limit price order, sell 1 price, daily:
        response = self._webull.place_order(stock=stock, action='SELL', price=price, enforce='GTC', orderType='LMT', quant=qty)
        self.print_order_details(response, stock, price, qty, 'SELL', 'GTC')

    def print_order_details(self, response, stock, price, qty, direction, order_type):
        if response['success']:
            print('-----------------------------------')
            print('>>>>>> Order placed successfully! <<<<<<')
            print('>>> Account_ID: ', self.account_id)
            print('>>> Order ID: ', response['data']['orderId'])
            print('>>> Order Time: ', datetime.datetime.now())
            print('>>> Trading stock name: ', stock, 'Trading direction: ', direction, order_type, 'order.')
            print('>>> Price around: ', price)
            print('>>> Buy quantity: ', qty)
            print('>>> Total cost: ', round(float(price) * int(qty), 3))
            return True
        else:
            print('-----------------------------------')
            print('>>>>>> Order placed Failed! <<<<<<')
            print(response)
            print('>>> Please check the error msg above!')
            return False




