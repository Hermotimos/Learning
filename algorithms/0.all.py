"""
    This file is for learning and exercise purposes.

    Topics:
        - all algorithms from the directory in one place.

    Sources:
        Indicated in separate files.
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
        if b < 0:
            res = -res
        return res


def multiply33(a, b):
    if b == 0:
        return 0
    res = a + multiply3(a, abs(b)-1)
    return -res if b < 0 else res


def multiply333(a, b):
    if b == 1:
        return a
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
    if n < 2:
        factorials2[n] = 1
    else:
        factorials2[n] = n * fact22(n-1)
    return factorials2[n]


# //////////// FACTORIAL RECURSIVE WITH MEMOIZATION -2- ////////////

factorials3 = {}


def fact3(n):
    if n in factorials3:
        return factorials3[n]
    res = 1 if n < 2 else n * fact3(n-1)
    factorials3[n] = res
    return res


def fact33(n):
    if n not in factorials3:
        res = 1 if n < 2 else n * fact33(n-1)
        factorials3[n] = res
    return factorials3[n]


def fact333(n):
    if n not in factorials3:
        factorials3[n] = 1 if n < 2 else n * fact333(n-1)
    return factorials3[n]


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


# //////////// GUESS&CHECK FOR POSITIVE NUMBERS ////////////

def cube_root1(n):
    for guess in range(n+1):
        if guess**3 == n:
            return f'Cube root of {n} is {guess}'
    return f'{n} is not a perfect cube'


# //////////// GUESS&CHECK FOR POSITIVE & NEGATIVE NUMBERS ////////////

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
            return f'Cube root of {n} is {-guess if n < 0 else guess}'
        elif guess**3 > abs(n):
            return f'{n} is not a perfect cube'


# //////////// APPROXIMATION FOR POSITIVE AND NEGATIVE NUMBERS ////////////

def cube_root3(n, tolerance=0.01, increment=0.01):
    approx = 0.0
    while (abs(n) - approx**3) > tolerance:
        approx += increment
    if n < 0:
        approx = -approx
    return approx


def cube_root33(n, tolerance=0.01, increment=0.01):
    approx = 0.0
    while (abs(n) - approx**3) > tolerance:
        approx += increment
    return -approx if n < 0 else approx


# //////////// BISECTION SEARCH FOR POSITIVE AND NEGATIVE NUMBERS [ITERATIVE] ////////////

def cube_root4(n, tolerance=0.01):
    low = 0
    high = abs(n)
    guess = (low + high) / 2
    while abs(abs(n) - guess**3) > tolerance:
        if guess**3 > abs(n):
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    if n < 0:
        guess = -guess
    return guess


def cube_root44(n, tolerance=0.01):
    low, high = 0, abs(n)
    guess = (low + high) / 2
    while abs(abs(n) - guess**3) > tolerance:
        if guess**3 > abs(n):
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    return -guess if n < 0 else guess


# //////////// BISECTION SEARCH FOR POSITIVE, NEGATIVE, AND FRACTIONS [ITERATIVE] ////////////

def cube_root5(n, tolerance=0.01):
    if abs(n) < 1:
        low, high = abs(n), 1
    else:
        low, high = 0, abs(n)
    guess = (low + high) / 2

    while abs(abs(n) - guess**3) > tolerance:
        if guess**3 > abs(n):
            high = guess
        else:
            low = guess
        guess = (low + high) / 2

    return -guess if n < 0 else guess


# //////////// BISECTION SEARCH FOR POSITIVE, NEGATIVE [RECURSIVE] ////////////

def cube_root6(n, low=0, high=0, tolerance=0.01):
    if high == 0:                                   # high == 0 only in the first step
        high = abs(n)
    guess = (low + high) / 2

    if abs(abs(n) - guess**3) <= tolerance:
        return -guess if n < 0 else guess

    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root6(n, low, high, tolerance)


# //////////// BISECTION SEARCH FOR POSITIVE, NEGATIVE, AND FRACTIONS [RECURSIVE] ////////////

def cube_root7(n, low=0, high=0, tolerance=0.01):
    if high == 0:                                   # high == 0 only in the first step
        if abs(n) < 1:
            low, high = abs(n), 1
        else:
            low, high = 0, abs(n)
    guess = (low + high) / 2

    if abs(abs(n) - guess**3) <= tolerance:
        return -guess if n < 0 else guess

    elif guess**3 > abs(n):
        high = guess
    else:
        low = guess
    return cube_root7(n, low, high, tolerance)


def cube_root8(n, low=0, high=0, tolerance=0.01):
    if high == 0:
        if abs(n) < 1:
            low, high = abs(n), 1
        else:
            low, high = 0, abs(n)
    guess = (low + high) / 2

    if abs(abs(n) - guess**3) > tolerance:
        if guess**3 > abs(n):
            high = guess
        else:
            low = guess
        return cube_root8(n, low, high, tolerance)
    else:
        return -guess if n < 0 else guess


# //////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////// PALINDROME /////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// PALINDROME SIMPLEST ////////////

def palindrome1(text):
    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')

    if len(text) == 0:
        return False
    return text == text[::-1]


def palindrome11(text):
    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')
    return len(text) != 0 and text == text[::-1]


# //////////// PALINDROME ITERATIVE ////////////

def palindrome2(text):
    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')

    if len(text) == 0:
        return False
    for n in range(1, len(text) // 2):
        if text[n-1] != text[-n]:
            return False
    return True


# //////////// PALINDROME RECURSIVE -1- ////////////

def palindrome3(text):
    if len(text) <= 1:
        return True

    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')

    if text[0] != text[-1]:
        return False
    else:
        check = palindrome3(text[1:-1])
    return check


def palindrome33(text):
    if len(text) <= 1:
        return True

    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')

    if text[0] != text[-1]:
        return False
    return palindrome33(text[1:-1])


def palindrome333(text):
    if len(text) <= 1:
        return True

    text = str(text).lower()
    for d in text:
        if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(d, '')

    return text[0] == text[-1] and palindrome333(text[1:-1])


# //////////// PALINDROME RECURSIVE -2- ////////////

def palindrome4(text):
    def convert_to_digits(string):
        string = str(string).lower()
        for d in string:
            if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                string = string.replace(d, '')
        return string

    def is_palindrome(string):
        if len(string) <= 1:
            return True
        return string[0] == string[-1] and is_palindrome(string[1:-1])

    text = convert_to_digits(text)
    if len(text) == 0:
        return False
    return is_palindrome(text)


def palindrome44(text):
    def convert_to_digits(string):
        string = str(string).lower()
        for d in string:
            if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                string = string.replace(d, '')
        return string

    def is_palindrome(string):
        if len(string) <= 1:
            return True
        return string[0] == string[-1] and is_palindrome(string[1:-1])

    text = convert_to_digits(text)
    return len(text) != 0 and is_palindrome(text)


# //////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// TOWERS OF HANOI ///////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


def hanoi1(height, source, middle, target):
    if height == 0:
        return
    hanoi1(height-1, source, target, middle)
    if source:
        target.append(source.pop())
    hanoi1(height-1, middle, source, target)


def hanoi2(height, source, target, middle):
    if height == 1:
        target.append(source.pop())
    else:
        hanoi2(height-1, source, middle, target)
        hanoi2(1, source, target, middle)
        hanoi2(height-1, middle, target, source)


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////// SEARCH //////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// LINEAR SEARCH (ITERATIVE) - UNSORTED LIST ////////////

def search(elem, iterable):
    for e in iterable:
        if e == elem:
            return True
    return False


# //////////// LINEAR SEARCH (ITERATIVE) - SORTED LIST ////////////

def search1(elem, iterable):
    for e in iterable:
        if e == elem:
            return True
        elif e > elem:
            return False
    return False


def search2(elem, iterable):
    indx = 0
    while indx < len(iterable):
        if iterable[indx] == elem:
            return True
        elif iterable[indx] > elem:
            return False
        else:
            indx += 1
    return False


# //////////// BINARY SEARCH (RECURSIVE) - INEFFICIENT ////////////

def search3(elem, iterable):
    if len(iterable) == 0:
        return False
    elif len(iterable) == 1:
        return iterable[0] == elem

    guess = len(iterable) // 2
    if iterable[guess] > elem:
        return search3(elem, iterable[:guess])
    else:
        return search3(elem, iterable[guess:])


# //////////// BINARY SEARCH (RECURSIVE) - EFFICIENT ////////////

def search4(elem, iterable, low=0, high=None):
    if len(iterable) == 0:
        return False

    if high is None:
        high = len(iterable)
    if len(iterable[low:high]) == 1:
        return iterable[0] == elem

    guess = (low + high) // 2
    if iterable[guess] == elem:
        return True
    elif iterable[guess] > elem:
        high = guess
    else:
        low = guess
    return search4(elem, iterable, low, high)


# //////////// BINARY SEARCH (ITERATIVE) - EFFICIENT ////////////

def search5(elem, iterable):
    low = 0
    high = len(iterable) - 1

    while low <= high:
        guess = (low + high) // 2
        if iterable[guess] == elem:
            return True
        if iterable[guess] > elem:
            high = guess - 1
        else:
            low = guess + 1
    return False


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////// SORT ////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////


# //////////// BOGO SORT = MONKEY SORT = SHOTGUN SORT ////////////

def bogo_sort(list_):
    import random
    while not all(list_[n-1] <= list_[n] for n in range(1, len(list_))):
        random.shuffle(list_)
    return list_


# ////////////////// BUBBLE SORT //////////////////

def bubble_sort(list_):
    while True:
        swap = False
        for n in range(1, len(list_)):
            if list_[n-1] > list_[n]:
                list_[n-1], list_[n] = list_[n], list_[n-1]
                swap = True
            if not swap:
                return list_


def bubble_sort2(list_):
    while not all(list_[n-1] <= list_[n] for n in range(1, len(list_))):
        for n in range(1, len(list_)):
            if list_[n-1] > list_[n]:
                list_[n-1], list_[n] = list_[n], list_[n-1]
    return list_


# ////////////////// SELECTION SORT //////////////////

def selection_sort(list_):
    suffix = 0
    while suffix < len(list_):
        for n in range(suffix, len(list_)):
            if list_[suffix] > list_[n]:
                list_[suffix], list_[n] = list_[n], list_[suffix]
        suffix += 1
    return list_


def selection_sort2(unordered_list):
    def find_smallest(list_):
        smallest = list_[0]
        smallest_index = 0
        for e in range(1, len(list_)):
            if list_[e] < smallest:
                smallest = list_[e]
                smallest_index = e
        return smallest_index

    ordered_list = []
    for _ in range(len(unordered_list)):
        smallest_ = find_smallest(unordered_list)
        ordered_list.append(unordered_list.pop(smallest_))
    return ordered_list


# ////////////////// MERGE SORT //////////////////

def merge_sort(list_):

    def merge(left, right):
        result = []
        a, b = 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                result.append(left[a])
                a += 1
            else:
                result.append(right[b])
                b += 1
        while a < len(left):
            result.append(left[a])
            a += 1
        while b < len(right):
            result.append(right[b])
            b += 1
        return result

    if len(list_) < 2:
        return list_
    else:
        mid = len(list_) // 2
        half1 = merge_sort(list_[:mid])
        half2 = merge_sort(list_[mid:])
        return merge(half1, half2)


# ////////////////// QUICK SORT //////////////////

def quick_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        less = [i for i in list_[1:] if i < pivot]
        greater = [i for i in list_[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)