
import pandas as pd



df=pd.read_csv('/Users/algotrading2024/batch 26/pandas files/Unicorn_companies.csv')
print(df)
print(df.info())
df = df.astype({
    "Funding": "int",
})
print(df.info())
print(df)