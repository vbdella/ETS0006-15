a = {1, 2, 3, 4}
b = {2, 3}
print(a.issuperset(b))  # Output: "True"

x = {1, 2}
y = {1, 2, 3}
print(x.issuperset(y))  # Output: "False"

s = {10, 20}
print(s.issuperset(s))  # Output: "True"
