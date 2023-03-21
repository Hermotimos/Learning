# TODO: dependency injection: https://youtu.be/-ghD-XjjO2g?t=622
# TODO: abstract class (ABC), abstract methods



# -----------------------------------------------------------------------------
# [1] basics


class Employee:
    # create class, every class is a type

    def __init__(self, first, last, pay):
        # define instance variables (attributes) of Employee
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # define regular method of Employee
    def fullname(self):
        return f'{self.first} {self.last}'

    # override regular method of Employee
    def __str__(self) -> str:
        return f"{self.fullname()} / {self.email}"


# create instances of a class
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print('[1]')
print(emp_1)
print(emp_2)
print(emp_1.fullname())
print(Employee.fullname(emp_1))  # to call method from the class, feed instance as 'self'
print()



# -----------------------------------------------------------------------------
# [2] class variables


class Employee:
    # class variables
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variables (attributes )
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # increment class variable whenever an instance is created
        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # increment instance attribute based on class attribute
        self.pay = int(self.pay * self.raise_amount)


# create instances of a class
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print('[2]')

print(Employee, Employee.raise_amount)
print(emp_1, emp_1.raise_amount)
# This will print class attribute as if it was an attribute of the instance
# Because if an instance does not have an attr, Python searches in its class and its parent classes
print()

print(emp_1, emp_1.raise_amount)
print(emp_2, emp_2.raise_amount)
print(emp_1.__dict__)               # no 'raise_amount' in instance's namespace
emp_1.raise_amount = 666            # creates an instance attribute on emp_1
print(emp_1.__dict__)               # now 'raise_amount' present in the namespace
print(emp_1, emp_1.raise_amount)
print(emp_2, emp_2.raise_amount)
print()



# -----------------------------------------------------------------------------
# [3] class methods


class Employee:
    employee_count = 0
    raise_amount = 1.04

    # constructor of class instances
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # define a class method (vs regular or static methods)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor of class instances
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)

# it's possible to set class variable from instance, but it's not practiced
emp_1.set_raise_amount(1.08)
print(Employee.raise_amount)

print('[3]')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()


# Use alternative constructor to instantiate Employee class, instead of split()
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1)
print()



# -----------------------------------------------------------------------------
# [4] static methods


class Employee:
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return f'{self.first} {self.last}'

    # regular methods pass 'self' as the first argument
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class methods pass 'cls' as the first argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods only use regular arguments, they don't use 'self' or 'cls'
    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amount(1.05)

print('[4]')

import datetime
mydate = datetime.date(2023, 3, 14)
print(Employee.isworkday(mydate))
print()



# -----------------------------------------------------------------------------
# [5] subclasses


class Employee:
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    # Only inherits, adds no new attributes or methods
    # But those will be accessible from the parent
    pass


dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

print('[5]')
print(dev_1)
print(dev_2)
print()

print(help(Developer))  # prints MRO, methods and attributes
# print(help(dev_1))    # does the same


class Developer(Employee):
    # Overrides parent class attribute
    raise_amount = 1.1
    print()
    print('Developer class redefined, raise amount 10%')

# Now after the override of Developer class with new 'raise_amount' values
# we would expect that this 'raise_amount' will be applied...
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
# So here the 'old' raise_amount was applied, why?
# Because dev_1 is an instance of the 'old' Developer class, where raise_amount = 1.04
print()

# Recreate dev_1 and the new value of 'raise_amount' applies
dev_1 = Developer('Corey', 'Schafer', 50000)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print()



# -----------------------------------------------------------------------------
# [6] subclasses 2


class Employee:
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    raise_amount = 1.1

    # to extend parent class method use ==> super().__init__()
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)      # use superclass' __init__ to do its job
        self.language = language                # and then so sth new

    # to override parent class method omit the super().__init__() call
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, lang = emp_str.split('-')
        return cls(first, last, pay, lang)


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
dev_3 = Developer.from_string("Mock-Employee-77777-Kobol")

print('[6]')
print(help(Developer))
print(dev_1, dev_1.language)
print(dev_2, dev_2.language)
print(dev_3, dev_3.language)
print()



# -----------------------------------------------------------------------------
# [7] dunder methods


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def __str__(self) -> str:
        return self.fullname()

    # declare a dunder method on a class
    def __len__(self) -> str:
        return len(self.fullname())

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Corey', 'Schafer')

print('[7]')

# builtins
print(1 + 2)
print(int.__add__(1, 2))

print(len('test'))
print('test'.__len__())

# defined on a class
print(str(emp_1))
print(emp_1.__str__())
print(emp_1)    # the same as __str__ is used to represent the obj

print(len(emp_1))
print()



# -----------------------------------------------------------------------------
# [8] property


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"  # include 'email'


emp_1 = Employee('Corey', 'Schafer')

print('[8]')
print(emp_1)
emp_1.first = "Abraham"
print(emp_1, "ups!!!")    # the problem is that 'email' hasn't been updated
print()



# The solution is to make 'email' into a method like 'fullname'


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # removed 'email' attribute

    def fullname(self):
        return f'{self.first} {self.last}'

    def email(self):
        return f'{self.first}.{self.last}@email.com'    # make it a method

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email()}"    # call email() method



emp_1 = Employee('Corey', 'Schafer')

print('[8]')
print(emp_1)
emp_1.first = "Abraham"
print(emp_1, "OK!")
print()


# Another way to do it, especially if we still want to call 'email' the old way
# as if it were an attribute, is to make it into a property:


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"    # call as properties



emp_1 = Employee('Corey', 'Schafer')

print('[8]')
print(emp_1)
emp_1.first = "Abraham"
print(emp_1, "still OK!")
print()




# -----------------------------------------------------------------------------
# [9] setters

# With the old example we cannot do this:
# emp_1.fullname = "John Doe"
# AttributeError: property 'fullname' of 'Employee' object has no setter

# SOLUTION: create setter


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"    # call as properties


emp_1 = Employee('Corey', 'Schafer')

print('[9]')
print(emp_1)
# Now this is possible
emp_1.fullname = "John Doe"
print(emp_1)
print()



# -----------------------------------------------------------------------------
# [10] getters, setters, deleters

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"    # call as properties


emp_1 = Employee('Corey', 'Schafer')

print('[10]')
print(emp_1)
del emp_1.fullname   # deleter makes this possible
print(emp_1)
print()

emp_1 = Employee('Corey', 'Schafer')
