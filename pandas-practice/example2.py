import numpy as np
import pandas as pd

# 2. read text file into dataframe
filename = 'weather_data.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 ot last 3 rows of df
print(df.head())
print(df.tail(3))

# 4. get data types, index, columns, values
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)
