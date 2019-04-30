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
print('\n-------------------------------------GUESS & CHECK\n')


# 1) only positive numbers

def guess_cube_root1(cube):
    for guess in range(cube + 1):
        if guess**3 == cube:
            return f'Cube root of {cube} is {guess}'
    return f'{cube} is not a perfect cube'


for d in (8, 27, 64, 100):
    print(guess_cube_root1(d))
print()


# ----------------------------------------------------------------------------------------------------

# 2) positive & negative numbers

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


# ----------------------------------------------------------------------------------------------------

# 3) positive & negative numbers [shorter]

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
print('\n-------------------------------------APPROXIMATION\n')


# In MIT source was: while abs(cube - guess ** 3) >= epsilon
# Changed to:        while (abs(cube) - guess ** 3) > tolerance
# With my change program doesn't enter infinite loop for cube = 10000 (that was example of infinite loop in MIT lecture)
# So block of code for 'not perfect cube' could be removed.
# Also added code for negative cubes.


def approximate_cube_root(cube, tolerance=0.001, increment=0.01):
    guess = 0.0
    guess_counter = 1

    while (abs(cube) - guess ** 3) > tolerance:
        guess += increment
        guess_counter += 1

    if cube < 0:
        guess = - guess
    print(f"""Approximate cube root of {cube} is: {guess}.
            Guesses: {guess_counter}.
            Max. inaccuracy: {tolerance}.
            Increment: {increment}.
            {guess}**3 = {guess**3}\n""")


approximate_cube_root(10000, tolerance=0.00001, increment=0.0001)
approximate_cube_root(-10000)

for num in range(9):
    approximate_cube_root(num)


# Here's the MIT algorithm with example that enters infinite loop.
def approximate_cube_root_mit(cube, tolerance=0.0001, increment=0.01):
    guess = 0.0
    guess_counter = 1

    while abs(cube - guess ** 3) > tolerance:
        guess += increment
        guess_counter += 1
    if abs(cube - guess ** 3) >= tolerance:
        print(f"""Failed on cube root of {cube}.
                Guesses: {guess_counter}.
                Max. inaccuracy: {tolerance}.
                Increment: {increment}.\n""")
    else:
        if cube < 0:
            guess = - guess
        print(f"""Approximate cube root of {cube} is: {guess}.
                Guesses: {guess_counter}.
                Max. inaccuracy: {tolerance}.
                Increment: {increment}.
                {guess}**3 = {guess**3}\n""")

# This enters infinite loop:
# approximate_cube_root_mit(10000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BISECTION/BINARY SEARCH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('\n-------------------------------------BISECTION/BINARY SEARCH\n')


def bisection_cube_root_only_positive(cube, tolerance=0.01):
    low, high = 0, cube
    guess = (low + high) / 2.0
    guess_counter = 1

    while abs(cube - guess**3) > tolerance:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess_counter += 1
        guess = (low + high)/2.0

    print(f"""Approximate cube root of {cube} is: {guess}.
            Guesses: {guess_counter}.
            Max. inaccuracy: {tolerance}.
            {guess}**3 = {guess**3}\n""")


print('\nBISECTION: POSITIVE NUMS\n')
bisection_cube_root_only_positive(64)
bisection_cube_root_only_positive(42331233, tolerance=0.00000001)

for num in range(9):
    bisection_cube_root_only_positive(num)


# ----------------------------------------------------------------------------------------------------


def bisection_cube_root_with_negative(cube, tolerance=0.01):
    low, high = 0, abs(cube)
    guess = (low + high) / 2.0
    guess_counter = 1

    while abs(abs(cube) - guess**3) > tolerance:
        if guess**3 < abs(cube):
            low = guess
        else:
            high = guess
        guess_counter += 1
        guess = (low + high)/2.0

    if cube < 0:
        guess = -guess

    print(f"""Approximate cube root of {cube} is: {guess}.
            Guesses: {guess_counter}.
            Max. inaccuracy: {tolerance}.
            {guess}**3 = {guess**3}\n""")
    return guess


print('\nBISECTION: POSITIVE & NEGATIVE NUMS\n')
bisection_cube_root_with_negative(-64)
bisection_cube_root_with_negative(-8)


# ----------------------------------------------------------------------------------------------------


# MIT ASSIGNMENT: FRACTIONS

def bisection_cube_root_fractions(cube, tolerance=0.00001):
    low, high = cube, 1
    guess = (low + high) / 2.0
    guess_counter = 1

    while abs(abs(cube) - guess**3) > tolerance:
        if guess**3 < abs(cube):
            low = guess
        else:
            high = guess
        guess_counter += 1
        guess = (low + high)/2.0

    if cube < 0:
        guess = -guess

    print(f"""Approximate cube root of {cube} is: {guess}.
            Guesses: {guess_counter}.
            Max. inaccuracy: {tolerance}.
            {guess}**3 = {guess**3}\n""")
    return guess


