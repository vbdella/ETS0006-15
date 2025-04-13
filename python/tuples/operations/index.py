numbers = (10, 20, 30, 40)
print(numbers.index(30))  # Output: "2"

data = (5, 10, 5, 20)
print(data.index(5))  # Output: "0"

t = (1, 2, 3)
# print(t.index(4))  ← Raises error
# Output: "ValueError: tuple.index(x): x not in tuple"