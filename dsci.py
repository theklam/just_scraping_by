import pyreadr
import numpy as np
data = pyreadr.read_r('cleaned_data/data14.rds')
df=data[None]
print(df.columns.values)
print(df)
