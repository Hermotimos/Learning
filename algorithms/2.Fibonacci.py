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
import time

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
timer = time.time()
for i in range(0, 111):
    print(fibonacci(i), '', end='')
print('\nTime:', time.time() - timer)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH RECURSION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fib_mit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_mit(n-1) + fib_mit(n-2)


# This one is for real Fibonacci: where sequence starts from 1 rabbit.
print('\nFibonacci with recursion [MIT]')
timer = time.time()
for i in range(0, 20):                      # This one takes forever to handle range(0, 111), hence lowered range.
    print(fib_mit(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------
def fib_mit_better(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_mit_better(n - 1) + fib_mit_better(n - 2)


# This one is for sequence starting with 0.
print('\nFibonacci with recursion without bug [MIT]')
timer = time.time()
for i in range(0, 20):                      # This one takes forever to handle range(0, 111), hence lowered range.
    print(fib_mit_better(i), '', end='')
print('\nTime:', time.time() - timer)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH MEMOIZATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# All three algorithms perform the same for n in range(0, 11111):
# fib_with_dict(): Time: 1.7741012573242188, 1.786102294921875, 1.7611007690429688
# fib_memo(): 1.8361051082611084, 1.797102689743042, 1.920109748840332
# fib_memo2(): Time: 1.9261102676391602; 1.8461055755615234; 1.8511056900024414
# fib_decorated(): Time: 1.7651009559631348, 1.8391053676605225, 1.8151037693023682


def fib_with_dict(num):
    if num in d:
        return d[num]
    else:
        answer = fib_with_dict(num - 1) + fib_with_dict(num - 2)
        d[num] = answer
        return answer


d = {0: 0, 1: 1}
print('\nFibonacci with memoization: dict with starting values, serves as cache [MIT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_with_dict(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------
fib_cache = {}


def fib_memo(n):
    if n in fib_cache:
        return fib_cache[n]

    elif n == 0:
        val = 0
    elif n == 1:
        val = 1
    else:
        val = fib_memo(n-1) + fib_memo(n-2)

    fib_cache[n] = val
    return val


# This one is MUCH more efficient.
# It prints out range(0, 111) in a second, whereas all the above slow down by 20th.
print('\nFibonacci with memoization: no starter, builds inner data itself [YT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_memo(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------
fib_cache2 = {}


def fib_memo2(n):
    if n in fib_cache2:
        return fib_cache2[n]
    else:
        if n == 0:
            val = 0
        elif n == 1:
            val = 1
        else:
            val = fib_memo(n-1) + fib_memo(n-2)

        fib_cache[n] = val
        return val


print('\nFibonacci with memoization version 2: no starter [experiments]')
timer = time.time()
for i in range(0, 1111):
    print(fib_memo2(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------
# Memoization can be done with module functools, decorator @lru_cache() [Last Recently Used]
import functools


@functools.lru_cache(maxsize=1000)
def fib_decorated(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_decorated(n-1) + fib_decorated(n-2)


print('\nFibonacci with memoization: with decorator [YT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_decorated(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------------

# The golden ratio of Fibonacci sequence
print('\n\nRatio of increment:')
for i in range(1, 11):
    print(fib_decorated(i + 1) / fib_decorated(i))
