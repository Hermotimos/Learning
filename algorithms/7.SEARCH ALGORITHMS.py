"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: linear search, bisection search, todo ..............

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""

UNSORTED_LETTERS = ['c', 'a', 'd', 'b', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 'z', 't', 'u', 'v', 'x', 'y']
SORTED_LETTERS = ['a', 'b', 'c', 'd', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
UNSORTED_NUMBERS = [4, 5, 6, 7, 1, 2, 3, 8, 9, 10, 13, 15, 16, 18, 31]
SORTED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16, 18, 31]

UNSORTED_LETTERS_TUPLE = ('c', 'a', 'd', 'b', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 'z', 't', 'u', 'v', 'x', 'y')
SORTED_LETTERS_TUPLE = ('a', 'b', 'c', 'd', 'g', 'j', 'k', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
UNSORTED_NUMBERS_TUPLE = (4, 5, 6, 7, 1, 2, 3, 8, 9, 10, 13, 15, 16, 18, 31)
SORTED_NUMBERS_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16, 18, 31)

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


print('LINEAR SEARCH ON SORTED ITERABLE')
print(linear_search_sorted(SORTED_NUMBERS, 4))
print(linear_search_sorted(SORTED_NUMBERS, 44))
print(linear_search_sorted(SORTED_NUMBERS, 11))
print(linear_search_sorted(SORTED_LETTERS, 'z'))
print(linear_search_sorted(SORTED_LETTERS, 'h'))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>> BISECTION SEARCH [REQUIRES SORTED ITERABLE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) ALGORITHM WITH COPYING OF THE LIST => cost O(n)
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


print('BISECTION SEARCH - WITH COPYING')
print(bisection_search(SORTED_NUMBERS, 4))
print(bisection_search(SORTED_NUMBERS, 44))
print(bisection_search(SORTED_NUMBERS, 11))
print(bisection_search(SORTED_LETTERS, 'z'))
print(bisection_search(SORTED_LETTERS, 'h'))
print()


# 2) MY ALGORITHM => cost O(log n)
# based on hint from MIT lecture to use pointers instead of copying iterable


def bisection_search_efficient_1(iterable, searched, low=0, high=None):
    if high is None:
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
            found = True                # returning True here would speed up, but not in worst case scenario (e absent)
    return f"""Steps: {steps:5}\t{'not ' if found == False else "":}found '{searched}' in {len(iterable)} elements"""


print('LINEAR SEARCH ON UNSORTED ITERABLE')
print(linear_search_unsorted(UNSORTED_NUMBERS, 4))
print(linear_search_unsorted(UNSORTED_NUMBERS, 11))
print(linear_search_unsorted(UNSORTED_NUMBERS, 44))
print(linear_search_unsorted(UNSORTED_LETTERS, 'z'))
print(linear_search_unsorted(UNSORTED_LETTERS, 'h'))
print()
print(linear_search_unsorted(UNSORTED_NUMBERS_TUPLE, 4))
print(linear_search_unsorted(UNSORTED_NUMBERS_TUPLE, 44))
print(linear_search_unsorted(UNSORTED_NUMBERS_TUPLE, 11))
print(linear_search_unsorted(UNSORTED_LETTERS_TUPLE, 'z'))
print(linear_search_unsorted(UNSORTED_LETTERS_TUPLE, 'h'))
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
        if iterable[e] > searched:
            break
    return f"""Steps: {steps:5}\t{'not ' if found == False else "":}found '{searched}' in {len(iterable)} elements"""


print('LINEAR SEARCH ON SORTED ITERABLE')
print(linear_search_sorted(SORTED_NUMBERS, 4))
print(linear_search_sorted(SORTED_NUMBERS, 44))
print(linear_search_sorted(SORTED_NUMBERS, 11))
print(linear_search_sorted(SORTED_LETTERS, 'z'))
print(linear_search_sorted(SORTED_LETTERS, 'h'))
print()
print(linear_search_sorted(SORTED_NUMBERS_TUPLE, 4))
print(linear_search_sorted(SORTED_NUMBERS_TUPLE, 44))
print(linear_search_sorted(SORTED_NUMBERS_TUPLE, 11))
print(linear_search_sorted(SORTED_LETTERS_TUPLE, 'z'))
print(linear_search_sorted(SORTED_LETTERS_TUPLE, 'h'))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>> BISECTION SEARCH [REQUIRES SORTED ITERABLE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) ALGORITHM WITH COPYING OF THE LIST => cost O(n)

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
print(bisection_search(SORTED_NUMBERS, 4))
print(bisection_search(SORTED_NUMBERS, 44))
print(bisection_search(SORTED_NUMBERS, 11))
print(bisection_search(SORTED_LETTERS, 'z'))
print(bisection_search(SORTED_LETTERS, 'h'))
print()
print(bisection_search(SORTED_NUMBERS_TUPLE, 4))
print(bisection_search(SORTED_NUMBERS_TUPLE, 44))
print(bisection_search(SORTED_NUMBERS_TUPLE, 11))
print(bisection_search(SORTED_LETTERS_TUPLE, 'z'))
print(bisection_search(SORTED_LETTERS_TUPLE, 'h'))
print()


# 2) MY ALGORITHM => cost O(log n)

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
print(bisection_search_efficient_1(SORTED_NUMBERS, 4))
print(bisection_search_efficient_1(SORTED_NUMBERS, 44))
print(bisection_search_efficient_1(SORTED_NUMBERS, 11))
print(bisection_search_efficient_1(SORTED_LETTERS, 'z'))
print(bisection_search_efficient_1(SORTED_LETTERS, 'h'))
print()
print(bisection_search_efficient_1(SORTED_NUMBERS_TUPLE, 4))
print(bisection_search_efficient_1(SORTED_NUMBERS_TUPLE, 44))
print(bisection_search_efficient_1(SORTED_NUMBERS_TUPLE, 11))
print(bisection_search_efficient_1(SORTED_LETTERS_TUPLE, 'z'))
print(bisection_search_efficient_1(SORTED_LETTERS_TUPLE, 'h'))
print()
