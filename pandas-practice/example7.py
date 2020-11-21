import numpy as np
import pandas as pd

# 2. read text file into dataframe
filename = 'weather_data.txt'
df = pd.read_csv(filename)
print(df)

# 7. slicing records
print(df.avg_low)
print(df['avg_low'])
print(df[2:4])
print(df[['avg_low','avg_high']])
print(df.loc[:,['avg_low','avg_high']])
print(df.loc[9,['avg_percipitation']])
print(df.iloc[3:5,[0,3]])
