import pandas as pd

df = pd.read_csv("data/mutual_funds.csv")

query = input("Enter query: ")

column, operator, value = query.split(maxsplit=2)

try:
    value = float(value)

    if operator == ">":
        result = df[df[column] > value]

    elif operator == "<":
        result = df[df[column] < value]

    elif operator == "==":
        result = df[df[column] == value]

except ValueError:

    if operator == "==":
        result = df[df[column] == value]

print(result)