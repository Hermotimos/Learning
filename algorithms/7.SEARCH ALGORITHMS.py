"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: linear search, bisection search

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        Aditya Bhargava - Algorytmy. Ilustrowany przewodnik.
"""

UNSORTED_LETTERS = ['c', 'a', 'd', 'b', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 'z', 't', 'u', 'v', 'x', 'y']
SORTED_LETTERS = ['a', 'b', 'c', 'd', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
UNSORTED_NUMBERS = [4, 5, 6, 7, 1, 2, 3, 8, 9, 10, 13, 15, 16, 18, 31]
SORTED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16, 18, 31]
print(sorted(UNSORTED_NUMBERS))

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LINEAR SEARCH <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def linear_search_unsorted(iterable, searched):
    for e in iterable:
        if e == searched:
            return True
    return False


print('LINEAR SEARCH ON UNSORTED ITERABLE')
print(linear_search_unsorted(UNSORTED_NUMBERS, 4))
print(linear_search_unsorted(UNSORTED_NUMBERS, 11))
print(linear_search_unsorted(UNSORTED_NUMBERS, 44))
print(linear_search_unsorted(UNSORTED_LETTERS, 'z'))
print(linear_search_unsorted(UNSORTED_LETTERS, 'h'))
print()


# LINEAR SEARCH ON SORTED ITERABLE


def linear_search_sorted(iterable, searched):
    for e in iterable:
        if e == searched:
            return True
        elif e > searched:
            return False
    return False


print('LINEAR SEARCH ON SORTED ITERABLE - 1')
print(linear_search_sorted(SORTED_NUMBERS, 4))
print(linear_search_sorted(SORTED_NUMBERS, 44))
print(linear_search_sorted(SORTED_NUMBERS, 11))
print(linear_search_sorted(SORTED_LETTERS, 'z'))
print(linear_search_sorted(SORTED_LETTERS, 'h'))
print()


def linear_search_sorted2(iterable, elem):
    indx = 0
    while indx < len(iterable):
        if iterable[indx] == elem:
            return True
        else:
            indx += 1
    return False


print('LINEAR SEARCH ON SORTED ITERABLE - 2')
print(linear_search_sorted2(SORTED_NUMBERS, 4))
print(linear_search_sorted2(SORTED_NUMBERS, 44))
print(linear_search_sorted2(SORTED_NUMBERS, 11))
print(linear_search_sorted2(SORTED_LETTERS, 'z'))
print(linear_search_sorted2(SORTED_LETTERS, 'h'))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>> BISECTION SEARCH [REQUIRES SORTED ITERABLE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) Aditya Bhardava - iterative bisection
# there was no division //2 in the book - must be a mistake, cause without it it's not a bisection
# Cost must be O(log n) because there's no copying of the iterable - it's like pointers.

def bisection_iter(iterable, elem):
    low = 0
    high = len(iterable) - 1

    while low <= high:
        guess = (low + high) // 2
        if iterable[guess] == elem:
            return guess
        if iterable[guess] > elem:
            high = guess - 1
        else:
            low = guess + 1
    return False


print('BISECTION SEARCH ITERATIVE - Aditya Bhargava - Algorytmy. Ilustrowany przewodnik')
print(bisection_iter(SORTED_NUMBERS, 4))
print(bisection_iter(SORTED_NUMBERS, 44))
print(bisection_iter(SORTED_NUMBERS, 11))
print(bisection_iter(SORTED_LETTERS, 'z'))
print(bisection_iter(SORTED_LETTERS, 'h'))
print()


# 2) ALGORITHM WITH COPYING OF THE LIST => cost O(n)
# cost of recursion is O(log n) but cost of copying the list is O(n)


def bisection_search(iterable, searched):
    if len(iterable) == 0:
        return False
    elif len(iterable) == 1:
        return iterable[0] == searched
    else:
        half = len(iterable) // 2
        if iterable[half] > searched:
            return bisection_search(iterable[:half], searched)
        else:
            return bisection_search(iterable[half:], searched)


def bisection_search2(iterable, searched):
    if len(iterable) == 0:
        return False
    elif len(iterable) == 1:
        return iterable[0] == searched

    half = len(iterable) // 2
    if iterable[half] > searched:
        return bisection_search2(iterable[:half], searched)
    else:
        return bisection_search2(iterable[half:], searched)


print('BISECTION SEARCH RECURSIVE - WITH COPYING')
print(bisection_search(SORTED_NUMBERS, 4))
print(bisection_search(SORTED_NUMBERS, 44))
print(bisection_search(SORTED_NUMBERS, 11))
print(bisection_search(SORTED_LETTERS, 'z'))
print(bisection_search(SORTED_LETTERS, 'h'))
print()


# 3) ALGORITHM WITHOUT COPYING OF THE LIST => cost O(log n)
# uses pointers instead of copying iterable
# MY OWN ALGORITHM - SIMPLER THAN THE ONE FROM MIT LECTURE


def bisection_search_efficient_1(iterable, searched, low=0, high=None):
    if len(iterable) == 0:
        return False

    if high is None:
        high = len(iterable)
    if len(iterable[low:high]) == 1:
        return iterable[0] == searched

    middle = (low + high) // 2
    if iterable[middle] == searched:
        return True
    elif iterable[middle] > searched:
        high = middle
    else:
        low = middle
    return bisection_search_efficient_1(iterable, searched, low, high)


print('BISECTION SEARCH RECURSIVE - WITH POINTERS')
print(bisection_search_efficient_1(SORTED_NUMBERS, 4))
print(bisection_search_efficient_1(SORTED_NUMBERS, 44))
print(bisection_search_efficient_1(SORTED_NUMBERS, 11))
print(bisection_search_efficient_1(SORTED_LETTERS, 'z'))
print(bisection_search_efficient_1(SORTED_LETTERS, 'h'))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')


# LINEAR SEARCH ON UNSORTED ITERABLE
def linear_search_unsorted(iterable, searched):
    found = False
    steps = 0
    for e in iterable:
        steps += 1
        if e == searched:
            found = True
    return f"""Steps: {steps:5}\t{'not ' if found == False else "":}found '{searched}' in {len(iterable)} elements"""


print('LINEAR SEARCH ON UNSORTED ITERABLE')
print(linear_search_unsorted(UNSORTED_NUMBERS, 4))
print(linear_search_unsorted(UNSORTED_NUMBERS, 11))
print(linear_search_unsorted(UNSORTED_NUMBERS, 44))
print(linear_search_unsorted(UNSORTED_LETTERS, 'z'))
print(linear_search_unsorted(UNSORTED_LETTERS, 'h'))
print()


# LINEAR SEARCH ON SORTED ITERABLE
def linear_search_sorted(iterable, searched):
    found = False
    steps = 0
    for e in range(len(iterable)):
        steps += 1
        if iterable[e] == searched:
            found = True
            break
        elif iterable[e] > searched:
            break
    return f"""Steps: {steps:5}\t{'not ' if found == False else "":}found '{searched}' in {len(iterable)} elements"""


print('LINEAR SEARCH ON SORTED ITERABLE')
print(linear_search_sorted(SORTED_NUMBERS, 4))
print(linear_search_sorted(SORTED_NUMBERS, 44))
print(linear_search_sorted(SORTED_NUMBERS, 11))
print(linear_search_sorted(SORTED_LETTERS, 'z'))
print(linear_search_sorted(SORTED_LETTERS, 'h'))
print()


def linear_search_sorted2(iterable, searched):
    indx = 0
    steps = 0
    found = False
    while indx < len(iterable):
        steps += 1
        if iterable[indx] == searched:
            found = True
            break
        elif iterable[indx] > searched:
            break
        else:
            indx += 1
    return f"""Steps: {steps:5}\t{'not ' if found == False else "":}found '{searched}' in {len(iterable)} elements"""


print('LINEAR SEARCH ON SORTED ITERABLE - 2')
print(linear_search_sorted2(SORTED_NUMBERS, 4))
print(linear_search_sorted2(SORTED_NUMBERS, 44))
print(linear_search_sorted2(SORTED_NUMBERS, 11))
print(linear_search_sorted2(SORTED_LETTERS, 'z'))
print(linear_search_sorted2(SORTED_LETTERS, 'h'))
print()

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>> BISECTION SEARCH [REQUIRES SORTED ITERABLE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) ITERATIVE BINARY SEARCH

def bisection_iter(iterable, searched):
    low = 0
    high = len(iterable) - 1
    steps = 0
    found = False

    while low <= high:
        steps += 1
        guess = (low + high) // 2
        if iterable[guess] == searched:
            found = True
            return f"Steps: {steps:5}\t{'not ' if found == False else '':}found '{searched}' in {len(iterable)} elements"
        if iterable[guess] > searched:
            high = guess - 1
        else:
            low = guess + 1
    return f"Steps: {steps:5}\t{'not ' if found == False else '':}found '{searched}' in {len(iterable)} elements"


print('BISECTION SEARCH ITERATIVE - Aditya Bhargava - Algorytmy. Ilustrowany przewodnik')
print(bisection_iter(SORTED_NUMBERS, 4))
print(bisection_iter(SORTED_NUMBERS, 44))
print(bisection_iter(SORTED_NUMBERS, 11))
print(bisection_iter(SORTED_LETTERS, 'z'))
print(bisection_iter(SORTED_LETTERS, 'h'))
print()


# 2) RECURSIVE ALGORITHM WITH COPYING OF THE LIST => cost O(n)

def bisection_search(iterable, searched):
    if len(iterable) == 0:
        return False
    elif len(iterable) == 1:
        return iterable[0] == searched
    else:
        half = len(iterable) // 2
        if iterable[half] > searched:
            return bisection_search(iterable[:half], searched)
        else:
            return bisection_search(iterable[half:], searched)


print('BISECTION SEARCH - WITH COPYING')
print('No steps printout by recursion')
print(bisection_search(SORTED_NUMBERS, 4))
print(bisection_search(SORTED_NUMBERS, 44))
print(bisection_search(SORTED_NUMBERS, 11))
print(bisection_search(SORTED_LETTERS, 'z'))
print(bisection_search(SORTED_LETTERS, 'h'))
print()


# 2) MY RECURSIVE ALGORITHM WITHOUT COPYING => cost O(log n)

def bisection_search_efficient_1(iterable, searched, low=0, high=0):
    if high == 0:
        high = len(iterable)

    if len(iterable) == 0:
        return False
    elif len(iterable[low:high]) == 1:
        return iterable[0] == searched
    else:
        middle = (low + high) // 2
        if iterable[middle] == searched:
            return True
        elif iterable[middle] > searched:
            high = middle
        else:
            low = middle
        return bisection_search_efficient_1(iterable, searched, low, high)


print('BISECTION SEARCH - WITH POINTERS')
print('No steps printout by recursion')
print(bisection_search_efficient_1(SORTED_NUMBERS, 4))
print(bisection_search_efficient_1(SORTED_NUMBERS, 44))
print(bisection_search_efficient_1(SORTED_NUMBERS, 11))
print(bisection_search_efficient_1(SORTED_LETTERS, 'z'))
print(bisection_search_efficient_1(SORTED_LETTERS, 'h'))
print()
