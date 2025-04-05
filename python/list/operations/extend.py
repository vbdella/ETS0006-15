list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)  # Output: "[1, 2, 3, 4, 5]"

chars = ['a', 'b']
chars.extend("cd")
print(chars)  # Output: "['a', 'b', 'c', 'd']"

nums = [1, 2]
nums.extend((3, 4))
print(nums)  # Output: "[1, 2, 3, 4]"
