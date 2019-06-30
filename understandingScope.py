"""In Python, there are built-in functions of the python programming 
language, such as the print() functions.  However, most Python programs contain 
a number of custom functions that can be called as requried when the program runs.

A custom function is created using the def (definition) keyword follwed by a 
name of your choice and () parentheses.  The programmer can choose any name 
for a cuntion except the Python keywords and the name of an existing built-in 
function.  This line must end with a colon : character, then the statements to 
be executed whenever the function gets called must appear on lines below and 
be indented. Syntax of a function definition, therefore, looks like this:

def function-name():
        statements-to-be-executed
        statements-to-be-executed
        
Once the function statements have been exxecuted, program flow resumes at the 
point directly folling the function call.  This modularity is very useful in 
Python programming to isolate set routines so they can be called upon repeatedly.

To create custom functions it is necessary to understand the accessibility 
("Scope") of variables in a program:

    -Variables created inside functions cannot be referenced by statements 
    inside functinos - they have "global" scope.
    -Variables created inside functions cannot be referenced from outside the 
    function in which they have been created - these have "local" scope.
    
    The limited accessibility of local variables means that variables of the 
    same name can appear in different functions without conflict.
    
    If you want to coerce a local variable to make it accessible elsewhere, 
    it must first be declared with the Python global keyword follwed by its 
    name only.  It may subsequently be assigend a value that can be referenced
    from anywher in the program.  Wher a global variable and a local variable 
    have the same name, the function will use the local version.
    
    
-function statements must be indented from the definition line by the same 
amount so the Python interpreter can recognize the block.
-Avoid using global variables in order to prevent accidental conflict - use 
only local variables where possible.
-Variables that are not global but appear in some outer scope can be addressed 
using the nonlocal keyword.    
"""


'''Start a new python script by initializing a global variable'''
global_var = 1
''' Next, crate a function named "my_vars" to display the 
value contained within the global variable.'''
def my_vars():
    print('Global Variable:', global_var)
    '''Now, add indented statements to the function block to 
    initialize a local variable and display the value it contains'''
    local_var = 2
    print('Local variable:' , local_var)
    '''Then, add indented statements to the function block to create 
    a coerced global variable and assign an initial value'''
    global inner_var
    inner_var = 3
'''Add a statement after the function to call upon that function to execute the statements it contains'''
my_vars()
'''Finally, add a statement to display the value contained in the coerced global variable'''
print('Coerced Global:' , inner_var)

'''Run the program to see the custom function display the variable values'''
    
    