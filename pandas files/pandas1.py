
import pandas as pd
import numpy as np
# a=[[1,2,3],[4,5,6],[7,8,9]]
# np1=np.array(a)
# print(np1)
# df=pd.DataFrame(np1,columns=['a','b','c'],index=['x','y','z'])
# print(df)
# df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/sp500.csv')
# print(df)

# print(df.tail(10))
# print(df.info())
# print(df.describe())

# print(df.shape)
# print(list(df.columns))
# print(df.values)
# print(list(df.index))

#print(df.sort_values('Sector'))

# print(df['Name'])
# print(df[ ['Name','Price'] ])

# print(df[df['EPS']<10])

#price greater than 100
#eps less than 5
# print(df[ (df['EPS']<5) & (df['Price']>100)  ])

# df['add']=df['Price']**2
# print(df)

df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')
print(df)

df1=df.set_index('Company')
print(df1)
print(df1.reset_index(drop=True))

print(list(df1.columns))