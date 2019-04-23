"""
    This file is for learning and exercise purposes.

    Topics:
        - comprehensions
    Sources:
        https://dbader.org/blog/list-dict-set-comprehensions-in-python
"""


print('LIST COMPREHENSION')
x = [x * 2 for x in range(10)]
print(x)
x = list(range(0, 19, 2))
print(x)


print('SET COMPREHENSION')
x = {x * x for x in range(-9, 10)}
print(x)

print('DICT COMPREHENSION')
x = {x: x * x for x in range(5)}
print(x)

print('TUPLE COMPREHENSION')
x = tuple(x for x in range(5))
print(x)
x = tuple(range(5))
print(x)


print('COMBINING LISTS WITH LIST COMPREHENSION')
nums = [1, 2, 3]
letters = ['a', 'b', 'c', 'd', 'e']
nums_letters = [[num, let] for num in nums for let in letters]
print(nums_letters)
print(x)


print('MORE COMPREHENSIONS')
x = [x**3 for x in range(1, 10)]
print(x)
x = {n for n in [0, 7, 0, 1, 2, 6, 0, 2, 1]}
print(x)
x = {w: len(w) for w in ('apple', 'I', 'have', 'no')}
print(x)
x = tuple(sign for sign in 'This is nothing')
print(x)
x = frozenset({n for n in [0, 7, 0, 1, 2, 6, 0, 2, 1]})
print(x)
