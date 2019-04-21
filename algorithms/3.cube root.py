"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: guess, approximation and bisection algorithms

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GUESS-AND-CHECK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
def guess_cube_root1(cube):
    for guess in range(cube + 1):
        if guess**3 == cube:
            print(f'Cube root of {cube} is {guess}')


print('\n----------------GUESS----------------\n')
guess_cube_root1(8)
guess_cube_root1(27)
guess_cube_root1(64)
guess_cube_root1(100)         # This one just won't print because condition is not met.
print()


# GUESS-AND-CHECK: with negative numbers
def guess_cube_root2(cube):
    guess = 0
    for guess in range(abs(cube) + 1):
        if guess ** 3 >= abs(cube):
            break
    if guess ** 3 != abs(cube):
        print(f'{cube} is not a perfect cube.')
    else:
        if cube < 0:
            guess = -guess
        print(f'Cube root of {cube} is {guess}.')


guess_cube_root2(8)
guess_cube_root2(-27)
guess_cube_root2(-64)
guess_cube_root2(100)
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>APPROXIMATE SOLUTION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

# In MIT source was: while abs(cube - guess ** 3) >= epsilon
# Changed to:        while (abs(cube) - guess ** 3) > max_inaccuracy
# With my change program doesn't enter infinite loop for cube = 10000 (that was example of infinite loop in MIT lecture)
# So block of code for 'not perfect cube' could be removed.
# Also added code for negative cubes.
def approximate_cube_root(cube, max_inaccuracy=0.0001, increment=0.01):
    guess = 0.0
    guess_counter = 0

    while (abs(cube) - guess ** 3) > max_inaccuracy:
        guess += increment
        guess_counter += 1

    if cube < 0:
        guess = - guess
    print(f"""Cube root of {cube} is approximately  {guess}.
            Number of guesses: {guess_counter}.
            Maximal inaccuracy allowed: {max_inaccuracy}.
            Increment set to: {increment}.
            {guess}**3 = {guess**3}\n""")


print('\n----------------APPROXIMATION----------------\n')
approximate_cube_root(10000, max_inaccuracy=0.00001, increment=0.0001)
approximate_cube_root(-10000)
for num in range(9):
    approximate_cube_root(num)


# Here's the MIT algorithm with example that enters infinite loop.
def approximate_cube_root_mit(cube, max_inaccuracy=0.0001, increment=0.01):
    guess = 0.0
    guess_counter = 0

    while abs(cube - guess ** 3) > max_inaccuracy:
        guess += increment
        guess_counter += 1
    if abs(cube - guess ** 3) >= max_inaccuracy:
        print(f"""Failed on cube root of {cube}.
                Number of guesses: {guess_counter}.
                Maximal inaccuracy: {max_inaccuracy}.
                Increment: {increment}.\n""")
    else:
        if cube < 0:
            guess = - guess
        print(f"""Cube root of {cube} is approximately  {guess}.
                Number of guesses: {guess_counter}.
                Maximal inaccuracy: {max_inaccuracy}.
                Increment: {increment}.
                {guess}**3 = {guess**3}\n""")

# This enters infinite loop:
# approximate_cube_root_mit(10000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BISECTION/BINARY SEARCH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def bisection_cube_root_only_positive(cube, max_inaccuracy=0.01):
    guess_count = 0
    low, high = 0, cube
    guess = (low + high) / 2.0

    while abs(cube - guess**3) > max_inaccuracy:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess_count += 1
        guess = (low + high)/2.0

    print(f"""Cube root of {cube} is approximately: {guess}
            Number of guesses: {guess_count}.
            Maximal inaccuracy: {max_inaccuracy}.
            {guess}**3 = {guess**3}\n""")


print('\n----------------BISECTION/BINARY SEARCH----------------\n')
print('ONLY POSITIVE NUMBERS')
bisection_cube_root_only_positive(64)
bisection_cube_root_only_positive(42331233, max_inaccuracy=0.00000001)
for num in range(9):
    bisection_cube_root_only_positive(num)
print()


def bisection_cube_root_with_negative(cube, max_inaccuracy=0.01):
    guess_count = 0
    low, high = 0, abs(cube)
    guess = (low + high) / 2.0

    while abs(abs(cube) - guess**3) > max_inaccuracy:
        if guess**3 < abs(cube):
            low = guess
        else:
            high = guess
        guess_count += 1
        guess = (low + high)/2.0

    if cube < 0:
        guess = -guess

    print(f"""Cube root of {cube} is approximately: {guess}
            Number of guesses: {guess_count}.
            Maximal inaccuracy: {max_inaccuracy}.
            {guess}**3 = {guess**3}\n""")
    return guess


