"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - memoization

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import time
import sys
sys.setrecursionlimit(100000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print('\nFactorial recursive')
for val in range(11):
    print(val, '=>', factorial(val))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL ITERATIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial2(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


print('\nFactorial iterative 1')
for val in range(11):
    print(val, '=>', factorial2(val))
print(factorial2(12345))


# ----------------------------------------------------------------------------------------------------


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

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE WITH MEMOIZATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# MEMOIZATION: in case of factorials there's no gain in performance if function is called just once.
# The gain occurs after we call it once to get some data into cache dict 'factorials', and only subsequent calls use it.


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
y = 3500
print(factorial_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# This one uses factorials cache, slight improvement in performance
print('Factorial recursive with memoizaition - iteration 2')
timer = time.time()
y = 3500
print(factorial_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Starting from ca. 4000 an more it would throw error if cache 'factorials' were empty, now it computes.
timer = time.time()
y = 5000
print(factorial_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Now it's possible to gradually increase numbers, as 'factorials' cache gradually gets bigger.
timer = time.time()
y = 8000
print(factorial_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
