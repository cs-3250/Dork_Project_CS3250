numbers = [5,2,1,7,4]
print((numbers), (" Here is the list of numbers stored inside the variable"))

#if we wanted to check the existance of a value in the list
#this should return a boolean value because it wont throw an error, so it safer to use
print((50 in numbers), ("       <-- This checks for the existance of 50 in the list"))

# append means add new item to the list
numbers.append(20)  
print((numbers),(" <-- this appended the number 20 to the end of the list"))

#this is how to insert a new value into the list which is placed at the beginning of the list
numbers.insert(0,10)
print((numbers), (" <-- this inserts 10 and index 0"))

#this is how to remove an item from the list
numbers.remove(5)
print((numbers), (" <-- this removed 5 from the list"))

#this returns the occurance of the item at the index
numbers.index(2)
print((numbers.index(2)), (" <-- this is number stored in index 2"))

#this removes the last item in the list
numbers.pop()
print((numbers), ("as you can see 20 has been removed from the list when the pop method is used"))

#this counts the number of times 6 appears in the list
numbers.append(6)
numbers.append(6)
print(numbers.count(6), " <-- This counts how many times 6 appears in the list")

#this is how to clear all items in the list
numbers.clear() #doesn't need a value   
print((numbers), ("this is where the numbers were cleared"))

print()

numbers = [5,2,1,7,4]
print((numbers), ("  Here is the orginal list again."))
 
#this method sorts all of the values in the list in order
numbers.sort()
print((numbers), ("  Here, the numbers are sorted with respect to their value."))
numbers.reverse()
print((numbers), ("  Here they are in reverse order"))

#the copy method creates 2 independant lists
numbers2 = numbers.copy()
numbers.append(10)
# numbers2 isn't going to show the number 10 in the list value 
# because we appended goes to the numbers variable.
print((numbers2), ("  This is the copied list")) 
print((numbers), ("  This is the orignal copy of the list"))

print()

#to remove the duplicates
numbers = [2,2,4,6,3,4,6,1] #here we insert new values for the numbers variable
print((numbers), ("  Here are a new set of numbers with duplicate numbers"))
unique =[] #next we make a new empty list
for number in numbers: #the loop finds the numbers that commonly appear in the list
    if number not in unique:
        unique.append(number) #unique gets appended with the values in the numbers list which is basically copying.
print((unique), ("  And now, here is the list with the duplicates removed")) # the statement should reflect that the duplicates are removed.




