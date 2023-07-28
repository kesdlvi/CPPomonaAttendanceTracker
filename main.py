import pandas as pd

df  = pd.read_csv("data.csv")

third_column_name = df.columns[2]  # Assuming the third column is at index 2 (0-based index)
third_column_data = df[third_column_name ]

print(third_column_data.dropna())