print('\nBISECTION: ONLY FRACTIONS\n')
bisection_cube_root_fractions(0.5)
bisection_cube_root_fractions(0.2)


# ----------------------------------------------------------------------------------------------------


# Positive, negative and fraction numbers.
# Also fixed bug from MIT lecture considering number of guesses: first guess was never counted.

def bisection_root_all(cube, tolerance=0.01):

    if abs(cube) < 1:                  # 0 < abs(cube) < 1
        low, high = abs(cube), 1
    else:                              # 1 <= abs(cube)
        low, high = 0, abs(cube)
    guess = (low + high) / 2.0
    guess_counter = 1

    while abs(abs(cube) - guess ** 3) > tolerance:
        if guess ** 3 > abs(cube):
            high = guess
        else:
            low = guess
        guess_counter += 1
        guess = (low + high) / 2.0

    if cube < 0:
        guess = -guess

    print(f"""Approximate cube root of {cube} is: {guess}.
            Guesses: {guess_counter}.
            Max. inaccuracy: {tolerance}.
            {guess}**3 = {guess**3}\n""")


print('\nBISECTION: POS, NEG & FRACTIONS\n')
for d in (7, 8, -64, 0.2, -1.5, -0.423425, -42341.6435235):
    bisection_root_all(d, tolerance=0.0001)


# ----------------------------------------------------------------------------------------------------


# BISECTION SEARCH FOR POSITIVE, NEGATIVE [RECURSIVE]

def cube_root6(n, low=0, high=0, tolerance=0.01):
    if high == 0:
        high = abs(n)
    guess = (low + high) / 2
    if abs(abs(n) - guess**3) <= tolerance:
        if n < 0:
            guess = -guess
        return f'Approximate cube root of {n} is: {guess}.'
    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root6(n, low, high, tolerance)


print('\nBISECTION: RECURSIVE FOR POSITIVE, NEGATIVE [my own]\n')
for d in (7, 8, -64, -1.5, -42341.6435235):
    print(cube_root6(d, tolerance=0.0001))


# ----------------------------------------------------------------------------------------------------


#  BISECTION SEARCH FOR POSITIVE, NEGATIVE, AND FRACTIONS [RECURSIVE]

def cube_root7(n, low=0, high=0, tolerance=0.01):
    if abs(n) < 1 and high == 0:
        low, high = abs(n), 1
    elif high == 0:
        high = abs(n)
    guess = (low + high) / 2
    if abs(abs(n) - guess**3) <= tolerance:
        if n < 0:
            guess = -guess
        return f'Approximate cube root of {n} is: {guess}.'
    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root7(n, low, high, tolerance)


print('\nBISECTION: RECURSIVE FOR POSITIVE, NEGATIVE, AND FRACTIONS [my own]\n')
for d in (7, 8, -64, 0.2, -1.5, -0.423425, -42341.6435235):
    print(cube_root7(d, tolerance=0.0001))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NEWTON-RAPHSON <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('\n-------------------------------------NEWTON-RAPHSON\n')
print('>>>>NEWTON-RAPHSON SQUARE ROOT + extensive printout from function<<<<')
print('>>>>> BEGIN')

# Newton-Raphson algorithm has different shapes depending on the case. The shape depends on calculus.
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
print('>>>>> END\n\n')


# ----------------------------------------------------------------------------------------------------


# SQUARE ROOT FOR POSITIVE

def newton_raphson_square_root(square, tolerance=0.001):
    guess = square / 2
    guess_cnt = 1
    while abs(guess * guess - square) >= tolerance:
        guess = guess - ((guess**2) - square) / (2 * guess)
        guess_cnt += 1
    print(f"""SQUARE root of {square} is approximately: {guess}
                    Number of guesses: {guess_cnt}.
                    Maximal inaccuracy: {tolerance}.
                    {guess}**2 = {guess ** 2}\n""")


print('\n>>>>NEWTON-RAPHSON SQUARE ROOT FOR POSITIVE<<<<')
for v in (8, 24, 49, 435345324):
    newton_raphson_square_root(v)


# ----------------------------------------------------------------------------------------------------


# CUBE ROOT FOR POSITIVE

def newton_raphson_cube_root(cube, tolerance=0.001):
    guess = cube / 2
    guess_cnt = 1
    while ((1/3) * (2*guess + cube/guess**2)) ** 3 - cube > tolerance:
        guess = (1/3) * (2*guess + cube/guess**2)
        guess_cnt += 1
    print(f"""CUBE root of {cube} is approximately: {guess}
                    Number of guesses: {guess_cnt}.
                    Maximal inaccuracy: {tolerance}.
                    {guess}**2 = {guess ** 3}\n""")


print('\n>>>>NEWTON-RAPHSON CUBE ROOT FOR POSITIVE<<<<')
for v in (8, 24, 49, 435345324):
    newton_raphson_cube_root(v)

