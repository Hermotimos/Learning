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


# //////////// FACTORIAL WITH MEMOIZATION ITERATIVE -1- ////////////

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


# //////////// FACTORIAL WITH MEMOIZATION RECURSIVE -1- ////////////

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
