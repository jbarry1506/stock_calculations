import yfinance as yf
import pprint
import time
from termcolor import colored

""" 
## EXAMPLE OF BASE DATA
# apple = yf.Ticker('AAPL')
# data_aapl = apple.info
# pprint.pprint(data_appl)
"""

## Data
# 52 week change
    # stock_info['52WeekChange']

# Ask price (seller offer)
    # stock_info['ask']

# Bid price (buyer offer)
    # stock_info['bid']

# what was the market value at the last close
    # stock_info['previousClose']

# trading volume
    # I think this is in the info

# outstanding shares
# Share Turnover Ratio = trading volume / average shares

# Is the stock liquid
# TODO:  WRITE STOCK LIQUIDITY FUNC


# get all info for stock
def get_investment_info(symbol):
    inv_data = yf.Ticker(symbol)
    inv_info = inv_data.info
    return inv_info


# Bid-ask spread = ask - bid
def bid_ask_spread(stock_info):
    return stock_info['ask'] - stock_info['bid']


# is the stock above the 50 day moving average
def above_fifty_day(fifty, bid):
    return bid > fifty


# is the stock above the 200 day moving average
def fifty_above_twohun(twohun, fifty):
    return fifty > twohun


# analyze the data
def investment_analysis(investments):
    for ms in investments:
        investment_info = None
        try:
            investment_info = get_investment_info(ms)
        except:
            print(colored("That symbol is not available for analysis at this time.", 'red'))
            continue
        
        name = investment_info['longName']
        investment_type = investment_info['quoteType']
        high_52 = investment_info['fiftyTwoWeekHigh']
        two_hundred_average = investment_info['twoHundredDayAverage']
        fifty_average = investment_info['fiftyDayAverage']
        previous_close = investment_info['previousClose']
        regular_market_previous_close = investment_info['regularMarketPreviousClose']
        regular_market_price = investment_info['regularMarketPrice']
        ytdreturn = investment_info['ytdReturn']
        last_split_date = time.ctime(investment_info['lastSplitDate'])
        last_split_factor = investment_info['lastSplitFactor']
        last_dividend_value = investment_info['lastDividendValue']
        dividend_rate = investment_info['dividendRate']
        dividend_yield = investment_info['dividendYield']

        print('\n')
        print(colored('{} \t {}'.format(name, ms), 'yellow'))
        try:
            print('The previous close was {}'.format(previous_close))
        except:
            print("The previous close data is not available for {}".format(name))

        try:
            print('The reg market previous close was {}'.format(regular_market_previous_close))
        except:
            print("The reg market previous close data is not available for {}".format(name))

        try:
            if regular_market_previous_close > regular_market_price:
                print(colored('The reg market price was {}'.format(regular_market_price), 'red'))
            else:
                print(colored('The reg market price was {}'.format(regular_market_price), 'green'))
        except:
            print("The reg market price data is not available for {}".format(name))

        try:
            print("YTD return is {}".format(ytdreturn))
            print(type(ytdreturn))
            if ytdreturn > .3:
                print("\t Look closer!")
        except:
            print("ytd return is not available for {}".format(name))

        try:
            print("The last split date was {} at a {} ratio.".format(last_split_date, last_split_factor))
        except:
            print("Unable to resolve a split date or factor.")

        # try to find the bid and ask values
        try:
            ask = investment_info['ask']
            buy = investment_info['bid']
            ba_spread = bid_ask_spread(investment_info)
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
        try:
            print("\tLast Dividend Value:  {}".format(last_dividend_value))
            print("\tDividend Rate:  {}".format(dividend_rate))
            print("\tDividend Yield:  {}".format(dividend_yield))
        except:
            print("Dividend rate or yield not available.")
        
    print(colored('got all the data', 'cyan'))


my_stocks = ['msft', 'aapl', 'sage', 'mdb', 'flr', 'ntnx']
lauren = ['fscsx', 'aapl', 'brk\\b']
jim = ['ggotx', 'msft', 'mu', 'qrvo', 'jagtx', 'trrdx', 'fscsx', 'aapl', 'ddog']
principal = ['fxnax', 'jcbux', 'mphrx', 'pgblx', 'trrfx', 'trrax', 'trrbx', 
'trrgx', 'trrhx', 'trrcx', 'trrjx', 'trrdx', 'trrkx', 'trrmx', 'trrnx', 'trrlx',
'fxaix', 'fcgax', 'peiqx', 'vftnx', 'aredx', 'ggotx', 'jvtnx', 'flmvx', 'fsccx', 
'vspmx', 'vsmsx', 'rerfx', 'odvyx', 'vtmgx'
]
janus = ['JABLX', 'JGLTX', 'JATAX', 'JDBAX', 'JACAX', 'JDCAX', 'JAGRX', 'JAFLX', 'JRAAX', 'JAWGX', 'JAGTX']

jagtx_top = ['MSFT', 'AAPL', 'AMZN', 'ADBE', 'MA', 'TXN', 'BABA', 'FB', 'ASML', 'CRM']
ggotx_top = ['LULU', 'VRSK', 'ORLY', 'DOCU', 'SPLK', 'VEEV', 'CDNS', 'ROK', 'BLL', 'PANW']
fscsx_top = ['MSFT', 'V', 'ADBE', 'CRM', 'MA', 'PYPL', 'GOOGL', 'CTSH', 'ORCL']

my_investments = [jim]

for i in my_investments:
    print('\n', i)
    investment_analysis(i)
