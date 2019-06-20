print('\n\n\n')

""" Start by defining a function to accept three arguments 
that will print out ther passed in values"""
def echo(user, lang, sys):
    print('user:',user,'Language:',lang, 'Platfor:',sys)

""" Next, call the function passing string values to the 
function arguments in the order they appear"""    
echo('Mike','Python','Windows')

""" Now, call the function passing string values to the 
function arguments by specifying the argument names"""
echo(lang = 'Python',sys='MacOS',user='Anne')

""" Then, define another function to accept two arguments 
with default values that will print out argument values"""
def mirror(user='Carole',lang = 'Python'):
    print('\nUser:',user,'Language:',lang)

""" Finally, add statements to call the second function 
both using a overriding default values"""
mirror()
mirror(lang = 'Java')
mirror( user = 'Tony')
mirror('Susan','C++')