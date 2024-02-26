import pandas as pd

# Read input data
data_path = "/workflow/inputs/input_dir/data.csv"
df = pd.read_csv(data_path)

# Process data
print(df)
df = df.drop('a', axis=1)
print(df)
