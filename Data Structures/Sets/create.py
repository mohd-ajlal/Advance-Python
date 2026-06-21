# SETS in Python
# A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements after creation. They are defined using curly braces {} or the set() constructor. Sets are commonly used for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference.

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Accessing elements in a set
# Note: Sets do not support indexing or slicing, so you cannot access elements by their position. However, you can iterate through the set using a loop.
for element in my_set:
    print(element)

print(my_set)  # Output: {1, 2, 3, 4, 5}