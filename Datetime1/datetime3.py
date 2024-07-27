

st1='2023-01-01'
import pandas as pd
dt1=pd.to_datetime(st1)
print(dt1)

dt2=pd.to_datetime('2020-01-01')

df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/SBIN.csv')
print(df.info())
df['date']=pd.to_datetime(df['date'])
print(df.info())
print(df)


df['new_date']=df['date']+pd.Timedelta(minutes=1)
print(df)

print(dt1.day_name())
print(df['date'].dt.day_name())

a='hello'
print(a.upper())