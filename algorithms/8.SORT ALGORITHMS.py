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
def is_sorted(listx):
    return all(listx[n - 1] <= listx[n] for n in range(1, len(listx)))


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
def bogo_sort(listx):
    while not all(listx[n - 1] <= listx[n] for n in range(1, len(listx))):
        random.shuffle(listx)
    return listx


# VERSION WITH PRINTOUT AND COUNTER
def bogo_sort2(listx, shuffle_counter=0):
    print(f'Start: {listx}')
    while not all(listx[n - 1] <= listx[n] for n in range(1, len(listx))):
        random.shuffle(listx)
        shuffle_counter += 1
    print(f'Steps needed: {shuffle_counter}: {listx}')


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bogo_sort2(list1)
print('\nlist2'), bogo_sort2(list2)
# print('\nlist3'), bogo_sort2(list3)        # Woooops... this probably takes hours.
print()

# This algorithm will eventually sort short lists.
# 10 trials for a 7-element list: 327, 325, 235, 204, 169, 421, 401, 593, 3, 391. Generally seen range 3 - 2400 !!!
# Order of growth O is here unbounded in the worst case scenario.


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BUBBLE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('BUBBLE SORT')
print()


# MIT VERSION

def bubble_mit(listx):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(listx)):
            if listx[j - 1] > listx[j]:
                swap = False
                temp = listx[j]
                listx[j] = listx[j - 1]
                listx[j - 1] = temp
    return listx


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'MIT algorithm test for {list1}:')
print(bubble_mit(list1))
print()
# COMMENT
# This 'swap' business here is very counter-intuitive, as 'swap = False' right before a swap is done.
# Also it doen't make use of multiple assignment. And it's long...
# So it needs simplification


# SHORTER VERSION

def bubble_sort_short(listx):
    while True:
        swap = False
        for e in range(1, len(listx)):
            if listx[e-1] > listx[e]:
                listx[e-1], listx[e] = listx[e], listx[e-1]
                swap = True
        if not swap:
            return listx


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'Shorter algorithm test for list {list1}:')
print(bubble_sort_short(list1))
print()


# SHORTEST VERSION

def bubble_sort_shortest(listx):
    while not all(listx[n-1] <= listx[n] for n in range(1, len(listx))):
        for e in range(1, len(listx)):
            if listx[e-1] > listx[e]:
                listx[e-1], listx[e] = listx[e], listx[e-1]
    return listx


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
print(f'Shortest algorithm test for list {list1}:')
print(bubble_sort_shortest(list1))
print()


# VERSION WITH PRINTOUT AND COUNTER
def bubble_sort2(listx, printout=True):
    print(f'Start: {listx}') if printout else None
    step_count = 0
    while True:
        swap = False
        for e in range(1, len(listx)):
            if listx[e-1] > listx[e]:
                listx[e-1], listx[e] = listx[e], listx[e-1]
                swap = True
                step_count += 1
                print(f'Step {step_count}: {listx}') if printout else None
        if not swap:
            return listx if printout else print(f'Steps: {step_count}: {listx}.')


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), bubble_sort2(list1)
print('\nlist2'), bubble_sort2(list2)
print('\nlist3'), bubble_sort2(list3, False)
print()

# Order of growth O(n**2) because each iterative solution is O(len(listx) = O(n).
# There are 2 iterative constructs (while and for), so O(n)*O(n) = O(n**2)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SELECTION SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
print('SELECTION SORT')


# PURE ALGORITHM
def selection_sort(listx):
    index = 0
    while index != len(listx):
        for n in range(index, len(listx)):
            if listx[index] > listx[n]:
                listx[index], listx[n] = listx[n], listx[index]
        index += 1
    return listx


# WITH PRINTOUT
def selection2(listx):
    index = 0
    while index != len(listx):
        print(f'Step {index}: {listx}')
        for n in range(index, len(listx)):
            if listx[index] > listx[n]:
                listx[index], listx[n] = listx[n], listx[index]
        index += 1
    return listx


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


