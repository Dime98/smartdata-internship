import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("Pokemon.csv")

# df[df["Total"].isnull()]
nan = []
for i in df["Total"]:
    print(i, np.isnan(i) )
    nan.append(i)
# print(len(nan))
# print(nan)


print( df["Legendary"].isnull().sum(axis = 0) )
print( df["Legendary"].isna().sum() )