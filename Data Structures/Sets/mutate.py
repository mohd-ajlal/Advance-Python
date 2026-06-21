# Mutate in Sets

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from the set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}


# Discarding an element from the set (does not raise an error if the element is not present)
my_set.discard(10)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Clearing all elements from the set
my_set.clear()

print(my_set)  # Output: set()