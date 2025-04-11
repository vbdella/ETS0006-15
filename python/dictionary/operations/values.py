user = {"name": "Sara", "age": 21}
print(user.values())  # Output: "dict_values(['Sara', 21])"

marks = {"math": 90, "science": 85}
for value in marks.values():
    print(value)  # Output: "90  85"

d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
print(values)  # Output: "[1, 2, 3]"