import pandas as pd

df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')
print(df)
print(type(df))
print(type(df['Company']))
#make a dataframe
list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
df=pd.DataFrame(list_of_lists,columns=['a','b','c'],index=['x','y','z'])
print(df)

#make a series
list1=[1,2,3]
series1=pd.Series(list1, name='d')
print(series1)
print(list(series1))

print(series1.to_list())