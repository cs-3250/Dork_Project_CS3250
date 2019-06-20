print('\n\n\n')
""" First, initialize a global variable"""
global_var = 1

""" Next, create function named "my_vars" to display the value contained 
within the global variable """
def my_vars():
    print('Global Variable:' , global_var)
    
    """ Add indented statements to the function block to initialize 
    a local variable and display the value it contains """
    local_var = 2
    print('Local variable:' , local_var)
    
    """ Add statements to the function block to create a coerced global 
    variable and assign an initial value"""
    global inner_var
    inner_var = 3
    
    """add a statement after the function to call upon that function to 
    execute the statements it contains"""
my_vars()
print('Coerced Global:' , inner_var)