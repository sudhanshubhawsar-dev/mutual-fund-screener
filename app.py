import pandas as pd
from query_engine import run_query

df = pd.read_csv("data/mutual_funds.csv")

query = input("Enter query: ").strip()

if not query:
    print("Error: Query cannot be empty")
else:
    result = run_query(df, query)
    
    if result is not None:
        print(result)
