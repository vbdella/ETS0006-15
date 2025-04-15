# add() method
The add() method inserts a single element into a set. If the element already exists, the set remains unchanged since sets do not allow duplicates. This method is very useful when dynamically building sets from user input or other data sources. It does not return anything; it modifies the set in place. You can only add immutable types like strings, numbers, or tuples. This method is commonly used in filtering unique items or creating lookup collections.

# remove() method
The remove() method deletes a specific element from the set. If the element is not found, it raises a KeyError. It's best used when you're certain the element is in the set. Since sets are unordered, you can’t remove by position, only by value. The method modifies the set in-place and returns nothing. It’s useful in filtering or cleanup operations.

# discard() method
The discard() method also removes an element from a set but does not raise an error if the item is missing. This makes it safer than remove() when you’re not sure if the item is present. It is useful in cases where you want to clean up a set without breaking your code. Like remove(), it only works by value, not by index. It changes the set directly and doesn’t return anything. This method is great for defensive programming.

# pop() method
The pop() method removes and returns a random element from the set since sets are unordered. It’s mainly used when you want to process and reduce a set one element at a time. If the set is empty, it raises a KeyError. The element removed is arbitrary — you don’t control which item is popped. This method is useful when you want to empty a set progressively or treat it like a pool of tasks. Since sets do not support indexing, pop() is the only way to retrieve elements directly.

# union() method
The union() method returns a new set containing all unique elements from the sets being joined. It does not modify the original sets, making it safe for reuse. This is useful when merging multiple datasets or tags without duplication. You can also use the | operator as a shorthand for union(). It works with any number of sets passed as arguments. This method is a core operation in set theory and data combination tasks.

# intersection() method
The intersection() method returns a new set containing only the elements that exist in all sets. It’s used to find common data, like shared tags or matched records. The original sets are not changed. This method helps narrow down results or detect overlaps between datasets. You can also use the & operator as a shortcut. If there are no common items, it returns an empty set.