# from finvizfinance.quote import finvizfinance

# stock = finvizfinance('tsla')

# print(stock.ticker_news().to_csv('demo2.csv'))

# import pandas as pd

# print(pd.Series(stock.ticker_fundament()).to_csv('demo2.csv'))



from finvizfinance.screener.overview import Overview

foverview = Overview()
# filters_dict = {'Index':'S&P 500','Sector':'Technology',"Market Cap.":'Mega ($200bln and more)','Target Price':"50% Above Price"}
filters_dict = {"P/E":'High (>50)'}
foverview.set_filter(filters_dict=filters_dict)
df = foverview.screener_view()
print(df)
df.head()
print(df.head())
