import pandas as pd

def run_query(df, query):
    
    supported_operators = ["==", ">", "<"]
    conditions = query.split(" AND ")

    result = df

    for condition in conditions:

        column, operator, value = condition.split(maxsplit=2)
        if column not in df.columns:
            print(f"Error: Column '{column}' does not exist")
            return None

        if operator not in supported_operators:
            print(f"Error: Operator '{operator}' is not supported")
            return None

        if operator == ">":
            result = result[result[column] > float(value)]

        elif operator == "<":
            result = result[result[column] < float(value)]

        elif operator == "==":

            try:
                value = float(value)
                result = result[result[column] == value]

            except ValueError:
                result = result[result[column] == value]

    return result