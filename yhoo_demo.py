import yfinance as yf
import pprint

# Is the stock liquid
# TODO:  WRITE STOCK LIQUIDITY FUNC

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

## Data
# 52 week change
    # stock_info['52WeekChange']

# Ask price (seller offer)
    # stock_info['ask']

# Bid price (buyer offer)
    # stock_info['bid']


# get all info for stock
# TODO - CHANGE FUNCTION TO get_investment_info(symbol)
def get_investment_info(stock):
    stock_data = yf.Ticker(stock)
    stock_info = stock_data.info
    return stock_info


# Bid-ask spread = ask - bid
def bid_ask_spread(stock_info):
    return stock_info['ask'] - stock_info['bid']


# is the stock above the 50 day moving average
def above_fifty_day(fifty, bid):
    return bid > fifty


# is the stock above the 200 day moving average
def fifty_above_twohun(twohun, fifty):
    return fifty > twohun


# what was the market value at the last close
    # stock_info['previousClose']

# trading volume
    # I think this is in the info

# outstanding shares
# Share Turnover Ratio = trading volume / average shares

my_stocks = ['msft', 'aapl', 'gild', 'sage', 'mdb', 'flr', 'ntnx']
lauren = ['fscsx']
principal = ['fxnax', 'jcbux', 'mphrx', 'pgblx', 'trrfx', 'trrax', 'trrbx', 
'trrgx', 'trrhx', 'trrcx', 'trrjx', 'trrdx', 'trrkx', 'trrmx', 'trrnx', 'trrlx',
'fxaix', 'fcgax', 'peiqx', 'vftnx', 'aredx', 'ggotx', 'jvtnx', 'flmvx', 'fsccx', 
'vspmx', 'vsmsx', 'rerfx', 'odvyx', 'vtmgx'
]

my_investments = [my_stocks, principal]

# TODO - MAKE THIS A FUNCTION
for ms in my_stocks:
    stock_info = None
    try:
        stock_info = get_investment_info(ms)
    except:
        print("That symbol is not available for analysis at this time.")
        break
    
    name = stock_info['longName']
    investment_type = stock_info['quoteType']
    high_52 = stock_info['fiftyTwoWeekHigh']
    two_hundred_average = stock_info['twoHundredDayAverage']
    fifty_average = stock_info['fiftyDayAverage']
    previous_close = stock_info['previousClose']

    print('\n', name)
    # try to find the bid and ask values
    try:
        ask = stock_info['ask']
        buy = stock_info['bid']
        ba_spread = bid_ask_spread(stock_info)
        print('The sellers are asking {} for {}'.format(ask, ms))
        print('The buyers are buying at {} for {}'.format(buy, ms))
        print('This puts the bid-ask spread at {}'.format(ba_spread))
        if above_fifty_day(fifty_average, buy) and fifty_above_twohun(two_hundred_average, fifty_average):
            print("The current buy price is above the fifty day average and the fifty is above the two hundred.")
        else:
            print("The fifty day average is {}".format(fifty_average))
            print("The two hundred day average is {}".format(two_hundred_average))
    except:
        print("The bid-ask spread can't be calculated for {}".format(name))
        if above_fifty_day(fifty_average, previous_close) and fifty_above_twohun(two_hundred_average, fifty_average):
            print("The previous close is above the fifty day average and the fifty is above the two hundred.")
        else:
            print("The fifty day average is {}".format(fifty_average))
            print("The two hundred day average is {}".format(two_hundred_average))            

    print("The investment type is {}".format(investment_type))
    
print('got all the data')