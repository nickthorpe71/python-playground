import numpy as np
import pandas as pd

# def header(msg):

# 1. load hard-coded data into a dataframe
# header("1. load hard-coded data into a df")

df = pd.DataFrame(
        [['Jan',58,42,74,22,2.95],
        ['Feb', 61,45,78,26,3.02],
        ['Mar', 65,48,73,25,1.02],
        ['Apr', 31,15,71,46,4.16],
        ['May', 53,20,72,21,3.12],
        ['Jun', 74,32,34,37,6.22],
        ['Jul', 62,44,56,26,7.42],
        ['Aug', 51,67,26,42,2.12],
        ['Sep', 41,77,27,73,8.02],
        ['Oct', 31,83,51,25,3.52],
        ['Nov', 21,92,20,77,9.02],
        ['Dec', 11,26,18,86,2.02],
        ],
        index = [0,1,2,3,4,5,6,7,8,9,10,11],
        columns = ['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_percipitation'])
print(df)

