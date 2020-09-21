import numpy
import yfinance as yf

# earnings growth rate
egr_years = [10,5,3]

rate_test = numpy.rate(nper=5,pmt=0, pv=-463,fv=1683)
print(rate_test)

msft = yf.Ticker('msft')
hist = msft.history(period='1y',interval='1mo')
print(hist)