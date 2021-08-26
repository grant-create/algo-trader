# MAKE SURE ACCOUNT IS WORKING: 
import alpaca_trade_api as tradeapi
from config import *
#API endpoint URL
url = "https://api.alpaca.markets"
#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')
#Init our account var
account = api.get_account()

# print(account.status)
# print(account.buying_power)
clock = api.get_clock()
portfolio = api.list_positions()
# print("The market is open: {}".format(clock.is_open))
portfolio = api.list_positions()
print(portfolio)