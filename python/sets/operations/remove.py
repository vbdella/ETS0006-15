items = {"pen", "pencil", "eraser"}
items.remove("pencil")
print(items)  # Output: "{'pen', 'eraser'}"

tools = {"hammer", "wrench"}
# tools.remove("screwdriver")  ← Raises KeyError
# Output: "KeyError: 'screwdriver'"

nums = {10, 20, 30}
nums.remove(20)
print(nums)  # Output: "{10, 30}"