def merge_sort(listx):
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

    if len(listx) < 2:
        return listx[:]
    else:
        middle = len(listx) // 2
        half1 = merge_sort(listx[:middle])
        half2 = merge_sort(listx[middle:])
        return merge(half1, half2)


list1 = [1, 2, 3, 1, 4, 3, 4, 3, 1]
list2 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list3 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3, 4, 3, 1, 17, 2, 73, 1, 34, 3, 54, 43, 11, 1, 2, 3, 1, 4, 3]
print('\nlist1'), print(merge_sort(list1))
print('\nlist2'), print(merge_sort(list2))
print('\nlist3'), print(merge_sort(list3))


# WITH PRINTOUT
# Steps counting has no meaning by recursion - I'm putting it here to see why

def merge_sort2(listx):
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

    if len(listx) < 2:
        return listx[:]
    else:
        middle = len(listx) // 2
        half1 = merge_sort2(listx[:middle])
        half2 = merge_sort2(listx[middle:])
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MERGE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


list1 = [(2, 'two'), (3, 'three'), (0, 'zero'), (4, 'four'), (1, 'one')]
list2 = [17, 2, 73, 1, 34, 3, 54, 43, 11, 1]
list3 = list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2 + list2
list4 = list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3 + list3
list5 = list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4 + list4
list6 = list5 + list5 + list5 + list5 + list5 + list5 + list5 + list5 + list5 + list5

lists = [list1, list2, list3, list4, list5, list6]
algorithms = [bogo_sort, bubble_mit, bubble_sort_short, bubble_sort_shortest, selection_sort, merge_sort]

for i, list_ in enumerate(lists):
    print(f'\nlist{i + 1} [length: {len(list_)}]\n-------')
    for a in algorithms:
        if not (list_ in (list3, list4, list5, list6) and a == bogo_sort):      # Avoid infinite waiting by monkey sort
            time_function(a)(list_)


# CONCLUSIONS
#
# 1)
# Surprisingly, my versions of bubble sort algorithm are much more efficient than the version from MIT lecture.
# I created them only in order to simplify syntax, but they actually work faster.
# This is visible especially for big lists.
# They even perform better than merge sort.
#
# 2)


"""
RESULTS:
list1 [length: 9]
-------
Time for bogo_sort                : 9072181
Time for bubble_mit               : 3284
Time for bubble_sort_short        : 2463
Time for bubble_sort_shortest     : 4516
Time for selection_sort           : 11084
Time for merge_sort               : 25863

list2 [length: 5]
-------
Time for bogo_sort                : 2414705
Time for bubble_mit               : 2464
Time for bubble_sort_short        : 2463
Time for bubble_sort_shortest     : 3284
Time for selection_sort           : 6568
Time for merge_sort               : 13137

list3 [length: 33]
-------
Time for bubble_mit               : 172831
Time for bubble_sort_short        : 5747
Time for bubble_sort_shortest     : 7800
Time for selection_sort           : 71021
Time for merge_sort               : 109610

list4 [length: 163]
-------
Time for bubble_mit               : 6437025
Time for bubble_sort_short        : 43926
Time for bubble_sort_shortest     : 47210
Time for selection_sort           : 2116254
Time for merge_sort               : 1190111

list5 [length: 685]
-------
Time for bubble_mit               : 104488757
Time for bubble_sort_short        : 93599
Time for bubble_sort_shortest     : 126031
Time for selection_sort           : 29530261
Time for merge_sort               : 21002024

list6 [length: 8905]
-------
Time for bubble_mit               : 12698599455
Time for bubble_sort_short        : 1128942
Time for bubble_sort_shortest     : 1563688
Time for selection_sort           : 4042312764
Time for merge_sort               : 51884554

list7 [length: 80145]
-------
Time for bubble_mit               : 1063667727599 ns = 1063.667727599 s = 17.72779546
Time for bubble_sort_short        : 10158019 ns = 0.010158019 s 
Time for bubble_sort_shortest     : 14344138 ns = 0.014344138 s 
Time for selection_sort           : 329638676420 ns = 329.63867642 s =  5.49397794
Time for merge_sort               : 578784174 ns = 0.578784174 s 


"""