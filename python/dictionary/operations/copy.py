a = [1, 2, 3]
b = a.copy()
a.append(4)
print(a)
print(b)  # Output: "[1, 2, 3, 4]  [1, 2, 3]"

info = {"name": "Sara"}
copy_info = info.copy()
info["age"] = 25
print(info)
print(copy_info)  # Output: "{'name': 'Sara', 'age': 25}  {'name': 'Sara'}"

x = {"a": 1}
y = x.copy()
print(x is y)  # Output: "False"
