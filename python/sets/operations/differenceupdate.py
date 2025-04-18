a = {1, 2, 3, 4}
b = {2, 3}
a.difference_update(b)
print(a)  # Output: "{1, 4}"

x = {"apple", "banana"}
y = {"cherry"}
x.difference_update(y)
print(x)  # Output: "{'apple', 'banana'}"

s = {1, 2, 3, 4, 5}
s.difference_update({1, 2}, {3})
print(s)  # Output: "{4, 5}"
