list = [1, 2, 3, 4, 5]
print(list)

print(list[0])  # Accessing the first element
print(list[1])  # Accessing the second element

# accessing using negative indexing
print(list[-1])  # Accessing the last element


sum = 0
for i in list:
    sum += i
print("Sum of all elements in the list:", sum)