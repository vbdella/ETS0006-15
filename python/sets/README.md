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

# difference() method
The difference() method returns a new set with elements that exist in the first set but not in the others. It's useful when you want to exclude specific values or find what’s unique to one dataset. The method does not modify the original set. You can compare against multiple sets at once. It works best when identifying non-overlapping items, like missing data. The - operator is a shorthand for it.

# symmetric_difference() method
The symmetric_difference() method returns a new set with elements that are in one of the sets, but not in both. It essentially combines the sets and removes the common items. This is great when you want to highlight differences. The method is non-destructive — it keeps the original sets unchanged. You can use the ^ operator as a shortcut. It’s perfect for spotting mismatches between datasets.

# update() method
The update() method adds all elements from another set or iterable to the current set. Unlike union(), it modifies the original set in-place instead of returning a new one. It avoids duplicates, so only new unique elements are added. You can update a set with multiple iterables. This method is useful when merging or expanding datasets. It’s commonly used for building a growing collection of unique items.

# intersection_update() method
The intersection_update() method updates the original set to keep only the elements found in both sets. It is different from intersection() because it modifies the set in-place and returns None. It’s useful when you want to reduce a set to just the common values shared with another. This method can take multiple iterables. It’s commonly used in data filtering and comparisons. After this operation, the original set contains only the shared items.

# difference_update() method
The difference_update() method removes elements from the original set that also exist in the other set(s). It is like difference(), but changes the original set instead of returning a new one. This is good for filtering out unwanted or duplicate values. You can pass multiple sets or iterables to compare against. The original set is permanently changed. It's a clean and efficient way to exclude elements.

# symmetric_difference_update() method
The symmetric_difference_update() method updates the set to contain elements that are in either set but not in both. It removes the common elements and adds the unique ones. This operation modifies the set directly and returns None. It’s great when you need to highlight differences between sets. It can be visualized as a merge that deletes duplicates. Use this when comparing mismatched or changing datasets.