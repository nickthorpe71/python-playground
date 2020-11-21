import numpy as np
import pandas as pd

# 2. read text file into dataframe
filename = 'weather_data.txt'
df = pd.read_csv(filename)
print(df)

# 6. sort records by any column
print(df.sort_values('record_high', ascending=False))

