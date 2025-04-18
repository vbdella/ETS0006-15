a = {1, 2, 3}
b = {3, 4}
a.symmetric_difference_update(b)
print(a)  # Output: "{1, 2, 4}"

x = {"red", "blue"}
y = {"blue", "green"}
x.symmetric_difference_update(y)
print(x)  # Output: "{'red', 'green'}"

s = {10, 20, 30}
s.symmetric_difference_update({20, 40})
print(s)  # Output: "{10, 30, 40}"
