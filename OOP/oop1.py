# TODO: dependency injection: https://youtu.be/-ghD-XjjO2g?t=622
# TODO: abstract class (ABC), abstract methods



# -----------------------------------------------------------------------------
# [1]


class Employee:
    # create class, every class is a type

    def __init__(self, first, last, pay):
        # define instance attributes of Employee
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # define regular method of Employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

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
# [2]


class Employee:

    # class variables
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # increment class variable whenever an instance is created
        Employee.employee_count += 1

    def __str__(self) -> str:
        return self.fullname()

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

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
# [3]


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
        return '{} {}'.format(self.first, self.last)

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
# [4]


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
        return '{} {}'.format(self.first, self.last)

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
