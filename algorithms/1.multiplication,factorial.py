"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import time


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MULTIPLICATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

# ITERATIVE MULTIPLICATION


def multiplication_iter1(a, b):
    result = 0
    for n in range(0, b):
        result += a
    return result


print('\nMultiplication iterative with range - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_iter1(x, y))


def multiplication_iter2(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print('\nMultiplication iterative while while - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_iter2(x, y))


def multiplication_iter3(a, b):
    result = 0
    for n in range(0, abs(b)):
        result += a
    if b < 0:
        result = -result
    return result


print('\nMultiplication iterative with range - for positive and negative numbers')
for x in range(-2, 3):
    for y in range(-2, 3):
        print(f'{x:2} * {y:2} =', multiplication_iter3(x, y))


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

# ------------------------------------------------------------------------------------------------------

# RECURSIVE MULTIPLICATION


def multiplication_recur1(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplication_recur1(a, b - 1)


print('\nMultiplication recursive - for positive numbers')
for x in range(0, 3):
    for y in range(0, 4):
        print(f'{x:2} * {y:2} =', multiplication_recur1(x, y))


def multiplication_recur2(a, b):
    if b == 0:
        value = 0
    elif abs(b) == 1:
        value = a
    else:
        value = a + multiplication_recur2(a, abs(b) - 1)

    if b < 0:
        value = -value
    return value


print('\nMultiplication recursive - negative numbers included')
for x in range(-2, 3):
    for y in range(-2, 3):
        print(f'{x:2} * {y:2} =', multiplication_recur2(x, y))

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FACTORIAL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print('\nFactorial recursive')
for val in range(11):
    print(val, '=>', factorial(val))


# ------------------------------------------------------------------------------------------------------
def factorial2(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


print('\nFactorial iterative 1')
for val in range(11):
    print(val, '=>', factorial2(val))
print(factorial2(12345))


def factorial3(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


print('\nFactorial iterative 2')
for val in range(11):
    print(val, '=>', factorial3(val))
print(factorial3(12345))

# ------------------------------------------------------------------------------------------------------
# MEMOIZATION: in case of factorials there's no gain in performance if function is called just once.
# The gain occurs after we call it once to get some data into cache dict 'factorials', and only subsequent calls use it.

import sys
sys.setrecursionlimit(100000)
factorials = {}


def factorial_memo(n):
    if n in factorials:
        return factorials[n]
    else:
        if n <= 1:
            result = 1
        else:
            result = n * factorial_memo(n - 1)
        factorials[n] = result
        return result


print('\nFactorial recursive with memoizaition - iteration 1')
timer = time.time()
n = 3500
print(factorial_memo(n))
print(f'Time for {n}!: ', time.time() - timer)
print()

# This one uses factorials cache, slight improvement in performance
print('Factorial recursive with memoizaition - iteration 2')
timer = time.time()
n = 3500
print(factorial_memo(n))
print(f'Time for {n}!: ', time.time() - timer)
print()

# Starting from ca. 4000 an more it would throw error if cache 'factorials' were empty, now it computes.
timer = time.time()
n = 5000
print(factorial_memo(n))
print(f'Time for {n}!: ', time.time() - timer)
print()

# Now it's possible to gradually increase numbers, as 'factorials' cache gradually gets bigger.
timer = time.time()
n = 8000
print(factorial_memo(n))
print(f'Time for {n}!: ', time.time() - timer)
