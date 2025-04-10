data = {"a": 1, "b": 2}
last = data.popitem()
print(last)
print(data)  # Output: "('b', 2)  {'a': 1}"

data = {"x": 100}
pair = data.popitem()
print(pair)  # Output: "('x', 100)"

empty = {}
# empty.popitem()  ← This will raise KeyError
# Output: "KeyError: 'popitem(): dictionary is empty'"