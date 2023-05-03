""""
    This file is for learning and exercise purposes.

    Topics:
        - simple lambda syntax
        - examples: map(), filter(), reduce()

    Sources:
        https://www.python.org/dev/peps/pep-0008/
        https://dbader.org/blog/python-lambda-functions
        https://treyhunner.com/2018/09/stop-writing-lambda-expressions/
"""


# SYNTAX:
# lambda arguments: expression

double = lambda x: x*2
square = lambda x: x**2
next_even = lambda x: x + 1 if x % 2 == 1 else x + 2

print(double(4))
print(square(4))
print(next_even(3))
print(next_even(6))
print()

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example = lambda x: [e for e in x if e % 2 == 0]

print(example(my_list))

print((lambda a, b: a + b)(111, 111))
print('##################################################')

# as per PEP8 lambdas shouldn't be used in simple assignments as above
# lambdas can be used inside other functions like below


# filter() takes function and iterable as args
# returns elements of list that pass the criteria of the function
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = list(filter(lambda x: (x % 2 == 0), my_list))
print(filtered)

filtered = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered)

for num in filter(lambda x: x % 2 == 1, range(0, 10)):
    print(num, '', end='')
print('\n##################################################')


# map() takes function and iterable as args
# returns all elements of iterable modified by the function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mapped = list(map(lambda x: x + 1, my_list))
print(mapped)

mapped = list(map(lambda x: x + 1 if x % 2 == 0 else x, my_list))
print(mapped)
print('\n##################################################')


# reduce() takes function and iterable as args
# performs rolling computation (function) on sequential pairs of elements from the iterable

from functools import reduce
summed = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(summed)

my_tuple = (1, 2, 3, 4)
summed = reduce(lambda a, b: a + b, my_tuple)
print(summed)

my_letters = ('a', 'b', 'c', 'c', 'c', 'c', 'd', 'a', 'g', 'b', 'b', 'b')
concatenated = reduce(lambda a, b: a + b, my_letters)
print(concatenated)









# lambda

func = lambda a, b: f"{a} / {b}"
print(func(1, 2))



#  map
alist1 = ['aa', 'bb', 'cc']
print(list(map(str.upper, alist1)))
print(list(map(str.title, alist1)))
print(list(map(str.capitalize, alist1)))

alist2 = [1.2, 2.5, 3.6]
print(list(map(round, alist2)))


zipped = list(map(lambda a, b: (a, b), alist1, alist2))
print(zipped)


def myzip(a, b):
    return a, b


zipped = list(map(myzip, alist1, alist2))
print(zipped)


# filter

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
print(list(filter(lambda a: a == a[::-1], dromes)))


# reduce

from functools import reduce


def mysum(a, b):
    return a + b


numbers = [3, 4, 6, 9, 34, 12]
print(reduce(mysum, numbers))


def anytrue(a, b) -> bool:
    return bool(a or b)


def alltrue(a, b) -> bool:
    return bool(a and b)


vals = [0, 0, 0, 1, 1, 0]

print(reduce(anytrue, vals))
print(reduce(alltrue, vals))

print(reduce(lambda a, b: bool(a or b), vals))
print(reduce(lambda a, b: bool(a and b), vals))

