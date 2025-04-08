keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys)
print(new_dict)  # Output: "{'a': None, 'b': None, 'c': None}"

items = ['apple', 'banana']
stock = dict.fromkeys(items, 0)
print(stock)  # Output: "{'apple': 0, 'banana': 0}"

letters = ['x', 'y']
d = dict.fromkeys(letters, [])
d['x'].append(1)
print(d)  # Output: "{'x': [1], 'y': [1]}"
