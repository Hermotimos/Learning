"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""


# GUESS-AND-CHECK
def guess1(cube):
    for guess in range(cube + 1):
        if guess**3 == cube:
            print(f'Cube root of {cube} is {guess}')


guess1(8)
guess1(27)
guess1(64)
guess1(100)         # This one just won't print because condition is not met.
print()


# GUESS-AND-CHECK: with negative numbers
def guess2(cube):
    result = 0
    for guess in range(abs(cube) + 1):
        if guess ** 3 >= abs(cube):
            result = guess
            break
    if abs(cube) != result ** 3:
        print(f'{cube} is not a perfect cube.')
    else:
        if cube < 0:
            result = -result
        print(f'Cube root of {cube} is {result}.')


guess2(8)
guess2(-27)
guess2(-64)
guess2(100)


# APPROXIMATE SOLUTION:


