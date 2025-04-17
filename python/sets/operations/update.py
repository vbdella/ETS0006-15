a = {1, 2}
b = {2, 3, 4}
a.update(b)
print(a)  # Output: "{1, 2, 3, 4}"

x = {"a", "b"}
x.update(["c", "d"])
print(x)  # Output: "{'a', 'b', 'd', 'c'}"

s = {10}
s.update({20, 30}, [40, 50])
print(s)  # Output: "{40, 10, 50, 20, 30}"
