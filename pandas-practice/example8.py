import numpy as np
import pandas as pd

# 2. read text file into dataframe
filename = 'weather_data.txt'
df = pd.read_csv(filename)
print(df)

# 8. filtering
print(df[df.avg_percipitation > 5.0])

print(df[df['month'].isin(['Jun','Jul','Aug'])])
