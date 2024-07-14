import pandas as pd
# df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/SBIN.csv')
# print(df)

# df1=df.iloc[:100,]
# print(df1)

# df2=df.iloc[101:200,]
# print(df2)

# df3=pd.concat([df1,df2])
# print(df3)

# df.index.name='sample'

# df5=df[['open','high']]
# df6=df[['close','volume']]
# print(df5)
# print(df6)


# df7=pd.merge(df5,df6,on='sample')
# print(df7)


# df1=pd.DataFrame([[1,2],[3,4]],columns=['x','y'],index=['a','b'])

# df1.index.name='ind1'
# df2=pd.DataFrame([[11,22,33],[44,55,66],[88,99,68]],columns=['m','n','o'],index=['a','b','c'])

# df2.index.name='ind1'
# print(df1)
# print(df2)

# df3=pd.merge(df1,df2,on='ind1',how='right')
# print(df3)



df1=pd.DataFrame([[1,2],[3,4]],columns=['x','y'],index=['a','b'])

# df1.index.name='ind1'
df2=pd.DataFrame([[11,22,33],[44,55,66],[88,99,68]],columns=['z','x','y'],index=['c','d','e'])

# df2.index.name='ind1'
print(df1)
print(df2)

df3=pd.concat([df1,df2])
# df3=pd.merge(df1,df2,on='ind1',how='right')
print(df3)
