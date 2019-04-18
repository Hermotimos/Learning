"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GUESS-AND-CHECK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
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
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>APPROXIMATE SOLUTION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

# In MIT source was: while abs(cube - guess ** 3) >= ...
# With my change program doesn't enter infinite loop for cube = 10000 (that was example of infinite loop in MIT lecture)
# Also added code for negative cubes.
def approximate_cube_root(cube, max_inaccuracy=0.0001, increment=0.01):
    guess = 0.0
    guess_counter = 0

    while (abs(cube) - guess ** 3) >= max_inaccuracy:
        guess += increment
        guess_counter += 1
    if (abs(cube) - guess ** 3) >= max_inaccuracy:
        print(f"""Failed on cube root of {cube}.
                Number of guesses: {guess_counter}.
                Maximal inaccuracy allowed: {max_inaccuracy}.
                Increment set to: {increment}.\n""")
    else:
        if cube < 0:
            guess = - guess
        print(f"""Cube root of {cube} is approximately  {guess}.
                Number of guesses: {guess_counter}.
                Maximal inaccuracy allowed: {max_inaccuracy}.
                Increment set to: {increment}.
                {guess}**3 = {guess**3}\n""")


approximate_cube_root(10000, max_inaccuracy=0.00001, increment=0.0001)
approximate_cube_root(-10000)
for num in range(9):
    approximate_cube_root(num)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BISECTION SEARCH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
