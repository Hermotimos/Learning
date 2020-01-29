"""
    This file is for learning and exercise purposes.

    Topics:
        - functions as args
        - inner functions (= nested functions)
        - returning function vs. returning function's value within another function
        - simple decorators
        - decorators: accepting args, returning values
        - __name__ of decorated function

    Sources:
        https://dbader.org/blog/python-first-class-functions
        https://www.programiz.com/python-programming/closure
        https://www.geeksforgeeks.org/python-closures/
        https://dbader.org/blog/python-decorators
        https://realpython.com/primer-on-python-decorators/
"""


# BASICS FOR UNDERSTANDING DECORATORS:
#       FUNCTIONS AS FIRST-CLASS OBJECTS
#       - like all objects in Py functions can be passed around and used as arguments
#       - functions can be defined inside other functions
#       - it's possible to return a function or it's value in the return statement of another function


# Function used as arg of another has to be used without parentheses ()
def function_using_other_functions_as_arg(another_function):
    """ use called function's __repr__ to get it's name"""
    info = another_function.__repr__()
    return info


def beep_function():
    print('beep! beeep!')


print(function_using_other_functions_as_arg(beep_function))
print(function_using_other_functions_as_arg(beep_function).split()[0])
print(function_using_other_functions_as_arg(beep_function).split()[1])
print(function_using_other_functions_as_arg(beep_function).split()[2])
print(function_using_other_functions_as_arg(beep_function).split()[3])
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
# Now this variable is a function, it is equal to first_func
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


# MORE ON DECORATORS
#        - decorators can be moved to separate file and then imported
#        - to make decorators accept arguments from decorated functions => put *args, **kwargs as arguments of wrapper
#        - to make decorators return values from decorated functions => make wrapper-function return them


def do_twice(any_function):
    def wrapper(*args, **kwargs):                   # wrapper() automatically gets *args and **kwargs from any_function
        any_function(*args, **kwargs)
        any_function(*args, **kwargs)
    return wrapper


@do_twice
def call_my_name(name):
    print(name, '!!!')


call_my_name('Mark')
print('#############################################################################################################')


def do_twice_with_return(any_function):
    def wrapper(*args, **kwargs):                   # wrapper() automatically gets *args and **kwargs from any_function
        any_function(*args, **kwargs)
        return any_function(*args, **kwargs)
    return wrapper


@do_twice_with_return
def call_my_name2(name):
    print(name, '!!!')
    return 'value returned from decorated function this is'


x = call_my_name2('Bob')
print(x)
print('#############################################################################################################')


# MORE ON DECORATORS
#        - decorated functions technically become wrappers inside decorating functions
#        - their __name__ becomes the name of the wrapper, which may be confusing
#        - to preserve their names use in-built @functools.wraps decorator from 'functools' module

print(call_my_name2.__name__)

import functools


def do_thrice(any_function):
    @functools.wraps(any_function)
    def wrapper(*args, **kwargs):                   # wrapper() automatically gets *args and **kwargs from any_function
        any_function(*args, **kwargs)
        return any_function(*args, **kwargs)
    return wrapper


@do_thrice
def call_my_name3(name):
    print(name, '!!!')
    return 'value returned from decorated function this is'


print(call_my_name3.__name__)
print('#############################################################################################################')


# EXAMPLE: DECORATOR TO VERIFY ANSWERS TO INPUT-FUNCTIONS:

def verify_decorator2(func):
    def wrapper():
        value = func()
        try:
            assert value in ('m', 'f')
            return value
        except AssertionError:
            print('Wrong value entered. Please try again.')
            return wrapper()                                  # ask_sex() becomes wrapper()
    return wrapper                                            # so return wrapper() serves to call ask_sex() recursively


@verify_decorator2
def ask_sex():
    answ = input("Enter 'm' for male or 'f' for female\n").lower()
    return answ


print(ask_sex())
