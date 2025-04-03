natural = [1, 2, 3]
duplicate = natural.copy()
print("natural:", natural)
print("Duplicate:", duplicate) # Output: "natural: [1, 2, 3] Duplicate: [1, 2, 3]" 

original = [10, 20, 30]
copy_list = original.copy()
copy_list.append(40)
print("Original:", original)
print("Copy:", copy_list)  # Output: "Original: [10, 20, 30] Copy: [10, 20, 30, 40]" 

main = [[1, 2], [3, 4]]
shallow_copy = main.copy()
shallow_copy[0][0] = 99
print("main:", main)
print("Shallow Copy:", shallow_copy)  # Output: "main: [[99, 2], [3, 4]] Shallow Copy: [[99, 2], [3, 4]]" 
