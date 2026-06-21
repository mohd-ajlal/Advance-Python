# Handle missing keys in a dictionary
my_dict = {
    "name": "Mohd Ajlal",
    "age": 22,
    "city": "Lucknow"
}

# Accessing a key that doesn't exist using get() method
print(my_dict.get("country", "Key not found"))  # Output: Key not found

# Accessing a key that doesn't exist using try-except block
try:
    print(my_dict["country"])
except KeyError:
    print("Key not found")  # Output: Key not found