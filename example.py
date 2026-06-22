import pandas as pd

# Load data
df = pd.read_csv("data/mutual_funds.csv")

# User query
query = input("Enter query: ")

# Split query into conditions
conditions = query.split(" AND ")

# Start with all rows
result = df

# Process each condition
for condition in conditions:

    column, operator, value = condition.split(maxsplit=2)

    # Numeric conditions
    if operator == ">":
        result = result[result[column] > float(value)]

    elif operator == "<":
        result = result[result[column] < float(value)]

    # Text conditions
    elif operator == "==":

        # Try numeric comparison first
        try:
            value = float(value)
            result = result[result[column] == value]

        # Otherwise text comparison
        except ValueError:
            result = result[result[column] == value]

print(result)