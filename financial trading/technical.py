







def sum_two_value(n1:int,n2:int,d=0) -> int:
    """
    n1:number 1
    n2:number 2
    d:default value which is 0
    """
    sum1=n1+n2
    return sum1

sum_two_value()

# l=len([1,2,3])
# print(l)
# s='hello'
# # s.replace()

# import pandas as pd

# pd.DataFrame()

# import random as rd

# r=rd.randint(a=10,b=100)
# r=rd.randint(b=10,a=100)
# print(r)


# import yfinance as yf


# yf.download()


# t=yf.Ticker(ticker='TSLA')
# print(t.option_chain())



# import yfinance 
# yfinance.download('TSLA',period='1mo')

# import yfinance as yf
# yf.download('AMZN',period='1mo')

# from yfinance import download,Ticker
from yfinance import *
import pandas as pd
# download('GOOG',period='1mo')

# Ticker('TSLA')

df1=download(tickers='TSLA',start='2024-01-01',end='2024-01-31')
df2=download(tickers='TSLA',start='2024-02-01',end='2024-02-28')
print(df1)
print(df2)


new_df=pd.concat([df1, df2])
print(new_df)

new_df=new_df.drop(['Adj Close','Volume'],axis=1)
print(new_df)

new_df['avg']=(new_df['Open']+new_df['High']+new_df['Low']+new_df['Close'])/4
print(new_df)



t_object=Ticker('RELIANCE.NS')

print(t_object.balance_sheet)