"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
import random
from time_function_decorator import time_function


# CODE TO CHECK IF LIST IS SORTED
def is_sorted(list_):
    return all(list_[n - 1] <= list_[n] for n in range(1, len(list_)))


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


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>> MONKEY SORT / BOGO SORT / SHOTGUN SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('MONKEY SORT / BOGO SORT / SHOTGUN SORT')


# PURE ALGORITHM
def bogo_sort(list_):
    while not all(list_[n - 1] <= list_[n] for n in range(1, len(list_))):
        random.shuffle(list_)
    return list_


# VERSION WITH PRINTOUT AND COUNTER
def bogo_sort2(list_, shuffle_counter=0):
    print(f'Start: {list_}')
    while not all(list_[n - 1] <= list_[n] for n in range(1, len(list_))):
        random.shuffle(list_)
        shuffle_counter += 1
    print(f'Steps needed: {shuffle_counter}: {list_}')


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bogo_sort2(list1)
print('\nlist2'), bogo_sort2(list2)
# print('\nlist3'), bogo_sort2(list3)        # Woooops... this probably takes hours.
print()

# This algorithm will eventually sort short lists.
# 10 trials for a 7-element list: 327, 325, 235, 204, 169, 421, 401, 593, 3, 391 ===> seen range 3 - 2400 !!!
# Order of growth O is unbounded.


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BUBBLE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('BUBBLE SORT')
print()


# MIT VERSION

def bubble_mit(list_):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(list_)):
            if list_[j - 1] > list_[j]:
                swap = False
                temp = list_[j]
                list_[j] = list_[j - 1]
                list_[j - 1] = temp
    return list_


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'MIT algorithm test for {list1}:')
print(bubble_mit(list1))
print()
# COMMENT
# The 'swap' flag in this algorithm is very counter-intuitive: it makes 'swap = False' right before a swap is done.
# Also it doen't make use of multiple assignment. And it's long... So it needs simplification:


# SHORTER VERSION

def bubble_sort_short(list_):
    while True:
        swap = False
        for e in range(1, len(list_)):
            if list_[e - 1] > list_[e]:
                list_[e - 1], list_[e] = list_[e], list_[e - 1]
                swap = True
        if not swap:
            return list_


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'Shorter algorithm test for list {list1}:')
print(bubble_sort_short(list1))
print()


# SHORTEST VERSION

def bubble_sort_shortest(list_):
    while not all(list_[n - 1] <= list_[n] for n in range(1, len(list_))):
        for e in range(1, len(list_)):
            if list_[e - 1] > list_[e]:
                list_[e - 1], list_[e] = list_[e], list_[e - 1]
    return list_


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'Shortest algorithm test for list {list1}:')
print(bubble_sort_shortest(list1))
print()


# VERSION WITH PRINTOUT AND COUNTER
def bubble_sort2(list_, printout=True):
    print(f'Start: {list_}') if printout else None
    step_count = 0
    while True:
        swap = False
        for e in range(1, len(list_)):
            if list_[e - 1] > list_[e]:
                list_[e - 1], list_[e] = list_[e], list_[e - 1]
                swap = True
                step_count += 1
                print(f'Step {step_count}: {list_}') if printout else None
        if not swap:
            return list_ if printout else print(f'Steps: {step_count}: {list_}.')


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bubble_sort2(list1)
print('\nlist2'), bubble_sort2(list2)
print('\nlist3'), bubble_sort2(list3, False)
print()

# Order of growth O(n**2) because each iterative solution is O(len(list_) = O(n).
# There are 2 iterative constructs (while and for), so O(n)*O(n) = O(n**2)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SELECTION SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('SELECTION SORT')


# PURE ALGORITHM
def selection_sort(list_):
    index = 0
    while index < len(list_):
        for n in range(index, len(list_)):
            if list_[index] > list_[n]:
                list_[index], list_[n] = list_[n], list_[index]
        index += 1
    return list_


# WITH PRINTOUT
def selection2(list_):
    index = 0
    while index != len(list_):
        print(f'Step {index}: {list_}')
        for n in range(index, len(list_)):
            if list_[index] > list_[n]:
                list_[index], list_[n] = list_[n], list_[index]
        index += 1
    return list_


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), print(selection2(list1))
print('\nlist2'), print(selection2(list2))
print('\nlist3'), print(selection2(list3))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MERGE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('MERGE SORT')


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
        return list_[:]
    else:
        middle = len(list_) // 2
        half1 = merge_sort(list_[:middle])
        half2 = merge_sort(list_[middle:])
        return merge(half1, half2)


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), print(merge_sort(list1))
print('\nlist2'), print(merge_sort(list2))
print('\nlist3'), print(merge_sort(list3))


# WITH PRINTOUT
# Steps counting has no meaning by recursion - I'm putting it here to see why

def merge_sort2(list_):
    global counter
    counter += 1

    def merge(left, right):
        print(f'Step {counter}:\n\t\tleft: {left}\n\t\tright: {right}')
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
        return list_[:]
    else:
        middle = len(list_) // 2
        half1 = merge_sort2(list_[:middle])
        half2 = merge_sort2(list_[middle:])
        return merge(half1, half2)


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
counter = 0
print('\nlist1'), print(merge_sort2(list1))
counter = 0
print('\nlist2'), print(merge_sort2(list2))
counter = 0
print('\nlist3'), print(merge_sort2(list3))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


algorithms = [bubble_mit, bubble_sort_short, bubble_sort_shortest, selection_sort, merge_sort]

for alg in algorithms:
    list1 = [17, 2, 73, 1, 34, 3, 54, 17, 2, 73]
    list2 = list1 + list1 + list1 + list1 + list1 + list1 + list1 + list1 + list1 + list1
    list3 = list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2
    list4 = list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3
    list5 = list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4
    lists = [list1, list2, list3, list4, list5]
    print()
    for i, list_ in enumerate(lists):
        print(f'list length: {len(list_)}')
        time_function(alg, print_args=False)(list_)
