"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>> MONKEY SORT / BOGO SORT / SHOTGUN SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
import random


def is_sorted(iterable):
    return all(iterable[n] <= iterable[n + 1] for n in range(len(iterable)-1))


tuple1 = 1, 2, 3, 4
list1 = [1, 2, 3, 4, 4]
tuple2 = 1, 2, 3, 4, 3
list2 = [1, 2, 3, 4, 3, 4, 3]

print('Test is_sorted(): True, True, False, False')
print(is_sorted(tuple1))
print(is_sorted(list1))
print(is_sorted(tuple2))
print(is_sorted(list2))
print()


def bogo_sort(iterable, shuffle_counter=0):
    print(f'Start: {iterable}')
    while not is_sorted(iterable):
        random.shuffle(iterable)
        shuffle_counter += 1
    print(f'Steps needed: {shuffle_counter}: {iterable}')


print('MONKEY SEARCH / BOGO SEARCH / SHOTGUN SEARCH')
list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bogo_sort(list1)
print('\nlist2'), bogo_sort(list2)
# print('\nlist3'), bogo_sort(list3)        # Woooops... this probably takes hours.
print()
# This algorithm will eventually sort short lists.
# 10 trials for a 7-element iterable: 327, 325, 235, 204, 169, 421, 401, 593, 3, 391. Generally seen range 3 - 2400 !!!
# Order of growth O is here unbounded in the worst case scenario.


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BUBBLE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def bubble_sort(iterable):
    while True:
        swap = True
        for e in range(1, len(iterable)):
            if iterable[e - 1] > iterable[e]:
                swap = False
                iterable[e - 1], iterable[e] = iterable[e], iterable[e - 1]
        if swap:
            return iterable


# VERSION WITH PRINTOUT:
def bubble_sort2(iterable, printout=True):
    print(f'Start: {iterable}') if printout else None
    step_count = 0
    while True:
        swap = True
        for e in range(1, len(iterable)):
            if iterable[e - 1] > iterable[e]:
                swap = False
                step_count += 1
                iterable[e - 1], iterable[e] = iterable[e], iterable[e - 1]
                print(f'Step {step_count}: {iterable}') if printout else None
        if swap:
            return iterable if printout else print(f'Steps: {step_count}: {iterable}.')


print('BUBBLE SEARCH')
list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bubble_sort2(list1)
print('\nlist2'), bubble_sort2(list2)
print('\nlist3'), bubble_sort2(list3, False)

# Order of growth O(n**2) because each iterative solution is O(len(iterable) = O(n).
# There are 2 iterative constructs (while and for), so O(n)*O(n) = O(n**2)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SELECTION SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


