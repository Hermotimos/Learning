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


tuple2 = 1, 2, 3, 4, 3
list2 = [1, 2, 3, 4, 3, 4, 3]
# bogo_sort(tuple2)             # Tuple is immutable: TypeError: 'tuple' object does not support item assignment
bogo_sort(list2)
print()
# This algorithm will eventually sort short lists.
# For 7-element iterable 'list2' steps needed in 10 trials: 327, 325, 235, 204, 169, 421, 401, 593, 3, 391
# LOL 3 steps - that's goooood. But sometimes it takes up to 900+, and once it needed 2400 steps...
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
def bubble_sort2(iterable):
    print(f'\nStart: {iterable}')
    step_count = 0
    while True:
        swap = True
        for e in range(1, len(iterable)):
            if iterable[e - 1] > iterable[e]:
                swap = False
                step_count += 1
                iterable[e - 1], iterable[e] = iterable[e], iterable[e - 1]
                print(f'Step {step_count}: {iterable}')
        if swap:
            return iterable


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
print(bubble_sort2(list1))
print(bubble_sort2(list2))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BUBBLE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


