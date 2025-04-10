data = {"a": 10, "b": 20}
value = data.pop("a")
print(value)
print(data)  # Output: "10  {'b': 20}"

info = {"name": "Sara"}
result = info.pop("age", "Not found")
print(result)  # Output: "Not found"

d = {"x": 1}
# d.pop("y")  ← This would raise an error
# Output: "KeyError: 'y'"