import pyreadr
import numpy as np
data = pyreadr.read_r('data/2018_main.rds')
df=data[None]
print(df.columns.values)
# print(df)
