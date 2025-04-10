# clear() method
The clear() method removes all elements from a list or dictionary, leaving it empty. It modifies the object in place and returns nothing (None). This method is useful when you want to reset a data structure without creating a new one. After using clear(), the structure still exists, but it contains no data. It’s often used in loops or functions when reusing the same variable. It works for both lists and dictionaries.

# copy() method
The copy() method creates a shallow copy of a dictionary or list. This means it copies the outer object, but not nested items (if any). The original and the copy are separate objects, so changing one won’t affect the other. It’s useful for preserving data before making changes. Be careful: with nested structures, inner objects will still be shared. This method is often used in data processing and testing backup scenarios.

# fromkeys() method
The fromkeys() method creates a new dictionary using a set of keys and assigns the same value to each key. It is called on the dict class, not on an instance. It’s commonly used to initialize dictionaries with default values like 0, None, or False. The keys are typically passed as a list, tuple, or any iterable. It saves time and avoids loops when creating uniform dictionaries. Be careful with mutable default values (like lists), as all keys will point to the same object.

# get() method
The get() method retrieves the value associated with a key in a dictionary. If the key exists, it returns the value just like using square brackets ([]), but if it doesn’t exist, it returns None or a custom default value. This prevents errors like KeyError when accessing non-existent keys. It’s useful when working with data that may or may not contain certain keys. You can also specify a default return value, which makes the program safer and cleaner. This method is often used in data parsing, input checking, and when working with user data.

# items() method
The items() method returns a view object that displays a list of a dictionary’s key-value pairs as tuples. It’s often used in loops to access both keys and values at the same time. This method is useful when processing, formatting, or printing complete dictionary content. The view object updates dynamically — if the dictionary changes, the view reflects those changes. It’s especially helpful in structured data tasks like exporting JSON, reporting, or building tables. It is commonly combined with loops (for key, value in dict.items():).

# keys() method
The keys() method returns a view object containing all the keys in the dictionary. This allows you to access, loop, or check for specific keys without touching their values. Like items(), the view updates if the dictionary changes. It’s useful for checking if a key exists, building dropdowns, or doing key comparisons. You can convert it to a list if you need indexing or advanced slicing. It’s one of the simplest and most frequently used dictionary tools in Python.

# pop() method
The pop() method removes a key from the dictionary and returns its value. If the key does not exist, it raises a KeyError unless a default value is provided. It’s useful when you want to extract and remove specific items at the same time. This is often used in scenarios like reducing data, transferring values, or modifying structures during iteration. It changes the original dictionary by deleting the specified key. Using pop() with a default helps make the code safer and more readable.

# popitem() method
The popitem() method removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError. It’s useful when treating dictionaries like stacks or managing the most recent additions. This method modifies the dictionary and is mostly used in order-sensitive applications (since Python 3.7+ preserves insertion order). It's ideal for undo-style behavior, temporary storage, or rolling back data. The return value is always a (key, value) tuple.

# setdefault() method
The setdefault() method looks for a key in the dictionary and returns its value if it exists. If the key is not found, it inserts the key with a default value and then returns that value. It’s useful when you want to ensure a key exists without overwriting existing values. This is often used in counting, grouping, or initializing nested structures. It helps reduce the need for multiple if statements. This method is great for working with dynamic or unknown keys.