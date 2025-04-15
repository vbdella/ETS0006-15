a = {1, 2}
b = {2, 3}
print(a.union(b))  # Output: "{1, 2, 3}"

x = {10, 20}
y = {30}
z = {20, 40}
print(x.union(y, z))  # Output: "{40, 10, 20, 30}"

s1 = {"a", "b"}
s2 = {"b", "c"}
print(s1 | s2)  # Output: "{'a', 'b', 'c'}"
