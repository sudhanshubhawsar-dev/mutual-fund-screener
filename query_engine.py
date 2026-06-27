import pandas as pd

def run_query(df, query):

    conditions = query.split(" AND ")

    result = df

    for condition in conditions:

        column, operator, value = condition.split(maxsplit=2)

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