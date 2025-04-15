items = {"pen", "pencil", "eraser"}
removed = items.pop()
print(removed)
print(items)  # Output: "pen  {'pencil', 'eraser'}"

colors = {"red", "blue", "green"}
print(colors.pop())
print(colors)  # Output: "green  {'red', 'blue'}"

s = set()
# s.pop() ← Raises KeyError
# Output: "KeyError: 'pop from an empty set'"