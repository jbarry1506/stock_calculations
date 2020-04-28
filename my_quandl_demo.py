import quandl
import creds

# each data source is a subscription
# SHARADAR $39.99/mo || $299/yr
quandl.ApiConfig.api_key = creds.quandlcom_key
mydata = quandl.get_table('SHARADAR/SEP', date='2018-12-31', ticker='XOM')
print(mydata)

