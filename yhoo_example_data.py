import yfinance as yf
import pprint

## EXAMPLE OF BASE DATA
apple = yf.Ticker('AAPL')
data_aapl = apple.info
pprint.pprint(data_aapl)

"""
{'52WeekChange': 0.38655996,
 'SandP52WeekChange': -0.03470111,
 'address1': 'One Apple Park Way',
 'algorithm': None,
 'annualHoldingsTurnover': None,
 'annualReportExpenseRatio': None,
 'ask': 293.59,
 'askSize': 1400,
 'averageDailyVolume10Day': 38180283,
 'averageVolume': 50937266,
 'averageVolume10days': 38180283,
 'beta': 1.173542,
 'beta3Year': None,
 'bid': 293.49,
 'bidSize': 1200,
 'bookValue': 18.137,
 'category': None,
 'circulatingSupply': None,
 'city': 'Cupertino',
 'companyOfficers': [],
 'country': 'United States',
 'currency': 'USD',
 'dateShortInterest': 1586908800,
 'dayHigh': 293.69,
 'dayLow': 286.33,
 'dividendRate': 3.28,
 'dividendYield': 0.0113,
 'earningsQuarterlyGrowth': -0.027,
 'enterpriseToEbitda': 16.527,
 'enterpriseToRevenue': 4.768,
 'enterpriseValue': 1277636247552,
 'exDividendDate': 1588896000,
 'exchange': 'NMS',
 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EDT',
 'expireDate': None,
 'fiftyDayAverage': 263.4409,
 'fiftyTwoWeekHigh': 327.85,
 'fiftyTwoWeekLow': 170.27,
 'fiveYearAverageReturn': None,
 'fiveYearAvgDividendYield': 1.59,
 'floatShares': 4329393858,
 'forwardEps': 14.73,
 'forwardPE': 19.90224,
 'fromCurrency': None,
 'fullTimeEmployees': 137000,
 'fundFamily': None,
 'fundInceptionDate': None,
 'gmtOffSetMilliseconds': '-14400000',
 'heldPercentInsiders': 0.00066,
 'heldPercentInstitutions': 0.6222,
 'industry': 'Consumer Electronics',
 'isEsgPopulated': False,
 'lastCapGain': None,
 'lastDividendValue': None,
 'lastFiscalYearEnd': 1569628800,
 'lastMarket': None,
 'lastSplitDate': 1402272000,
 'lastSplitFactor': '7:1',
 'legalType': None,
 'logo_url': 'https://logo.clearbit.com/apple.com',
 'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets '
                        'smartphones, personal computers, tablets, wearables, '
                        'and accessories worldwide. It also sells various '
                        'related services. The company offers iPhone, a line '
                        'of smartphones; Mac, a line of personal computers; '
                        'iPad, a line of multi-purpose tablets; and wearables, '
                        'home, and accessories comprising AirPods, Apple TV, '
                        'Apple Watch, Beats products, HomePod, iPod touch, and '
                        'other Apple-branded and third-party accessories. It '
                        'also provides digital content stores and streaming '
                        'services; AppleCare support services; and iCloud, a '
                        'cloud service, which stores music, photos, contacts, '
                        'calendars, mail, documents, and others. In addition, '
                        'the company offers various service, such as Apple '
                        'Arcade, a game subscription service; Apple Card, a '
                        'co-branded credit card; Apple News+, a subscription '
                        'news and magazine service; and Apple Pay, a cashless '
                        'payment service, as well as licenses its intellectual '
                        'property, and provides other related services. The '
                        'company serves consumers, and small and mid-sized '
                        'businesses; and the education, enterprise, and '
                        'government markets. It sells and delivers third-party '
                        'applications for its products through the App Store, '
                        'Mac App Store, and Watch App Store. The company also '
                        'sells its products through its retail and online '
                        'stores, and direct sales force; and third-party '
                        'cellular network carriers, wholesalers, retailers, '
                        'and resellers. Apple Inc. has a collaboration with '
                        'Google to develop COVID-19 tracking system for '
                        'Android and iOS devices. Apple Inc. was founded in '
                        '1977 and is headquartered in Cupertino, California.',
 'longName': 'Apple Inc.',
 'market': 'us_market',
 'marketCap': 1282715680768,
 'maxAge': 1,
 'maxSupply': None,
 'messageBoardId': 'finmb_24937',
 'morningStarOverallRating': None,
 'morningStarRiskRating': None,
 'mostRecentQuarter': 1585353600,
 'navPrice': None,
 'netIncomeToCommon': 57215000576,
 'nextFiscalYearEnd': 1632787200,
 'open': 289.17,
 'openInterest': None,
 'payoutRatio': 0.2408,
 'pegRatio': 2.05,
 'phone': '408-996-1010',
 'previousClose': 289.07,
 'priceHint': 2,
 'priceToBook': 16.163645,
 'priceToSalesTrailing12Months': 4.786592,
 'profitMargins': 0.21350001,
 'quoteType': 'EQUITY',
 'regularMarketDayHigh': 293.69,
 'regularMarketDayLow': 286.33,
 'regularMarketOpen': 289.17,
 'regularMarketPreviousClose': 289.07,
 'regularMarketPrice': 289.17,
 'regularMarketVolume': 33391986,
 'revenueQuarterlyGrowth': None,
 'sector': 'Technology',
 'sharesOutstanding': 4375479808,
 'sharesPercentSharesOut': 0.008,
 'sharesShort': 34636195,
 'sharesShortPreviousMonthDate': 1584057600,
 'sharesShortPriorMonth': 38427917,
 'shortName': 'Apple Inc.',
 'shortPercentOfFloat': 0.008,
 'shortRatio': 0.61,
 'startDate': None,
 'state': 'CA',
 'strikePrice': None,
 'symbol': 'AAPL',
 'threeYearAverageReturn': None,
 'toCurrency': None,
 'totalAssets': None,
 'tradeable': False,
 'trailingAnnualDividendRate': 3.08,
 'trailingAnnualDividendYield': 0.010654858,
 'trailingEps': 12.728,
 'trailingPE': 23.032684,
 'twoHundredDayAverage': 279.22528,
 'volume': 33391986,
 'volume24Hr': None,
 'volumeAllCurrencies': None,
 'website': 'http://www.apple.com',
 'yield': None,
 'ytdReturn': None,
 'zip': '95014'}
"""