
import pandas as pd
import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
np1=np.array(a)
print(np1)
df=pd.DataFrame(np1,columns=['a','b','c'],index=['x','y','z'])
print(df)

print(df['a']['y'])

data=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')

data=data.set_index('Company')
print(data)
# 2 square bracket
print(data['Funding']['Zihaiguo'])

#loc
print(data.loc['Zihaiguo' ,'Funding' ])

#iloc
print(data.iloc[-3,-1])

print(data.loc['Zopa',['Industry','Funding']])
print(data.iloc[-2,-2:])

print(data.loc[ 'SpaceX':'SHEIN', 'Date Joined': 'Industry' ])

print(data.loc[['Stripe','Klarna'],['Valuation','Funding']])
print(data.iloc[[3,4],[0,-1]])


