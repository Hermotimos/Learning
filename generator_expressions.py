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
    print(elem, ' ', end='')
print()

generator_expression = (x**2 for x in my_list if x % 2 == 0)
for elem in generator_expression:
    print(elem, ' ', end='')
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
