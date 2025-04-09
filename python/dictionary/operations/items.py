info = {"name": "Sara", "age": 22}
print(info.items())  # Output: "dict_items([('name', 'Sara'), ('age', 22)])"

info = {"x": 1, "y": 2}
for key, value in info.items():
    print(key, value)  # Output: "x 1  y 2"

data = {"a": 10, "b": 20}
print(list(data.items()))  # Output: "[('a', 10), ('b', 20)]"
