import pandas as pd

df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')
print(df)

# df=df.drop(2,axis=0)
df.drop(2,axis=0,inplace=True)
print(df)

# df.drop('Funding',axis=1,inplace=True)
# print(df)
# df.drop(1072,axis=0,inplace=True)
# print(df)

df=df.drop('Year Founded',axis=1)
print(df)

import pandas as pd
data=pd.DataFrame([[1,2,3],[4,5,6],[1,7,7]])
print(data)
data.drop_duplicates(subset=0,inplace=True)
print(data)