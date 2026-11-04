from pandas import isna

print("Hello World")


import ssl
# Bypass SSL verification checks globally
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")
print(df.head())

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

#Task 2
print(df.isna())

#PDS_Practical 3.1
print(df.iloc[0])
print(df.iloc[10:20])
print(df.loc[0:5, ['total_bill', 'tip']])

print(df.iloc[239:])
print(df.loc[20:30, ['total_bill', 'tip']])

print(df[df['day'] == 'Sun'])
print(df[(df['day'] == 'Sun') & (df['total_bill'] > 20)])
print(df.query("day == 'Sun' and total_bill > 20"))