import pandas as pd

df  = pd.read_csv("data.csv")

email_col_name  = df.columns[1]
email_col_data = df[email_col_name]

third_column_name = df.columns[2]  # Assuming the third column is at index 2 (0-based index)
third_column_data = df[third_column_name ]

print(third_column_data.dropna().iloc[:20] + " " + email_col_data.dropna().iloc[:20])