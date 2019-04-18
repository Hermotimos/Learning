"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - memoization

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.youtube.com/watch?v=7k7tMKxH6Dg
        https://www.youtube.com/watch?v=Qk0zUZW-U_M
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH ITERATION AND  MULTIPLE ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fibonacci(n):
    current = 0
    after = 1
    for _ in range(n):
        current, after = after, current + after
    return current


# This one always keeps track of the next value in sequence, hence 'foresight'
print('\nFibonacci with iteration and multiple assignment [YT]')
for i in range(0, 11):
    print(fibonacci(i), '', end='')


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH RECURSION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fib_mit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_mit(n-1) + fib_mit(n-2)


print('\nFibonacci with recursion [MIT]')
for i in range(0, 11):
    print(fib_mit(i), '', end='')
# Printout shows bug in this algorithm. It's one step too far into the Fibonacci (skipped value for 0).
# Bug: n == 0 should return 0


def fib_simplest(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_simplest(n-1) + fib_simplest(n-2)


print('\nFibonacci with recursion without bug [MIT]')
for i in range(0, 11):
    print(fib_simplest(i), '', end='')


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH MEMOIZATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
def fib_with_dict(num):
    if num in d:
        return d[num]
    else:
        answer = fib_with_dict(num - 1) + fib_with_dict(num - 2)
        d[num] = answer
        return answer


d = {0: 0, 1: 1}
print('\nFibonacci with memoization: dict with starting values, serves as cache [MIT]')
for i in range(0, 111):
    print(fib_with_dict(i), '', end='')


# -----------------------------------------------------------------------------------------------------
fib_cache = {}


def fib_memo(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        val = 0
    elif n == 1:
        val = 1
    elif n > 1:
        val = fib_memo(n-1) + fib_memo(n-2)

    fib_cache[n] = val
    return val


# This one is MUCH more efficient.
# It prints out range(0, 111) in a second, whereas all the above slow down by 20th.
print('\nFibonacci with memoization: no starter, build inner data itself [YT]')
for i in range(0, 111):
    print(fib_memo(i), '', end='')


# Memoization can be done with module functools, decorator @lru_cache() [Last Recently Used]
import functools


@functools.lru_cache(maxsize=1000)
def fib_decorated(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib_decorated(n-1) + fib_decorated(n-2)


print('\nFibonacci with memoization: with decorator [YT]')
for i in range(0, 111):
    print(fib_decorated(i), '', end='')


# The golden ratio of Fibonacci sequence
print('\n\nRatio of increment:')
for i in range(1, 11):
    print(fib_decorated(i + 1) / fib_decorated(i))
