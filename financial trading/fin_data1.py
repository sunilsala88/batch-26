

import yfinance as yf

# data=yf.download('TSLA','2024-01-01','2024-06-01')
# data=yf.download(tickers='TSLA',start='2024-01-01',end='2024-06-01')

# data=yf.download(tickers="TSLA",period='1mo')
# print(data)

t=yf.Ticker(ticker='GOOG')
# print(t.info.get('beta'))
# print(t.news)
import pandas as pd

df=pd.DataFrame(t.get_news())
print(df)

df.to_csv('demo1.csv')

#beta of dow jones
