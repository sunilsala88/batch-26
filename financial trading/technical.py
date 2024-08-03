

import yfinance as yf


# d=yf.download(tickers='MSFT',period='1mo')
# d=yf.download('MSFT',period='1mo')
# d=yf.download(tickers='MSFT',start='2024-01-01',end='2024-02-01')
d=yf.download('MSFT','2024-01-01','2024-02-01')
print(d)

# t=yf.Ticker()



def abc(a:list,b:str,c=0)-> list:
    """
    a(number 1): int
    b(number 2): int
    c:optional parameter default is 0
    """
    b=b.upper()
    a.append(b)
    return a


ans=abc(a=[1],b='y')
print(ans)