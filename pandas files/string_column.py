
import pandas as pd


df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')
print(df)
# print(df.info())
# print(df[df['Company'].str.startswith('A')])
# print(df[df['Company'].str.upper().str.endswith('I')])
# print(df['Date Joined'].str[-4:])
df['new_date']=pd.to_datetime(df['Date Joined'],format='%d-%m-%Y')
print(df['new_date']+pd.Timedelta(days=1))