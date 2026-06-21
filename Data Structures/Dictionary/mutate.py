# Mutate 

my_dict = {
    "name": "Mohd Ajlal",
    "age": 22,
    "city": "Lucknow"
}

# Mutate the dictionary
my_dict["age"] = 23  # Update the age

print(my_dict)  # Output: {'name': 'Mohd Ajlal', 'age': 23, 'city': 'Lucknow'}

# add a new key-value pair
my_dict["country"] = "India"
print(my_dict)  # Output: {'name': 'Mohd Ajlal', 'age': 23, 'city': 'Lucknow', 'country': 'India'}

# delete a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Mohd Ajlal', 'age': 23, 'country': 'India'}

# pop() method to remove a key-value pair and return the value
age = my_dict.pop("age")
print(age)  # Output: 23
print(my_dict)  # Output: {'name': 'Mohd Ajlal', 'country': 'India'}