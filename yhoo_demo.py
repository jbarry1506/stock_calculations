import yfinance as yf
import pprint

# microsoft = yf.Ticker('MSFT')
# apple = yf.Ticker('AAPL')
# vray = yf.Ticker('VRAY')
# data_vray = vray.info
# data_msft = microsoft.info
# data_aapl = apple.info

gild = yf.Ticker('GILD')
data_gild = gild.info
pprint.pprint(data_gild)
print('got all the data')