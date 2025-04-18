a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # Output: "{2, 3}"

x = {10, 20}
y = {30, 40}
x.intersection_update(y)
print(x)  # Output: "set()"

s = {1, 2, 3, 4}
s.intersection_update({2, 3, 4}, {3, 4})
print(s)  # Output: "{3, 4}"
