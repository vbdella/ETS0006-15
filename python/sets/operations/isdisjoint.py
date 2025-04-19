a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # Output: "True"

x = {"apple", "banana"}
y = {"banana", "cherry"}
print(x.isdisjoint(y))  # Output: "False"

s = {1, 2, 3}
t = set()
print(s.isdisjoint(t))  # Output: "True"
