"""
    This file is for learning and exercise purposes.

    Topics:
        - all algorithms from directory in one place.

    Sources:
        In separate files.
"""

# //////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////// MULTIPLICATION ///////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// MULTIPLICATION ITERATIVE -1- ////////////

def multiply1(a, b):
    res = 0
    for _ in range(abs(b)):
        res += a
    if b < 0:
        res = -res
    return res


def multiply11(a, b):
    res = 0
    for _ in range(abs(b)):
        res += a
    return -res if b < 0 else res


# //////////// MULTIPLICATION ITERATIVE -2- ////////////

def multiply2(a, b):
    res = 0
    iters = abs(b)
    while iters > 0:
        res += a
        iters -= 1
    if b < 0:
        res = -res
    return res


def multiply22(a, b):
    res = 0
    iters = abs(b)
    while iters > 0:
        res += a
        iters -= 1
    return -res if b < 0 else res


# //////////// MULTIPLICATION RECURSIVE -1- ////////////

def multiply3(a, b):
    if b == 0:
        return 0
    else:
        res = a + multiply3(a, abs(b)-1)
        if res < 0:
            res = -res
        return res


def multiply33(a, b):
    if b == 0:
        return 0
    res = a + multiply3(a, abs(b)-1)
    return -res if b < 0 else res


# //////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// FACTORIAL //////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// FACTORIAL ITERATIVE -1- ////////////

def factorial1(n):
    res = 1
    for x in range(1, n+1):
        res *= x
    return res


# //////////// FACTORIAL ITERATIVE -2- ////////////

def factorial2(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res


# //////////// FACTORIAL RECURSIVE -1- ////////////

def factorial3(n):
    if n < 2:
        return 1
    else:
        return n * factorial3(n-1)


# //////////// FACTORIAL ITERATIVE WITH MEMOIZATION -1- ////////////

factorials1 = {}


def fact1(n):
    if n in factorials1:
        return factorials1[n]
    else:
        res = 1
        for n in range(1, n+1):
            res *= n
            factorials1[n] = res
        return res


def fact11(n):
    if n not in factorials1:
        res = 1
        for n in range(1, n+1):
            res *= n
            factorials1[n] = res
    return factorials1[n]


# //////////// FACTORIAL RECURSIVE WITH MEMOIZATION -1- ////////////

factorials2 = {}


def fact2(n):
    if n in factorials2:
        return factorials2[n]
    else:
        if n < 2:
            res = 1
        else:
            res = n * fact2(n-1)
    factorials2[n] = res
    return res


def fact22(n):
    if n in factorials2:
        return factorials2[n]
    res = 1 if n < 2 else n * fact22(n-1)
    factorials2[n] = res
    return res


def fact222(n):
    if n not in factorials2:
        res = 1 if n < 2 else n * fact222(n-1)
        factorials2[n] = res
    return factorials2[n]


# //////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// FIBONACCI //////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// FIBONACCI ITERATIVE -1- ////////////

def fib1(n):
    current = 0
    after = 1
    for n in range(n):
        current, after = after, current + after
    return current


# //////////// FIBONACCI RECURSIVE -1- ////////////

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


# //////////// FIBONACCI RECURSIVE WITH MEMOIZATION -1- ////////////

fibonacci = {}


def fib3(n):
    if n in fibonacci:
        return fibonacci[n]
    else:
        if n == 0:
            res = 0
        elif n < 3:
            res = 1
        else:
            res = fib3(n-1) + fib3(n-2)
        fibonacci[n] = res
    return res


def fib33(n):
    if n not in fibonacci:
        if n == 0:
            res = 0
        elif n < 3:
            res = 1
        else:
            res = fib33(n-1) + fib33(n-2)
        fibonacci[n] = res
    return fibonacci[n]


def fib333(n):
    if n not in fibonacci:
        if n == 0:
            fibonacci[n] = 0
        elif n < 3:
            fibonacci[n] = 1
        else:
            fibonacci[n] = fib333(n-1) + fib333(n-2)
    return fibonacci[n]


# //////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// CUBE ROOT //////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
# ALL SOLS ARE ITERATIVE
# TODO test these algorithms, because they have been reshaped (simplified or shortened)


# //////////// GUESS&CHECK FOR POSITIVE NUMBERS ONLY -1- ////////////

def cube_root1(n):
    for guess in range(n+1):
        if guess**3 == n:
            return f'Cube root of {n} is {guess}'
    return f'{n} is not a perfect cube'


# //////////// GUESS&CHECK FOR POSITIVE & NEGATIVE NUMBERS -1- ////////////

def cube_root2(n):
    for guess in range(abs(n)+1):
        if guess**3 == abs(n):
            if n < 0:
                guess = -guess
            return f'Cube root of {n} is {guess}'
        elif guess**3 > abs(n):
            return f'{n} is not a perfect cube'


def cube_root22(n):
    for guess in range(abs(n)+1):
        if guess**3 == abs(n):
            guess = -guess if n < 0 else guess
            return f'Cube root of {n} is {guess}'
        elif guess**3 > abs(n):
            return f'{n} is not a perfect cube'
