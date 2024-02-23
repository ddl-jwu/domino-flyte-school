import pandas as pd
import argparse

data_path = "/workflow/inputs/data_path"
df = pd.read_csv(data_path)
print(df)
df = df.drop('a', axis=1)
print(df)

df.to_csv("/workflow/outputs/processed_data")