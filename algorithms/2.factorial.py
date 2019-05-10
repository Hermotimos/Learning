"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - memoization
        - decorators

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import sys
from time_function_decorator import time_function
sys.setrecursionlimit(100000)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def fact_recur1(n):
    if n == 0:
        return 1
    else:
        return n * fact_recur1(n - 1)


# Shorter:
def fact_recur11(n):
    if n < 2:
        return 1
    return n * fact_recur11(n - 1)


# Shortest but unreadable:
def fact_recur111(n): return 1 if n < 2 else n * fact_recur111(n - 1)


print('\nFactorial recursive')
for val in range(11):
    print(val, '=>', fact_recur1(val))
# print(factorial_recursive(12345))  ------------> Recursive algorithm is not efficient enough to compute this.


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL ITERATIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def fact_iter1(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


print('\nFactorial iterative 1')
for val in range(11):
    print(val, '=>', fact_iter1(val))
print(fact_iter1(12345))


# ----------------------------------------------------------------------------------------------------


def fact_iter2(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


print('\nFactorial iterative 2')
for val in range(11):
    print(val, '=>', fact_iter2(val))
print(fact_iter2(12345))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FACTORIAL WITH MEMOIZATION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# MEMOIZATION: in case of factorials_1 there's no gain in performance if function is called just once.
# The gain occurs by second call (after data from first is cached in dict 'factorials_1', subsequent calls can use it).

factorials_1 = {}


def fact_recur_memo1(n):
    if n in factorials_1:
        return factorials_1[n]
    else:
        if n == 0:
            result = 1
        else:
            result = n * fact_recur_memo1(n - 1)
        factorials_1[n] = result
        return result


def fact_recur_memo1_short(n):
    if n in factorials_1:
        return factorials_1[n]
    if n < 2:
        factorials_1[n] = 1
    else:
        factorials_1[n] = n * fact_recur_memo1_short(n-1)
    return factorials_1[n]


print('\nFactorial recursive with memoization 1')
time_function(fact_recur_memo1)(3500)
# The one below already uses factorials_1 cache, so there's slight improvement in performance
time_function(fact_recur_memo1)(3500)
# Starting from ca. 4000 and more it would throw error if cache 'factorials_1' were empty, now it computes.
# Now it's possible to gradually increase numbers, as 'factorials_1' cache gradually gets bigger.
time_function(fact_recur_memo1)(5000)
time_function(fact_recur_memo1)(8000)
time_function(fact_recur_memo1)(8000)


# ----------------------------------------------------------------------------------------------------

factorials_2 = {}


def fact_recur_memo2(n):
    if n not in factorials_2:
        if n == 0:
            value = 1
        else:
            value = n * fact_recur_memo2(n - 1)
        factorials_2[n] = value
    return factorials_2[n]


print('\nFactorial recursive with memoization - 2')
time_function(fact_recur_memo2)(3500)
time_function(fact_recur_memo2)(3500)
time_function(fact_recur_memo2)(5000)
time_function(fact_recur_memo2)(8000)
time_function(fact_recur_memo2)(8000)


# ----------------------------------------------------------------------------------------------------

factorials_3 = {}


def fact_recur_memo3(n):
    if n not in factorials_3:
        value = 1 if n == 0 else n * fact_recur_memo2(n - 1)
        factorials_3[n] = value
    return factorials_3[n]


print('\nFactorial recursive with memoization - 3')
time_function(fact_recur_memo3)(3500)
time_function(fact_recur_memo3)(3500)
time_function(fact_recur_memo3)(5000)
time_function(fact_recur_memo3)(8000)
time_function(fact_recur_memo3)(8000)
# This algorithm seems to be a variation of previous one, but it performs better, maybe due to one assignment less.

# ----------------------------------------------------------------------------------------------------

factorials_4 = {}


def factorial_iter_memo(n):
    if n not in factorials_4:
        value = 1
        for n in range(1, n + 1):
            value *= n
            factorials_4[n] = value
    return factorials_4[n]


print('\nFactorial iterative with memoization')
time_function(factorial_iter_memo)(3500)
time_function(factorial_iter_memo)(3500)
time_function(factorial_iter_memo)(5000)
time_function(factorial_iter_memo)(8000)
time_function(factorial_iter_memo)(8000)

print('Cache RESET')
factorials_4.clear()
time_function(factorial_iter_memo)(50000)

# TODO works up to 50000! (ca. 1.6 secs) but higher values will hang the system ==> try out on stronger system.
# TODO: Probably this is caused by searching for memoized/cached data => try with bisection search algorithms


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


print('\n--------------------------------------------------------')
# Reset cached/memoized data before performance test:
factorials_1.clear()
factorials_2.clear()
factorials_3.clear()
factorials_4.clear()


print('\nPERFORMANCE: iterative 1')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 20000, 90000, 90000):
    time_function(fact_iter1)(v)

print('\nPERFORMANCE: iterative 2')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 20000, 90000, 90000):
    time_function(fact_iter2)(v)


print('\nPERFORMANCE: recursive')
for v in (3000, 3000):
    time_function(fact_recur1)(v)
print('This algorithm can\'t do 5000!: Process finished with exit code -1073741571 (0xC00000FD)')

print('\nPERFORMANCE: recursive with memoization')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(fact_recur_memo1)(v)


print('\nPERFORMANCE: iterative with memoization')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(factorial_iter_memo)(v)

print('\nPERFORMANCE: iterative with memoization can do even more [from scratch, cached data reset]:')
factorials_4.clear()
for v in (50000, 60000):
    time_function(factorial_iter_memo)(v)


# CONCLUSION:
# ----------
# RECURSIVE:    Without memoization recursive algorithm is a joke.
# ITERATIVE:    performs very well for small numbers (up to 20000). But then it slows down significantly.
# RECURSIVE WITH MEMOIZATION: works well if it can populate its cache with gradually increasing searched n.
#                             It's potentially better than iterative for big numbers (only by gradually increasing n).
# ITERATIVE WITH MEMOIZATION: the most efficient one, can handle 50000 from scratch in 1.5 secs (though more hangs the
#                             system instead of throwing exception). It's slightly slower than recursive memo, but
#                             can handle much bigger leaps of n values than recursive.
#                             TODO Test theory that it's a problem with searching the dict. Use search algorithm !
