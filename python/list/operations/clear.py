numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)  # Output: "[]"

data = [5, 10, 15]
print("Before clearing:", data)
data.clear()
print("After clearing:", data)  # Output: "Before clearing: [5, 10, 15] After clearing: []"

data1 = [1, 2, 3]
backup = data1  # Both variables point to the same list
data1.clear()
print("Data:", data1)
print("Backup:", backup)  # Also empty because both reference the same list
# Output: "Data: [] Backup: []"
