"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: guess, approximation and bisection algorithms

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.youtube.com/watch?v=7k7tMKxH6Dg
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH DICT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
def fib_with_dict(num):
    d = {0: 0, 1: 1}        # serves as starting point
    if num in d:
        return d[num]
    else:
        answer = fib_with_dict(num - 1) + fib_with_dict(num - 2)
        d[num] = answer
        return answer


print('\nFibonacci with dict MIT')
for i in range(0, 11):
    print(fib_with_dict(i), '', end='')


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI WITH FORESIGHT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fibonacci(n):
    current = 0
    after = 1
    for _ in range(n):
        current, after = after, current + after
    return current


# This one always keeps track of the next value in sequence, hence 'foresight'
print('\nFibonacci YT')
for i in range(0, 11):
    print(fibonacci(i), '', end='')


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIBONACCI SIMPLEST<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def fib_mit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_mit(n-1) + fib_mit(n-2)


print('\nFibonacci simplest MIT')
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


print('\nFibonacci simplest MIT without bug')
for i in range(0, 11):
    print(fib_simplest(i), '', end='')
