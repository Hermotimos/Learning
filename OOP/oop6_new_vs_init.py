"""
Source: https://www.youtube.com/watch?v=-zsV0_QrfTw
"""



class A:
    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)


obj = A(1, 2, 3, akwarg=4)
"""

__new__:
    * creates and returns the actual object
    * receives the class as argument
    * it's a class method
    * it returns the object

__init__
    * initializes the object, ex. sets values, default values etc.
    * receives object (an instance of the class) as argument
    * it doesn't return anything, it only modifies the object (self)
    * it's only called if __new__ returns an object of the correct class

Use cases:
    * subclassing builtin immutable types
    * Singleton design pattern

"""




"""
* subclassing builtin immutable types

The role of __new__ in Python is primarely to allow programmers to subclass
immutable data types.
Subclassing a bultin type instead of wrapping it up in some Python code
may be desirable to achieve better performance: bulitins are written in C,
and have much better performance than Python code.

    * first example doesn't work, because for immutable data types' __init__
        it's too late to modify the object
    * second example modifies the object in __new__, and that works

"""

# 1
class UppercaseTuple(tuple):
    def __init__(self, iterable):
        print(f'init {iterable}')
        try:
            for i, arg in enumerate(iterable):
                self[i] = arg.upper()
        except TypeError as exc:
            print(exc)      # Error: tuples are immutable, even in init


def inheriting_immutable_uppercase_tuple_example():
    print("UPPERCASE TUPLE EXAMPLE:", UppercaseTuple(["hi", "there"]))

inheriting_immutable_uppercase_tuple_example()


# 2
class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)


def inheriting_immutable_uppercase_tuple_example():
    print("UPPERCASE TUPLE EXAMPLE:", UppercaseTuple(["hi", "there"]))

inheriting_immutable_uppercase_tuple_example()


"""
* Singleton design pattern

A singleton is class that should have at most 1 instance.
Ex. global config object, database connection.
All parts of the program have reference to the same object,
and whenever it's changed, all references get have access to the new state.


"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Here __new__ always returns an instance of the class,
        # but it's not necesserily a 'new' instance - it may already exist.
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def singleton_example():
    print("SINGLETON EXAMPLE")
    x = Singleton()
    y = Singleton()
    print(f'{x is y=}')


singleton_example()