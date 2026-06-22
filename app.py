import pandas as pd

df = pd.read_csv("data/mutual_funds.csv")

result = df[df['return_3y'] > 20]

print(result[['fund_name', 'return_3y']])
