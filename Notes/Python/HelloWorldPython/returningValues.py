print('\n\n\n\n\n\n\n')
""" Python's built-in str() function, which returns a string representation of the value 
specified as it's arguments by the caller, custom functions can also return a value to 
their caller by using the python return keyword to specify a value to 
be returned.  For example, to return to the caller the total of adding two specified 
argument values, like this: """
def sum(a,b):
    return a +b
""" The returned result may be assigned to a variable by the caller for subsequent use 
by the program, like this: """
total = sum(8,4)
print('Eight Plus Four Is: ', total)
""" Or the returned result may be used directly "in-line", like this: """
print('Eight Plus Four is:' , sum(8,4))

""" Typically, a return statement will apear at the very end of a function block to 
return the final result of executing all statements contained in that function.

A return statement may, however, appear earlier in the function block to halt 
execution of all subsequent statemtns in that block. This is immediately resumes 
execution of the program and returned to the caller or the value may be omitted.  
Where no value is specified, a default value of None is assumed.
Typically, a return statement will appear at the very end of a function block to
return the final result of executing all statements contained in that function.  
Typically, this is used to halt execution of the function statements after a 
conditional test is found to be False.  For example, where a passed argument value 
is below a specified number: """

def sum(a,b):
    if a < 5:
        return
    return a + b
""" In this case, the function will return the default value None when the first
passed argument value is below five and the final statement will not be executed.

Wher the function is to perform arithmetic, user input can be validated for 
interger values with the build-in isdigit() function."""

######################################################################################
    
""" Initialize a variable with user input of an interger value ofr manipulation """
num = input('Enter An Interger: ')

""" Next, add a funciton definintion that accepts a single argument value to be 
passed from the caller"""
def sqare(num):
    """ Insert into the function block an indented statement to validate the 
    passed value as an interger or halt further execution of the function's statements"""
    if not num.isdigit():
        return 'invalid Entry'
    """ Then, add indented statements to cast the passed value as an int data type 
    then return the sum of squaring that value to the caller"""    
    num = int(num)
    return num * num
""" Finally, add a statement to output a string and the returned value from the 
function call"""
print(num, 'Squared is:', square(num))