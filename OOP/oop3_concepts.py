
"""
Key concepts in OOP:
1) Abstraction
2) Encapsulation
3) Inheritance

also:
4) Composition
5) Polymorphism

"""


"""
ABSTRACTION
-----------
Abstraction is a process of handling complexity by hiding unnecessary information
(i.e. internal details of an application) from the outer world.
It enables other programmers to implement even more complex logic on top of the provided abstraction
without understanding or even thinking about all the hidden background/back-end complexity.

Abstraction is achieved through various mechanisms:
    * Encapsulation (organizing code into classes)
    * Inheritance   (reusing classes)
    * Polymorphism  (objects that are different can be used in a unified way)
    * Composition   (objects can be composed of other objects)

Abstraction is essential in programming because it allows developers to manage complexity
and build systems that are easy to use and understand.
By hiding the details of a system, programmers can focus on designing the essential features
and providing a clean and intuitive interface for users to interact with.


Example in Python: abstraction can be achieved through the use of abstract classes and interfaces,
which are defined using the 'abc' module:
    * an abstract class subclasses ABC class from 'abc' module
    * an abstract method is decorated with 'abstractmethod' decorator from 'abc' module

An abstract class that contains only abstract methods is an interface.
"""

# Interface - example

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


"""
ENCAPSULATION
-------------

Encapsulation is a fundamental concept in Object-Oriented Programming (OOP)
that involves bundling data and functions together into a single unit, called a class.
The main idea is to hide the implementation details of a class from the outside world
and provide a clean and consistent interface for interacting with the class.

In Python, encapsulation is achieved through the use of access modifiers,
which determine the visibility of data and functions within a class.
Python does not have true access modifiers like other OOP languages,
but it provides conventions for indicating the level of visibility of a class member.

    * Public members:
        members without underscores before their names,
        can be accessed from anywhere.
    * Protected members:
        members with a single underscore (_) before their names,
        can only be accessed from within the class or its subclasses;
        but no error raised otherwise.
    * Private members:
        members that have double underscores (__) before their names,
        can only be accessed from within the class;
        exception is raised otherwise.

"""

# Encapsulation - example
# BankAccount class  encapsulates the details of a bank account, such as the account number and balance,
# and exposes only the relevant behavior to the user, such as depositing, withdrawing, and getting the balance.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number      # private member
        self._somestuff = "can be accessed"         # protected member
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


account = BankAccount(1122334455, 1500)
print(account.balance)
account.withdraw(111)
print(account.balance)

try:
    print(account.__account_number)
except AttributeError:
    print("Raised exception: AttributeError: 'BankAccount' object has no attribute '__account_number'")
print(account._somestuff)






"""
INHERITANCE
-----------

Inheritance is a core concept in Object-Oriented Programming (OOP).
Inheritance that allows a class to inherit the properties and methods of another class.
    * the class that is inherited from: "parent" or "superclass",
    * the class that inherits from it: "child" or "subclass".

Inheritance allows subclasses to reuse code from their superclass, which:
    1) reduces code duplication (DRY)
    2) improves the maintainability of software

Ad 1)
By inheriting properties and methods from a superclass,
a subclass can extend or modify its behavior without having to rewrite everything from scratch.

"""


# Code reuse - example
# Both __init__ and __str__ methods are reused by subclasses

class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"({self.__class__.__name__}: {self.a}, {self.b})"

    def do_its_thing(self):
        raise NotImplementedError

class ChildAdd(ParentClass):
    def do_its_thing(self):
        return self.a + self.b

class ChildMultiply(ParentClass):
    def do_its_thing(self):
        return self.a * self.b


a1 = ChildAdd(2, 5)
a2 = ChildAdd(2, 6)
print(a1.do_its_thing())
print(a2.do_its_thing())


b1 = ChildMultiply(2, 5)
b2 = ChildMultiply(2, 6)
print(b1.do_its_thing())
print(b2.do_its_thing())

print(a1)
print(b1)

"""
Inheritance - hints
    * every class (=type) in Python is a subclass of 'object'.
    * if a subclass A should inherit only some methods from the superclass B,
      this is a sign, that a third class C should be created and those methods
      should be placed in that class C and then inherited by A and B.


"""




"""
COMPOSITION
-----------

Composition is another fundamental concept in object-oriented programming
that allows developers to reuse code and create more complex and flexible software systems.

Composition is a programming technique where a class contains an instance of another class
as one of its member variables. This means that the class is composed of other objects.

Composition can be achieved in two ways:
    1) class composition
    2) passing objects to constructors

"""


# Ad 1) composition via class composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()          # class composition

    def start(self):
        self.engine.start()


car = Car()
car.start()  # output: Engine started



# Ad 2) composition via passing objects to constructors
class Engine:
    def start(self):
        print(f"Engine started.")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


my_engine = Engine()
my_car = Car(engine=my_engine)
my_car.start()





"""
POLYMORPHISM
------------

Polymorphism is one of the fundamental concepts in object-oriented programming (OOP)
that allows objects to have multiple forms or behaviors.
It refers to the ability of an object or method to take on multiple forms or behaviors
depending on the context in which it is used.

There are two types of polymorphism in OOP:

1) Compile-time polymorphism (aka static polymorphism or method overloading):
    Allows you to define multiple methods with the same name in a class,
    but with different parameters or argument types.
    The compiler determines which method to call based on the number and types of arguments passed to the method.

    Python does not support function/method overloading in the traditional sense
    as in languages like C++ or Java, where multiple functions with the same name can be defined
    with different argument types or number of arguments.
    However, we can still achieve a similar effect in Python - example below.

2) Runtime polymorphism (aka dynamic polymorphism or method overriding):
    Allows you to define a method in a subclass
    that has the same name and signature as a method in its superclass.
    When the method is called on an object of the subclass,
    the overridden method in the subclass is executed instead of the method in the superclass.

Polymorphism is a powerful concept in OOP because it allows you to write more flexible and extensible code.
By using polymorphism, you can create code that works with different types of objects,
as long as they implement the same interface or inherit from the same base class.
This makes it easier to write reusable code and to write code that can adapt to changing requirements over time.


"""

# Method overriding (runtime polymorphism)

class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_its_thing(self):
        raise NotImplementedError

class ChildAdd(ParentClass):
    def do_its_thing(self):
        return self.a + self.b

class ChildMultiply(ParentClass):
    def do_its_thing(self):
        return self.a * self.b


a1 = ChildAdd(2, 5)
print(a1.do_its_thing())
b1 = ChildMultiply(2, 5)
print(b1.do_its_thing())




# Something like compile-time polymorphism, but without method overloading

class Calculator:
    def add(self, x, y=0, z=None):
        if z is None:
            return x + y
        else:
            return x + y + z


calculator = Calculator()
print(calculator.add(2, 3))
print(calculator.add(2, 3, 4))