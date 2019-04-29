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
import sys
import time
import functools
from time_function_decorator import time_function

sys.setrecursionlimit(100000)

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH ITERATION AND  MULTIPLE ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def fib_iter(n):
    current = 0
    after = 1
    for _ in range(n):
        current, after = after, current + after
    return current


print('\nFibonacci iteration [YT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_iter(i), '', end='')
print('\nTime:', time.time() - timer)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH RECURSION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fib_recur1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recur1(n - 1) + fib_recur1(n - 2)

# This one is for real Fibonacci: where sequence starts from 1 rabbit.
# But for comparison purposes it's skipped - only those starting with 0 are printed out and compared.


# -----------------------------------------------------------------------------------------------------

def fib_recur2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur2(n - 1) + fib_recur2(n - 2)


# This recursive algorithm takes forever to handle range(111), hence lower range.
print('\nFibonacci recursion [MIT]')
timer = time.time()
for i in range(0, 20):
    print(fib_recur2(i), '', end='')
print('\nTime:', time.time() - timer)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH MEMOIZATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
# All three algorithms perform the same for n in range(0, 11111):
# fib_memo_mit(): Time: 1.7741012573242188, 1.786102294921875, 1.7611007690429688
# fib_memo(): 1.8361051082611084, 1.797102689743042, 1.920109748840332
# fib_memo2(): Time: 1.8981084823608398, 1.8031032085418701, 1.8231043815612793
# fib_decorated(): Time: 1.7651009559631348, 1.8391053676605225, 1.8151037693023682


d = {0: 0, 1: 1}


def fib_memo_mit(num):
    if num in d:
        return d[num]
    else:
        answer = fib_memo_mit(num - 1) + fib_memo_mit(num - 2)
        d[num] = answer
        return answer

# This algorithm from MIT lecture uses a 'starter' cache with two entries for base cases.
# However there's a more elegant solution to this problem (see below).


# -----------------------------------------------------------------------------------------------------

fib_cache1 = {}


def fib_memo(n):
    if n in fib_cache1:
        return fib_cache1[n]

    elif n == 0:
        val = 0
    elif n == 1:
        val = 1
    else:
        val = fib_memo(n-1) + fib_memo(n-2)

    fib_cache1[n] = val
    return val


# This one is MUCH more efficient than previous ones.
# It prints range(0, 111) in a second, whereas previous ones slow down by 20.
print('\nFibonacci recursive with memoization - version 1 [YT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_memo(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------

fib_cache2 = {}


def fib_memo2(n):
    if n in fib_cache2:
        return fib_cache2[n]
    elif n == 0:
        fib_cache2[n] = 0
    elif n == 1:
        fib_cache2[n] = 1
    else:
        fib_cache2[n] = fib_memo2(n-1) + fib_memo2(n-2)
    return fib_cache2[n]


print('\nFibonacci recursive with memoization  - version 2')
timer = time.time()
for i in range(0, 1111):
    print(fib_memo2(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------

fib_cache3 = {}


def fib_memo3(n):
    if n not in fib_cache3:
        if n == 0:
            fib_cache3[n] = 0
        elif n == 1:
            fib_cache3[n] = 1
        else:
            fib_cache3[n] = fib_memo3(n-1) + fib_memo3(n-2)
    return fib_cache3[n]


print('\nFibonacci recursive with memoization  - version 3')
timer = time.time()
for i in range(0, 1111):
    print(fib_memo3(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------


# Memoization can be done with module functools, decorator @lru_cache() [Last Recently Used]
@functools.lru_cache(maxsize=100000)
def fib_decorated(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_decorated(n-1) + fib_decorated(n-2)


print('\nFibonacci recursive with memoization  - with decorator [YT]')
timer = time.time()
for i in range(0, 1111):
    print(fib_decorated(i), '', end='')
print('\nTime:', time.time() - timer)


# -----------------------------------------------------------------------------------------------------------

# The golden ratio of Fibonacci sequence
print('\n\nRatio of increment:')
for i in range(1, 11):
    print(fib_decorated(i + 1) / fib_decorated(i))
print()

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

fib_cache1.clear()
fib_cache2.clear()
fib_cache3.clear()


print('\nPERFORMANCE: iterative')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500, 50000, 100000):
    time_function(fib_iter)(v)

print('\nPERFORMANCE: recursive')
print('Regular recursive algorithm performs so bad that it takes long even for range(111)')

print('\nPERFORMANCE: recursive + memoization MIT (with starter cache)')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(fib_memo_mit)(v)


print('\nPERFORMANCE: recursive + memoization 2')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(fib_memo2)(v)

print('\nPERFORMANCE: recursive + memoization 3')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(fib_memo3)(v)

print('\nPERFORMANCE: recursive + memoization decorated')
for v in (3000, 3000, 5000, 5000, 8000, 8000, 11500, 15000, 18500, 22000, 25500, 29000, 32500, 32500):
    time_function(fib_decorated)(v)

# CONCLUSION
# 1) Iterative algorithm for very big starting numbers performs better than recursive (can handle them).
#    What recursive algorithms with memoization can't even handle, iterative can.
# 2) However, recursive with memoization will perform better provided they have opportunity to build up their cache.
# 3) Surprisingly, decorated recursive with memoization can handle leap between 5000 and 8000. Implementation ?
