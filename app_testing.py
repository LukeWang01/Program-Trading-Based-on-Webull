# start trading test
from Trader import Trader
from env.de_k import *
from env._secrete import *
import time

"""

Test login, real time price quote, and then place order

For test only.
"""

user_email = user_email_cn
pd = str(decryption_key_pd())
access_token = decryption_key_at()
pd2 = str(decryption_key_pd2())
device_name = device_name
trader = Trader()


trader.set_trader_info(user_email, pd, pd2, device_name)
trader.access_token = decryption_key_at()
trader.log_in()
time.sleep(3)

trader.enable_trading()
time.sleep(3)

res_dict = trader.get_stock_quote('SOXL')
time.sleep(3)

price = trader.get_buy_one_price('SOXL')

if price:
    trader.order_limit_buy_gtc('SOXL', price, 1)

