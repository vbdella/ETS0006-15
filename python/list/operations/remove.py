colors = ['red', 'blue', 'green']
colors.remove('blue')
print(colors)  # Output: "['red', 'green']"

nums = [1, 2, 3, 2, 4]
nums.remove(2)
print(nums)  # Output: "[1, 3, 2, 4]"

animals = ['cat', 'dog']
# animals.remove('lion')  # Uncommenting this will raise a ValueError
# Output: "ValueError: list.remove(x): x not in list"