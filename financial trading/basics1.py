# import pandas as pd

# data=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# df=data[0]
# print(df)
# print(df.info())

# print(df.columns)

# df['Date added']=pd.to_datetime(df['Date added'],format='%Y-%m-%d')

# df['Founded']=df['Founded'].str[:4].astype(int)
# print(df.info())

# # print(df.sort_values(by='Date added'))

# print(df)
# #astype

# #get all comp found after 2000 and dateadded after 2010

# df1=df[(df['Founded']>2000) ]
# df1=df1[(df['Date added'])>pd.to_datetime('2010-01-01')]
# print(df1)


# df5=pd.read_excel('/Users/algotrading2024/batch 26/financial trading/Data2.xlsx')
# print(df5)


import yfinance as yf

data=yf.download(tickers='AMZN',start='2021-01-01',end='2024-06-30')
print(data)