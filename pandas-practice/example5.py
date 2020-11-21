import numpy as np
import pandas as pd

# 2. read text file into dataframe
filename = 'weather_data.txt'
df = pd.read_csv(filename)
print(df)

# 5. statistical summary of each column
print(df.describe())
