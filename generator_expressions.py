"""
    This file is for learning and exercise purposes.

    Topics:
        - generator expressions
        - looping over generator expressions

    Sources:
        https://dbader.org/blog/python-generators
        https://www.programiz.com/python-programming/generator
        https://dbader.org/blog/python-generator-expressions
"""


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

generator_expression = (x**2 for x in my_list)
for elem in generator_expression:
    print(elem, '', end='')
print()

generator_expression = (x**2 for x in my_list if x % 2 == 0)
for elem in generator_expression:
    print(elem, '', end='')
print()

generator_expression = (x**2 for x in my_list if x % 2 == 0)
x = sum(generator_expression)
print(x)

for elem in (x + 1 for x in my_list):
    print(elem, '\b, ', end='')
print()


my_list = [1, 2, 3, 4]
my_list_2 = ['a', 'b', 'c']
my_list_3 = ['*', '~']
for outcome in (num * let + symb for num in my_list
                                 for let in my_list_2
                                 for symb in my_list_3):
    print(outcome)



# Generators vs iterators

iterator = iter([1, 2, 3, 4, 5])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print()

generator = (x for x in [1, 2, 3, 4, 5])
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

iterator = iter([1, 2, 3, 4, 5])
generator = (x for x in [1, 2, 3, 4, 5])

for v in iterator:
    print(v)

for v in generator:
    print(v)

print()



#  Iterator class

class MyIterator:

    def __init__(self, iterable):
        self.iter_obj = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter_obj)


myiterator = MyIterator([1, 2, 3])  # myiterator = iter([1, 2, 3])
print(myiterator)
for i in myiterator:
    print(i)

print()



# Generator class

class MyGenerator:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for x in self.iterable:
            yield x


mygen = MyGenerator([1, 2, 3])  # mygen = (x for x in [1, 2, 3])
print(mygen)
for i in mygen:
    print(i)
