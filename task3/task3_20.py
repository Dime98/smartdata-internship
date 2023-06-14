import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df["Min.Price"].value_counts

def repl_nan(val, replace_with):
    # print()
    print(f"val   {val} {type(val)}")
    # # print(f"np.nan  {np.nan} {type(np.nan)}")
    # # print(np.isnan(val), val == np.nan)
    # # print(f"replace_with {replace_with}")
    if np.isnan(val) or val == None:
        print("\t",val,replace_with)
        val = replace_with
    return val

mean = df['Min.Price'].mean()
df['Min.Price'] = df['Min.Price'].apply(lambda x : repl_nan(x, mean))
# df['Min.Price'].mean()

print()
# print(df['Min.Price'])
# print(df['Min.Price'].value_counts)