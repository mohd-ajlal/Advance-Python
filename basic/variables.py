# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10    # Integer
myfloat = 13.2576  # Float
mystr = "This is a string"  # String
mybool = True  # Boolean


print(myint)
print(mystr)

# Operators are used to perform operations on variables
print(myint * myfloat)
print(myint % 3)

another_str = "This is another string"
print(mystr + another_str)


# print(mystr + 1)  # This will cause an error because you cannot concatenate a string and an integer
# print(1 + mystr)  # This will also cause an error for the same reason


print("ajlal " * 3)

# Logical and comparison operators 
print(myint == 10)
print(myfloat != 20)
print(myint < 5 and myfloat > 25.0)
print(myint > 5 or myfloat < 10.0)  

# re-declaring a variable works
myint = "abc"
print(myint)