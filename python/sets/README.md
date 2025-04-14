# add() method
The add() method inserts a single element into a set. If the element already exists, the set remains unchanged since sets do not allow duplicates. This method is very useful when dynamically building sets from user input or other data sources. It does not return anything; it modifies the set in place. You can only add immutable types like strings, numbers, or tuples. This method is commonly used in filtering unique items or creating lookup collections.

# remove() method
The remove() method deletes a specific element from the set. If the element is not found, it raises a KeyError. It's best used when you're certain the element is in the set. Since sets are unordered, you can’t remove by position, only by value. The method modifies the set in-place and returns nothing. It’s useful in filtering or cleanup operations.

# discard() method
The discard() method also removes an element from a set but does not raise an error if the item is missing. This makes it safer than remove() when you’re not sure if the item is present. It is useful in cases where you want to clean up a set without breaking your code. Like remove(), it only works by value, not by index. It changes the set directly and doesn’t return anything. This method is great for defensive programming.