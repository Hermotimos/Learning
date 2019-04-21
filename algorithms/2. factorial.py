"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - memoization

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import time
import functools
import sys
sys.setrecursionlimit(100000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print('\nFactorial recursive')
for val in range(11):
    print(val, '=>', factorial_recursive(val))
# print(factorial_recursive(12345))  ------------> Recursive algorithm is not efficient enough to compute this.


# Shorter but harder to read version is:
def factorial_recursive_short(n): return 1 if n == 0 else n * factorial_recursive(n - 1)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL ITERATIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial_iterative_1(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


print('\nFactorial iterative 1')
for val in range(11):
    print(val, '=>', factorial_iterative_1(val))
print(factorial_iterative_1(12345))


# ----------------------------------------------------------------------------------------------------


def factorial_iterative_2(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


print('\nFactorial iterative 2')
for val in range(11):
    print(val, '=>', factorial_iterative_2(val))
print(factorial_iterative_2(12345))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE WITH MEMOIZATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# MEMOIZATION: in case of factorials there's no gain in performance if function is called just once.
# The gain occurs after we call it once to get some data into cache dict 'factorials', and only subsequent calls use it.


factorials = {}


def factorial_recur_memo(n):
    if n in factorials:
        return factorials[n]
    else:
        if n == 0:
            result = 1
        else:
            result = n * factorial_recur_memo(n - 1)
        factorials[n] = result
        return result


print('\n', '-' * 50)
print('Factorial recursive with memoizaition - iteration 1')
print('-' * 50)

timer = time.time()
y = 3500
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# This one uses factorials cache, slight improvement in performance
print('Factorial recursive with memoizaition - iteration 2')
timer = time.time()
y = 3500
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Starting from ca. 4000 an more it would throw error if cache 'factorials' were empty, now it computes.
timer = time.time()
y = 5000
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Now it's possible to gradually increase numbers, as 'factorials' cache gradually gets bigger.
timer = time.time()
y = 8000
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)

timer = time.time()
y = 8000
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)


# ----------------------------------------------------------------------------------------------------


factorials_2 = {}


def factorial_recur_memo_short(n):
    if n not in factorials_2:
        if n == 0:
            value = 1
        else:
            value = n * factorial_recur_memo_short(n - 1)
        factorials_2[n] = value
    return factorials_2[n]


def factorial_recur_memo_shortest(n):
    if n not in factorials_2:
        value = 1 if n == 0 else n * factorial_recur_memo_short(n - 1)
        factorials_2[n] = value
    return factorials_2[n]


print('\n', '-' * 50)
print('Factorial recursive with memoization - more concise code')
print('-' * 50)

timer = time.time()
y = 3500
print(factorial_recur_memo_short(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

timer = time.time()
y = 3500
print(factorial_recur_memo_short(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

timer = time.time()
y = 5000
print(factorial_recur_memo_short(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

timer = time.time()
y = 8000
print(factorial_recur_memo_short(y))
print(f'Time for {y}!: ', time.time() - timer)


# ----------------------------------------------------------------------------------------------------


@functools.lru_cache(maxsize=100000)
def factorial_memo_decorated(n):
    if n == 0:
        return 1
    else:
        return n * factorial_memo_decorated(n - 1)

# SO FAR THIS DOESN'T WORK - TODO


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def time_function(function):
    def wrapper(*args):
        timer_start = time.time()
        function(*args)
        timer_stop = time.time() - timer_start
        print('Time elapsed for {}({}): {}'.format(function.__name__, ",".join(str(a) for a in args), timer_stop))
    return wrapper


clocked_factorial = time_function(factorial_recur_memo_short)
clocked_factorial(3000)