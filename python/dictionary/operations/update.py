info = {"name": "Ali"}
info.update({"age": 25, "country": "Ethiopia"})
print(info)  # Output: "{'name': 'Ali', 'age': 25, 'country': 'Ethiopia'}"

data = {"score": 90, "grade": "B"}
data.update({"grade": "A"})
print(data)  # Output: "{'score': 90, 'grade': 'A'}"

a = {"x": 1}
b = {"y": 2}
a.update(b)
print(a)  # Output: "{'x': 1, 'y': 2}"
