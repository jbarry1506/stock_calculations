import yfinance as yf
import pprint

# microsoft = yf.Ticker('MSFT')
# apple = yf.Ticker('AAPL')
# vray = yf.Ticker('VRAY')
# data_vray = vray.info
# pprint.pprint(data_vray)

# data_msft = microsoft.info
# data_aapl = apple.info

# gild = yf.Ticker('GILD')
# data_gild = gild.info
# pprint.pprint(data_gild)

## Data to find
# get all info for stock
def get_stock_info(stock):
    stock_data = yf.Ticker(stock)
    stock_info = stock_data.info
    return stock_info

# Is the stock liquid
# TODO:  WRITE STOCK LIQUIDITY FUNC

# Ask price (seller offer)
def get_stock_ask(stock_info):
    return stock_info['ask']

# Bid price (buyer offer)
def get_stock_bid(stock_info):
    return stock_info['bid']

# Bid-ask spread = ask - bid
def bid_ask_spread(stock_info):
    return get_stock_ask(stock_info) - get_stock_bid(stock_info)

# trading volume

# outstanding shares
# Share Turnover Ratio = trading volume / average shares

my_stocks = ['msft', 'aapl', 'vray', 'gild', 'sage', 'mdb', 'jpm']

for ms in my_stocks:
    stock_info = get_stock_info(ms)
    ask = get_stock_ask(stock_info)
    buy = get_stock_bid(stock_info)
    ba_spread = bid_ask_spread(get_stock_info(ms))
    print('The sellers are asking {} for {}'.format(ask, ms))
    print('The buyers are buying at {} for {}'.format(buy, ms))
    print('This puts the bid-ask spread at {}'.format(ba_spread))
    
print('got all the data')