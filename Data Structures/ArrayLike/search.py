# Search array 

list = [1, 2, 3, 4, 5]
item_to_find = 3

if item_to_find in list:
    print(f"{item_to_find} found in the list.")
else:
    print(f"{item_to_find} not found in the list.")


# Built-in function to find the index of an item

try:
    index = list.index(item_to_find)
    print(f"Index of {item_to_find} is {index}.")
except ValueError:
    print(f"{item_to_find} is not in the list.")

