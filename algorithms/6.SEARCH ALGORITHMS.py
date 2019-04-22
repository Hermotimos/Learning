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


