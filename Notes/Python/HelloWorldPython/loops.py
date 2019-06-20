i =1
while i < 4:
    print('\nOuter Loop Iteration:', i)
    i += 1
    j = 1
    while j < 4:
        print('\tInner Loop Iteration:', j)
        j +=1
        
######################################################################
# For Loops#
######################################################################
print('\n\n')

""" Start by initializing a list, a tuple, and a dictionary. """
chars = [' A ', ' B ' , ' C ']
fruit = {'Apple', 'Banana', 'Cherry'}
dict = {'name': 'Mike', 'ref':'Python', 'sys': 'Win'}

print(chars)
print(fruit)
print(dict)

""" Add statements to display all list element values and their relative index number. """
print('\nElements:\t' , end = '')

""" Next, add statements to display all list element values """
for item in chars:
    print(item, end ='')
    
""" Add statements that list element values and their relative index number. """     
print('\nEnumerated:\t' , end ='')
for item in enumerate(chars):
        print(item, end='')
        
""" Then, add statements to display all list and tuple elements """       
print('\nZipped:\t', end = '')
for item in zip(chars, fruit):
    print(item, end='')

""" Finally, add statements to display all dictionary key names and associated 
element values """    
print('\nParied:')
for key, value in dict.items():
    print(key, '=', value)
    
""" Follow the output in the debug and break at the beginning. """