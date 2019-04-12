# BASICS FOR UNDERSTANDING DECORATORS:
#       FUNCTIONS AS FIRST-CLASS OBJECTS
#       - like all objects in Py functions can be passed around and used as arguments
#       - functions can be defined inside other functions
#       - it's possible to return a function or it's value in the return of another function


# Function used as arg of another has to be used without parentheses ()
def function_using_other_functions_as_arg(another_function):
    """ use called function's __repr__ to get it's name"""
    info = another_function.__repr__()
    return info


def beep_function():
    print('beep! beeep!')


print(function_using_other_functions_as_arg(beep_function))
print(function_using_other_functions_as_arg(beep_function).split()[1])
print(function_using_other_functions_as_arg(function_using_other_functions_as_arg))
print(function_using_other_functions_as_arg(print))
print('#############################################################################################################')


# The order in which inner functions are defined doesn't matter => the order in which they're called does
def function_with_inner_functions():
    def first_func():
        print('ONE')

    def second_func():
        print('TWO')

    print('function_with_inner_functions START')
    second_func()
    first_func()
    print('function_with_inner_functions END')


function_with_inner_functions()
print('#############################################################################################################')


# To return function from inside another function, we have to put it in return statement without parentheses ()
def function_with_inner_functions(num):
    def first_func():
        print('ONE!')
        return 1

    def second_func():
        print('TWO!')
        return 2

    if num == 1:
        return first_func          # NO PARENTHESES HERE => returns reference to the function
    if num == 2:
        return second_func         # NO PARENTHESES HERE => returns reference to the function
    else:
        return first_func() + second_func()    # IF PARENTHESES => returns value of the function


# These return differently based on parentheses presence above
print(function_with_inner_functions(1))
print(function_with_inner_functions(2))
print(function_with_inner_functions('else'))
print()


# It's possible to assign reference to a function to a variable:
variable = function_with_inner_functions(1)
var2 = function_with_inner_functions(2)
# Now whis variable is a function, specifically its equal to first_func
variable()
var2()

# This can't be done below, as 'else' block of function_with_inner_functions returns values, not references fo functions
print()
var3 = function_with_inner_functions('sth else')
# var3() - this would cause error
print(var3)
print('#############################################################################################################')


# SIMPLE DECORATORS:
#           Decorator is a function that accepts another function as argument and modifies it's behavior
#           Decorator wraps a function in some more code.
#           Decorated function becomes an argument of decorating function

def decorator_function(decorated_function):
    def wrapper_func():
        print('Something happens before decorated function is called')
        decorated_function()
        print('Something happens after decorated function is called')
    return wrapper_func                                                     # NO PARENTHESES HERE after wrapper_func


def say_whee():
    print('Wheeee!')


whee = decorator_function(say_whee)                                         # NO PARENTHESES HERE after say_whee
whee()
print('#############################################################################################################')


# The above statements can be expressed in a more concise way with '@' operator
def decorator_function(decorated_function):
    def wrapper_func():
        print('Something happens before decorated function is called')
        decorated_function()
        print('Something happens after decorated function is called')
    return wrapper_func                                                     # NO PARENTHESES HERE after wrapper_func


@decorator_function                             # thus say_whee() is doomed to always be arg of decorator_function()
def say_whee():
    print('Wheeee, here "@" is used!')


say_whee()
print('#############################################################################################################')