print('POSITIVE AND NEGATIVE BUT NO FRACTIONS')
bisection_cube_root_with_negative(-64)
bisection_cube_root_with_negative(-8)
print()


# MIT ASSIGNMENT: FRACTIONS
def bisection_cube_root_fractions(cube, max_inaccuracy=0.00001):
    guess_count = 0
    low, high = cube, 1
    guess = (low + high) / 2.0

    while abs(abs(cube) - guess**3) > max_inaccuracy:
        if guess**3 < abs(cube):
            low = guess
        else:
            high = guess
        guess_count += 1
        guess = (low + high)/2.0

    if cube < 0:
        guess = -guess

    print(f"""Cube root of {cube} is approximately: {guess}
            Number of guesses: {guess_count}.
            Maximal inaccuracy: {max_inaccuracy}.
            {guess}**3 = {guess**3}\n""")
    return guess


print('FRACTIONS')
bisection_cube_root_fractions(0.5)
bisection_cube_root_fractions(0.2)


# Positive, negative and fraction numbers.
# Also fixed bug from MIT lecture considering number of guesses: first guess was never counted.


def bisection_root_all(cube, max_inaccuracy=0.01):

    if abs(cube) < 1:                  # 0 < abs(cube) < 1
        low, high = abs(cube), 1
    else:                              # 1 <= abs(cube)
        low, high = 0, abs(cube)
    guess = (low + high) / 2.0
    guess_count = 1

    while abs(abs(cube) - guess ** 3) > max_inaccuracy:
        if guess ** 3 > abs(cube):
            high = guess
        else:
            low = guess
        guess_count += 1
        guess = (low + high) / 2.0

    if cube < 0:
        guess = -guess

    print(f"""Cube root of {cube} is approximately: {guess}
                Number of guesses: {guess_count}.
                Maximal inaccuracy: {max_inaccuracy}.
                {guess}**3 = {guess ** 3}\n""")


print('>>>>ALL<<<<')
bisection_root_all(8, max_inaccuracy=0.0001)
bisection_root_all(7, max_inaccuracy=0.0001)
bisection_root_all(-64, max_inaccuracy=0.0001)
bisection_root_all(0.2, max_inaccuracy=0.0001)
bisection_root_all(-1.5, max_inaccuracy=0.0001)
bisection_root_all(-42341.6435235, max_inaccuracy=0.0001)
bisection_root_all(-0.423425, max_inaccuracy=0.0001)



# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NEWTON-RAPHSON <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# VIVISECTION:
epsilon = 0.01
y = 8
myguess = y / 2
step = 0
print(f'Cube = {y}\nInitial guess = {myguess}\n')

while abs(myguess * myguess - y) >= epsilon:

    print(f'{myguess}*{myguess} - {y} >= {epsilon}')
    print(f'{myguess * myguess} - {y} >= {epsilon}')
    step += 1
    print(f"""Guess {step}: guess = guess - ((guess**2) - y)/(2 * guess)
         guess = {myguess} - (({myguess}**2) - {y})/(2 * {myguess})
         guess = {myguess} - ({myguess ** 2} - {y})/({2 * myguess})
         guess = {myguess} - {myguess ** 2 - y}/{2 * myguess}
         guess = {myguess} - {(myguess ** 2 - y) / (2 * myguess)}
         guess = {myguess - ((myguess ** 2) - y) / (2 * myguess)})\n""")

    myguess = myguess - ((myguess ** 2) - y) / (2 * myguess)           # <<== ACTUAL ALGORITHM

print(f'Square root of {y} is about {myguess}\n'
      f'{myguess}**2 = {myguess ** 2}')


# FUNCTION
def newton_raphson_square_root(square, max_inaccuracy=0.01):
    guess = square / 2
    guess_cnt = 1
    while abs(guess * guess - square) >= max_inaccuracy:
        guess = guess - ((guess**2) - square) / (2 * guess)
        guess_cnt += 1
    print(f"""Cube root of {square} is approximately: {guess}
                    Number of guesses: {guess_cnt}.
                    Maximal inaccuracy: {max_inaccuracy}.
                    {guess}**2 = {guess ** 2}\n""")


print('\n>>>>NEWTON-RAPHSON SQUARE ROOT FOR POSITIVE<<<<')
newton_raphson_square_root(24)
newton_raphson_square_root(7)
newton_raphson_square_root(435345324)
