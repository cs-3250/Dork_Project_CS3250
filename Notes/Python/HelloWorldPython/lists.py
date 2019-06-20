names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1]) #prints the last name in the index
print(names[-2]) #prints the second item in the list
print(names[2:]) #prints range from Mosh to Mary
print(names[2:4]) #prints range index 2 to index 4
print()

#if you want to change the name at a specific index
names[0] = 'jon'
print(names)
print()

#Here is a random list of numbers
"""This is going to loop through from the first index to the last 
 ,comparing the numbers and returning the highest value"""
numbers = [3,6, 2, 4, 8, 10]
max = numbers[0] #to find the largest number in the variable
for number in numbers:
    if number > max:
        max = number
print(max)  

"""Try tabbing the print 1 time and run the program."""
"""  Pay attention to the behavior."""

print()

fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append("orange")
print(fruits)


print()


quarter = ['January', 'February', 'March']
print('First Month :' , quarter[0])
print( 'Second Month :' , quarter[1])
print( 'Third Month :' , quarter[2])

coords = [[1,2,3] , [4,5,6]]
print('\nTop Left 0,0 :' , coords[0][0])
print('\nBottom Right 1,2 :' , coords[1][2])

print('\nFirst Month First Letter :', quarter[1][2]) 

print('\nSecond Month First Letter :' , quarter[1][0])