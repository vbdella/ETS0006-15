# clear() method
The clear() method removes all elements from a list or dictionary, leaving it empty. It modifies the object in place and returns nothing (None). This method is useful when you want to reset a data structure without creating a new one. After using clear(), the structure still exists, but it contains no data. It’s often used in loops or functions when reusing the same variable. It works for both lists and dictionaries.

# copy() method
The copy() method creates a shallow copy of a dictionary or list. This means it copies the outer object, but not nested items (if any). The original and the copy are separate objects, so changing one won’t affect the other. It’s useful for preserving data before making changes. Be careful: with nested structures, inner objects will still be shared. This method is often used in data processing and testing backup scenarios.

# fromkeys() method
The fromkeys() method creates a new dictionary using a set of keys and assigns the same value to each key. It is called on the dict class, not on an instance. It’s commonly used to initialize dictionaries with default values like 0, None, or False. The keys are typically passed as a list, tuple, or any iterable. It saves time and avoids loops when creating uniform dictionaries. Be careful with mutable default values (like lists), as all keys will point to the same object.