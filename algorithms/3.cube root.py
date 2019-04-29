"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: guess, approximation and bisection algorithms

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.youtube.com/watch?v=6_Va36K-DE8
        https://stackoverflow.com/questions/49714510/find-a-cube-root-with-newtons-method
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GUESS-AND-CHECK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

# GUESS-AND-CHECK: only positive numbers

def guess_cube_root1(cube):
    for guess in range(cube + 1):
        if guess**3 == cube:
            return f'Cube root of {cube} is {guess}'
    return f'{cube} is not a perfect cube'


print('\n----------------GUESS & CHECK----------------\n')
for d in (8, 27, 64, 100):
    print(guess_cube_root1(d))
print()


# GUESS-AND-CHECK: with negative numbers

def guess_cube_root2(cube):
    guess = 0
    for guess in range(abs(cube) + 1):
        if guess ** 3 >= abs(cube):
            break
    if guess ** 3 != abs(cube):
        return f'{cube} is not a perfect cube.'
    else:
        if cube < 0:
            guess = -guess
        return f'Cube root of {cube} is {guess}.'


for d in (8, -27, -64, 100):
    print(guess_cube_root2(d))
print()


# GUESS-AND-CHECK: with negative numbers [shorter]

def guess_cube_root3(n):
    for guess in range(abs(n)+1):
        if guess**3 == abs(n):
            guess = -guess if n < 0 else guess
            return f'Cube root of {n} is {guess}.'
        elif guess**3 > abs(n):
            return f'{n} is not a perfect cube.'


for d in (8, -27, -64, 100):
    print(guess_cube_root3(d))
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
    guess_counter = 1

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
    guess_counter = 1

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
    low, high = 0, cube
    guess = (low + high) / 2.0
    guess_count = 1

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
    low, high = 0, abs(cube)
    guess = (low + high) / 2.0
    guess_count = 1

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
    low, high = cube, 1
    guess = (low + high) / 2.0
    guess_count = 1

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


# //////////// BISECTION SEARCH FOR POSITIVE, NEGATIVE [RECURSIVE] ////////////

def cube_root6(n, low=0, high=0, tolerance=0.01):
    if high == 0:
        high = abs(n)
    guess = (low + high) / 2
    if abs(abs(n) - guess**3) <= tolerance:
        if n < 0:
            guess = -guess
        return f'Cube root of {n} is approximately: {guess}'
    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root6(n, low, high, tolerance)


print('>>>>BISECION RECURSIVE FOR POSITIVE, NEGATIVE [my own]<<<<')
print(cube_root6(8, tolerance=0.0001))
print(cube_root6(7, tolerance=0.0001))
print(cube_root6(-64, tolerance=0.0001))
print(cube_root6(42341.6435235, tolerance=0.0001))
print()


# //////////// BISECTION SEARCH FOR POSITIVE, NEGATIVE, AND FRACTIONS [RECURSIVE] ////////////


def cube_root7(n, low=0, high=0, tolerance=0.01):
    if abs(n) < 1 and high == 0:
        low, high = abs(n), 1
    elif high == 0:
        high = abs(n)
    guess = (low + high) / 2
    if abs(abs(n) - guess**3) <= tolerance:
        if n < 0:
            guess = -guess
        return f'Cube root of {n} is approximately: {guess}'
    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root7(n, low, high, tolerance)


print('>>>>BISECION RECURSIVE FOR POSITIVE, NEGATIVE, AND FRACTIONS [my own]<<<<')
print(cube_root7(8, tolerance=0.0001))
print(cube_root7(7, tolerance=0.0001))
print(cube_root7(-64, tolerance=0.0001))
print(cube_root7(0.2, tolerance=0.0001))
print(cube_root7(-1.5, tolerance=0.0001))
print(cube_root7(-42341.6435235, tolerance=0.0001))
print(cube_root7(-0.423425, tolerance=0.0001))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NEWTON-RAPHSON <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('\n>>>>NEWTON-RAPHSON SQUARE ROOT <<<<')
# This algorithm has different shapes depending on the case. The shape depends on calculus.
# So this is only taken from net, but real meaning is yet to be understood.


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
def newton_raphson_square_root(square, max_inaccuracy=0.001):
    guess = square / 2
    guess_cnt = 1
    while abs(guess * guess - square) >= max_inaccuracy:
        guess = guess - ((guess**2) - square) / (2 * guess)
        guess_cnt += 1
    print(f"""SQUARE root of {square} is approximately: {guess}
                    Number of guesses: {guess_cnt}.
                    Maximal inaccuracy: {max_inaccuracy}.
                    {guess}**2 = {guess ** 2}\n""")


print('\n>>>>NEWTON-RAPHSON SQUARE ROOT FOR POSITIVE<<<<')
newton_raphson_square_root(49)
newton_raphson_square_root(24)
newton_raphson_square_root(8)
newton_raphson_square_root(435345324)


def newton_raphson_cube_root(cube, max_inaccuracy=0.001):
    guess = cube / 2
    guess_cnt = 1
    while ((1/3) * (2*guess + cube/guess**2)) ** 3 - cube > max_inaccuracy:
        guess = (1/3) * (2*guess + cube/guess**2)
        guess_cnt += 1
    print(f"""CUBE root of {cube} is approximately: {guess}
                    Number of guesses: {guess_cnt}.
                    Maximal inaccuracy: {max_inaccuracy}.
                    {guess}**2 = {guess ** 3}\n""")


print('\n>>>>NEWTON-RAPHSON CUBE ROOT FOR POSITIVE<<<<')
newton_raphson_cube_root(49)
newton_raphson_cube_root(24)
newton_raphson_cube_root(8)
newton_raphson_cube_root(435345324)
