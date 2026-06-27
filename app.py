import pandas as pd
from query_engine import run_query

df = pd.read_csv("data/mutual_funds.csv")

query = input("Enter query: ")

result = run_query(df, query)

print(result)
