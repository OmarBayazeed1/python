#80.Create a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 30]

result = {}
for i in range(len(keys)):
    value = values[i] if i < len(values) else None
    result[keys[i]] = value

print(result)
