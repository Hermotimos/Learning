""""
    This file is for learning and exercise purposes.

    Topics:
        - simple lambda syntax
        - examples: map(), filter(), reduce()
        - comprehensions
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

example1 = lambda x: [e for e in x if e % 2 == 0]
print(example1(my_list))

example2 = [e for e in my_list if e % 2 == 0]               # NOTE: comprehension is simpler
print(example2)


print('\n##################################################')
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered1 = list(filter(lambda x: (x % 2 == 0), my_list))
print(filtered1)
filtered2 = [x for x in my_list if x % 2 == 0]              # NOTE: comprehension is simpler
print(filtered2)


for num in filter(lambda x: x % 2 == 1, range(0, 10)):
    print(num, '', end='')
print('')
for num in [x for x in range(0, 10) if x % 2 == 1]:         # NOTE: comprehension is simpler
    print(num, '', end='')


print('\n##################################################')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mapped = list(map(lambda x: x + 1, my_list))
print(mapped)
mapped = [x + 1 for x in my_list]                           # NOTE: comprehension is simpler
print(mapped)

mapped = list(map(lambda x: x + 1 if x % 2 == 0 else x, my_list))
print(mapped)
mapped = [x + 1 if x % 2 == 0 else x for x in my_list]      # NOTE: comprehension is simpler
print(mapped)


print('\n##################################################')
from functools import reduce
my_list = [1, 2, 3, 4]

summed = reduce(lambda a, b: a + b, my_list)           # NOTE: no idea how to do this with comprehension
print(summed)                                          # but sum(*my_list) will do
summed = sum(my_list)
print(summed)

my_tuple = (1, 2, 3, 4)
summed = reduce(lambda a, b: a + b, my_tuple)          # NOTE: no idea how to do this with comprehension
print(summed)                                          # but sum(*my_tuple) will do
summed = sum(my_tuple)
print(summed)

my_letters = ('a', 'b', 'c', 'c', 'c', 'c', 'd', 'a', 'g', 'b', 'b', 'b')
concatenated = reduce(lambda a, b: a + b, my_letters)
print(concatenated)
