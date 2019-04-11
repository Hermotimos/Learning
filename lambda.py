
# https://www.python.org/dev/peps/pep-0008/
# https://dbader.org/blog/python-lambda-functions
# https://treyhunner.com/2018/09/stop-writing-lambda-expressions/

# SYNTAX:
# lambda arguments: expression

double = lambda x: x*2
square = lambda x: x**2
next_even = lambda x: x + 1 if x % 2 == 1 else False

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
example = lambda x: [e for e in x if e % 2 == 0]

print(double(4))
print(square(4))
print(next_even(3))
print(next_even(6))

print(example(my_list))

print((lambda a, b: a + b)(111, 111))
print('##################################################')

# as per PEP8 lambdas shouldn't be used in simple assignments as above
# lambdas can be used inside other functions like below

# filter() takes function and iterable as args
# returns elements of list that pass the criteria of the function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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


def somefunc(): return 'a'


