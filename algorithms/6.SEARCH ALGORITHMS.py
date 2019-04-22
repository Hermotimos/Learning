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
    for e in iterable:
        if e == searched:
            found = True
    print(found)


linear_search_unsorted(UNSORTED_NUMBERS, 4)
linear_search_unsorted(UNSORTED_NUMBERS, 44)
linear_search_unsorted(UNSORTED_LETTERS, 'z')
linear_search_unsorted(UNSORTED_LETTERS, 'h')
linear_search_unsorted(SORTED_LETTERS, 'a')
print()
linear_search_unsorted(UNSORTED_NUMBERS_TUPLE, 4)
linear_search_unsorted(UNSORTED_NUMBERS_TUPLE, 44)
linear_search_unsorted(UNSORTED_LETTERS_TUPLE, 'z')
linear_search_unsorted(UNSORTED_LETTERS_TUPLE, 'h')
print()


def linear_search_sorted(iterable, searched):
    for e in range(len(iterable)):
        if iterable[e] == searched:
            return True
