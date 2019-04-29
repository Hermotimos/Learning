"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - memoization
        - decorators

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import time
import sys
from time_function_decorator import time_function
sys.setrecursionlimit(100000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Shorter:
def factorial_rec_short1(n):
    if n < 2:
        return 1
    return n * factorial_rec_short1(n - 1)


# Still shorter but harder to read:
def factorial_rec_short2(n): return 1 if n < 2 else n * factorial_rec_short2(n - 1)


print('\nFactorial recursive')
for val in range(11):
    print(val, '=>', factorial_recursive(val))
# print(factorial_recursive(12345))  ------------> Recursive algorithm is not efficient enough to compute this.


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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL WITH MEMOIZATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# MEMOIZATION: in case of factorials_1 there's no gain in performance if function is called just once.
# The gain occurs by second call (after data from first is cached in dict 'factorials_1' subsequent calls can use it).

factorials_1 = {}


def factorial_recur_memo(n):
    if n in factorials_1:
        return factorials_1[n]
    else:
        if n == 0:
            result = 1
        else:
            result = n * factorial_recur_memo(n - 1)
        factorials_1[n] = result
        return result


print('\n', '-' * 50)
print('Factorial recursive with memoizaition - iteration 1')
print('-' * 50)

timer = time.time()
y = 3500
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# This one already uses factorials_1 cache, so there's slight improvement in performance
print('\n', '-' * 50)
print('Factorial recursive with memoizaition - iteration 2 (improvement in performance)')
print('-' * 50)

timer = time.time()
y = 3500
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Starting from ca. 4000 an more it would throw error if cache 'factorials_1' were empty, now it computes.
timer = time.time()
y = 5000
print(factorial_recur_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

# Now it's possible to gradually increase numbers, as 'factorials_1' cache gradually gets bigger.
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

# ----------------------------------------------------------------------------------------------------

factorials_3 = {}


def factorial_iter_memo(n):
    if n not in factorials_3:
        value = 1
        for n in range(1, n + 1):
            value *= n
            factorials_3[n] = value
    return factorials_3[n]


print('\n', '-' * 50)
print('Factorial iterative with memoization')
print('-' * 50)

timer = time.time()
y = 50000
print(factorial_iter_memo(y))
print(f'Time for {y}!: ', time.time() - timer)
print()

factorials_3 = {}
print(f'Time for 50000!: ')
time_function(factorial_iter_memo)(50000)
# TODO works up to 50000 (1.5 secs) but more will hang the system ==> try out on stronger system.
# TODO: Probably this is caused by searching for memoized/cached data => try with bisection search algorithms
print()

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
factorials_1 = {}
factorials_2 = {}
factorials_3 = {}
# Redeclared to reset stored data before performance test.

print('PERFORMANCE: iterative 1')
clocked_factorial = time_function(factorial_iterative_1)
for v in (3000, 3000, 5000, 5000, 8000, 8000, 20000, 90000, 90000):
    print(v, '', end=''), clocked_factorial(v)
print()

print('PERFORMANCE: iterative 2')
clocked_factorial = time_function(factorial_iterative_2)
for v in (3000, 3000, 5000, 5000, 8000, 8000, 20000, 90000, 90000):
    print(v, '', end=''), clocked_factorial(v)
print()


print('PERFORMANCE: recursive')
clocked_factorial = time_function(factorial_recursive)
for v in (3000, 3000):          # THIS WON'T EVEN COMPUTE FOR 5000 !!!!!!
    print(v, '', end=''), clocked_factorial(v)
print()


print('PERFORMANCE: recursive with memoization')
clocked_factorial = time_function(factorial_recur_memo)
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    print(v, '', end=''), clocked_factorial(v)
print()


print('PERFORMANCE: iterative with memoization')
clocked_factorial = time_function(factorial_iter_memo)
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500, 50000, 60000):
    print(v, '', end=''), clocked_factorial(v)
print()


# CONCLUSION:
# ----------
# RECURSIVE: Without memoization recursive algorithm is a joke.
# ITERATIVE: performs very well for small numbers (up to 20000). But then it slows down significantly.
# RECURSIVE WITH MEMOIZATION: works well if it can populate its cache with gradually increasing searched n.
#                             So it's potentially better than iterative for big numbers, but under conditions.
# ITERATIVE WITH MEMOIZATION: the most efficient one, can handle 50000 from scratch in 1.5 secs (though more hangs the
#                             system instead of throwing exception). It's slightly slower than recursive memo, but
#                             can handle much bigger leaps of n values than recursive.

# TODO clean up this mess... - break into 2 files: one with algorithms and trials, another with performance tests.

# TODO something doesn't work with time for recursive with memo: it prints 2.5e-06 secs though it takes no time...