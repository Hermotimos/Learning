"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ITERATIVE MULTIPLICATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def multiplication_iter1(a, b):
    result = 0
    for n in range(b):
        result += a
    return result


print('\nMultiplication iterative with range - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_iter1(x, y))


# ----------------------------------------------------------------------------------------------------


def multiplication_iter2(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print('\nMultiplication iterative while - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_iter2(x, y))


# ----------------------------------------------------------------------------------------------------


def multiplication_iter3(a, b):
    result = 0
    for n in range(abs(b)):
        result += a
    if b < 0:
        result = -result
    return result


print('\nMultiplication iterative with range - for positive and negative numbers')
for x in range(-2, 3):
    for y in range(-2, 3):
        print(f'{x:2} * {y:2} =', multiplication_iter3(x, y))


# ----------------------------------------------------------------------------------------------------


def multiplication_iter4(a, b):
    result = 0
    iterations = abs(b)
    while iterations > 0:
        result += a
        iterations -= 1
    if b < 0:
        result = -result
    return result


print('\nMultiplication iterative with while - for positive and negative numbers')
for x in range(-2, 3):
    for y in range(-2, 3):
        print(f'{x:2} * {y:2} =', multiplication_iter4(x, y))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RECURSIVE MULTIPLICATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def multiplication_recur1(a, b):
    if b == 0:
        return 0
    return a + multiplication_recur1(a, b - 1)


print('\nMultiplication recursive - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_recur1(x, y))


# ----------------------------------------------------------------------------------------------------


def multiplication_recur2(a, b):
    if b == 0:
        return 0
    else:
        value = a + multiplication_recur2(a, abs(b) - 1)

    if b < 0:
        value = -value
    return value


# Shorter version:
def multiply_recur3(a, b):
    if b == 0:
        return 0
    value = a + multiply_recur3(a, abs(b) - 1)
    if b < 0:
        value = -value
    return value


print('\nMultiplication recursive - negative numbers included')
for x in range(-2, 3):
    for y in range(-2, 3):
        print(f'{x:2} * {y:2} =', multiplication_recur2(x, y))

