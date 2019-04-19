"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MULTIPLICATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# ITERATIVE MULTIPLICATION


def multiplication_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print('\nMultiplication iterative - for positive numbers')
print(multiplication_iter(3, 1))
print(multiplication_iter(7, 7))


def multiplication_iter2(a, b):
    result = 0
    iterations = abs(b)
    while iterations > 0:
        result += a
        iterations -= 1
    if b < 0:
        result = -result
    return result


print('\nMultiplication iterative - negative numbers included')
print(multiplication_iter2(3, 7))
print(multiplication_iter2(-3, 7))
print(multiplication_iter2(3, -7))
print(multiplication_iter2(-3, -7))


# RECURSIVE MULTIPLICATION


def multiplication(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplication(a, b-1)


print('\nMultiplication recursive - for positive numbers')
print(multiplication(3, 1))
print(multiplication(7, 7))
print(multiplication(-7, 7))        # works for a < 0, but error for b < 0


def multiplication2(a, b):
    if b == 0:
        value = 0
    elif abs(b) == 1:
        value = a
    else:
        value = a + multiplication(a, abs(b)-1)

    if b < 0:
        value = -value
    return value


print('\nMultiplication recursive - negative numbers included')
print(multiplication2(3, 7))
print(multiplication2(-3, 7))
print(multiplication2(3, -7))
print(multiplication2(-3, -7))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FACTORIAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

