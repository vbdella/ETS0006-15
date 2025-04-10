data = {"lang": "Python"}
print(data.setdefault("lang", "Java"))
print(data)  # Output: "Python  {'lang': 'Python'}"

info = {}
info.setdefault("country", "Ethiopia")
print(info)  # Output: "{'country': 'Ethiopia'}"

counter = {}
for char in "aab":
    counter.setdefault(char, 0)
    counter[char] += 1
print(counter)  # Output: "{'a': 2, 'b': 1}"
