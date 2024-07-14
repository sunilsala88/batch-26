import pandas as pd
df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/SBIN.csv')
print(df)

df1=df.iloc[:100,]
print(df1)

df2=df.iloc[101:200,]
print(df2)

df3=pd.concat([df1,df2])
print(df3)

df.index.name='sample'

df5=df[['open','high']]
df6=df[['close','volume']]
print(df5)
print(df6)


df7=pd.merge(df5,df6,on='sample')
print(df7)

