# Tuples are used to store a list of items.
# Also, similar to lists.
# Unlike lists, we cannot modify them.
# You cannot add or remove new items.
    # also called immutable items.
        # cannot mutate or change.
# Don't have the ability to use pop, clear, insert.
# Can only use the two methods:
    # count - used to count the number of occurances of an item.
    # index - used to find the FIRST occurance of an item.
# We use brackets[] to define lists and parenthesis() to define tuples.

# Note: If you want to create a list of items and makes sure that no where in your program 
# you accidentally modify that list, then it's better to use a tuple

numbers = (1,2,3) # <-- this is how a tuple is defined
print((numbers[0]), (" This is the number at index 0"))

# if we try to change the first item we will get an error
# numbers[0] = 10
# print(numbers[0])

#---Unpacking---

# A better approach to writing complex code is to get the values and store them in spearate variables.
coordinates = (1, 2, 3) # Imagine that these are the coordinates (x,y,z) and maybe we want to use them in a complex expression.
# x = coordinates = [0]
# y = coordinates = [1]
# z = coordinates = [2]

# We can set x y z to a tuple
# This takes the first item 1 in this tuple and assigns it to the it to the first variable x.
# Then it will look at the second item in the tuple 2 and assign it to the y variable.
x,y,z = coordinates  # This is a shorthand to achieve the same result from the example above.
print(x)
print(y)
print(z)