
query = input("Enter query: ")
condition = query

parts = condition.split(maxsplit=2)


column = parts[0]
operator = parts[1]
value = parts[2]

print(column)
print(operator)
print(value)