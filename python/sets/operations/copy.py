colors = {"red", "green", "blue"}
backup = colors.copy()
print(backup)  # Output: "{'red', 'green', 'blue'}"

a = {1, 2, 3}
b = a.copy()
b.add(4)
print(a)
print(b)  # Output: "{1, 2, 3}  {1, 2, 3, 4}"

numbers = {10, 20}
backup_numbers = numbers.copy()
numbers.clear()
print(backup_numbers)  # Output: "{10, 20}"
