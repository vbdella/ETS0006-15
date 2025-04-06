fruits = ['apple', 'banana', 'cherry']
last = fruits.pop()
print(last)
print(fruits)  # Output: "cherry ['apple', 'banana']"

nums = [10, 20, 30]
first = nums.pop(0)
print(first)
print(nums)  # Output: "10 [20, 30]"

empty = []
# empty.pop()  # Uncommenting this will raise an IndexError
# Output: "IndexError: pop from empty list"