"""Sections of a Python script in shich it is possible to anticipate errors, 
such as those handling user input, can be enclosed in a try except block to 
handle "exception errors".  The statements to be executed are grouped in a 
try : block, and exceptions are passed to the ensuing except : block for 
handling.  Optionally, this may be followed by a finally : block containing 
statements to be executed after exceptions have been handled.

Python recognizes many built-in exceptions such as the NameError, which 
occurs when a varable name is not found, the IndexError, which occurs when 
trying to address a non-existent list index, and the ValueError, which 
occurs when a built-in operation or function receives an argument that has 
an inappropriate value.

Each exception returns a descriptive message that can, usefully, be assigned 
to a variable with the as keyword.  This can then be used to display the 
nature of the exception when it occurs. """

