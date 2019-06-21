print('\n\n\n\n\n')

""" Start your debugger!!!!  Step over each function and read along with the comments
to observe the behavior of this program."""

""" In python, a named function is created using the def keyword to specify a function 
name, which can be use to call that function  at any time in the program to execute the 
statements it contains. Optionally, the named function can return a value to the caller.

Python also allows an anonymous un-named function to be created using the lambda keyword.  
An anonymous function ma only ontain a single expression that must always return a value.

Unlike the usual creation of a function with the def keyword, the creation of a function
with the lambda keyword returns a "function object".  This can be assigned to a variable, 
which can then be used to reference ("call back") the function at any time in the program 
to execute the expression it contains.  The lambda keyword, therefore, offers the programmer 
an alternative syntax for the reation of a function. For example:"""
def square(x):
    return x **2
""" can alternatively be written more succinctly as..."""
square = lambda x : x **2

""" In either case, the call square(5) returns the result 25 by passing in an interger 
argument to the function.  Note that the lambda keyword is followed by an argument without 
parentheses, and the specified expression does not require the return keyword as all 
functions created lambda mush implicityly return a value.

While the lambda keyword offers an alternative way to create a function it is mostly used 
to embed a function within the code.  For instance, callbacks are frequently coded as inline 
lambda expressions embedded directly in a caller's arguments list - instead of being 
defined with the def keyword elswhere in the program and reference by name 
For example:

def function_1: statements-to-be-executed
def function_2: statements-to-be-executed

can alternatively be written more succinctly as...

calbacks = [lambda : expression, lambda : expression]
"""



""" Define threee functions to return a passed argument raised to various powers"""
def function_1(x): return x **2
def function_2(x): return x **3
def function_3(x): return x **4
""" Next, add a statement to create a list of callbacks to each of the functions 
by referencing their names"""
callbacks = [function_1, function_2, function_3]
""" Now, display a heading and the result of passing a value to each of 
the named functions"""
print('\nNamed Functions:')
for function in callbacks: print('Result:', function(3))
""" Then, add a statement to create a list of callbacks to inline annonymous 
functions that return a passed argument raised to various power."""
callbacks = \
[lambda x : x ** 2, lambda x : x ** 3, lambda x : x **4]
""" Finally, display a heading and the result of passing a value to each 
of the anonymous functions."""
print ('\nAnonymous Functions:"')
for function in callbacks : print('Result:', function(3))
