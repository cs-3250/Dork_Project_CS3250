"""
When a Python function is called, it executes the statements it contains 
and may return any value specified to the return keyword.  After the 
function ends, control returns to the caller and the state of the function 
is not retained.  When the function is next called it will process its 
statements from start to finish once more.

A python generator, on the other hand, is a special function that returns 
a "generator object" to the caller rather than a data values.  This, 
effectively, retains the state of the function when it was last called, 
so it will continue from that point when next called.

Generator functions are produced by definition just like regular functions, 
but contain a "yield" statement.  This begins with the Python yield keyword 
and specifies the generator object to be returned to the caller.  When the 
yield statement gets executed the state of the generator object is frozen, 
and the current value in it's "expression list" is retained.  The generator 
object returned by the yeild statment can be conveniently assigned to a 
variable Python's built-in next() function can then specify that variable 
name within it's parentheses to continue execution of the function from the 
point at which it was frozen - exactly as if the yield statement were just 
another external call.

Repeatedly calling the generator object with the next() function continues 
execution of the function until it raises and exception.  This can be 
avoided by enclosing the yeild statment within an infinite loop so it will 
return successive values on each iteration.  For example, to yeild an 
incremented value on each call:
"""

def incrementer():
    i = 1
    while True:
        yield i
        i += 1
inc = incrementer()

print( next(inc))
print( next(inc))
print( next(inc))

"""
These calls display the interger value 1, then 2, then 3.

Perhaps more usefully, the generator object can be referenced from a loop 
to successively iterate through values.
"""

####################################################################################
"""Start by defining a function that begins by initializing two variables 
with an integer of one."""
def fibonacci_generator():
    a = b = 1
    """Next, in the function body insert an indented infinite loop to 
    yield the addition of two previous values.    """
    while True:
        yield a
        a, b = b, a + b
"""Now, assign the returned generator object to a variable."""
fib = fibonacci_generator()
"""Finally, add a loop to successively call the generator fucntion and 
display its value on each iteration."""
for i in fib:
    if i > 100:
        break
    else:
        print( 'Generated:' , i)

"""Run to see the loop display increasing generated values."""