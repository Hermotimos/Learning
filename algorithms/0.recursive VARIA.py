"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion, monkey sort, bubble sort, selection sort, merge sort

    Sources:
        Aditya Bhargava - Algorytmy. Ilustrowany przewodnik.
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RECURSIVE SUM OF ELEMENTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def recursive_adding(iterable):
    if not iterable:
        return 0
    else:
        return iterable[0] + recursive_adding(iterable[1:])


print('\n', '\bRECURSIVE SUM OF ELEMENTS')
list_1 = [1, 2, 3, 4, 10, 11, 12]
tuple_1 = (1, 2, 3, 4, 10, 11, 12)
set_1 = {1, 2, 3, 4, 10, 11, 12}      # TypeError: 'set' object is not subscriptable

print(recursive_adding(list_1))
print(recursive_adding(tuple_1))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RECURSIVE COUNT OF ELEMENTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def recursive_count(iterable):
    if not iterable:
        return 0
    else:
        return 1 + recursive_count(iterable[1:])


print('\n', '\bRECURSIVE COUNT OF ELEMENTS')
list_1 = [1, 2, 3, 4, 10, 11, 12]
tuple_1 = (1, 2, 3, 4, 10, 11, 12)

print(recursive_count(list_1))
print(recursive_count(tuple_1))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RECURSIVE MAX ELEMENT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# based on merge sort (this I would call 'emerge' sort :))
def recursive_max(iterable):
    if not iterable:
        return None
    elif len(iterable) == 1:
        return iterable[0]
    else:
        mid = len(iterable) // 2
        half1 = recursive_max(iterable[:mid])
        half2 = recursive_max(iterable[mid:])
        return half1 if half1 > half2 else half2


print('\n', '\bRECURSIVE MAX ELEMENT 1')
list_1 = [1, 2, 3, 4, 10, 11, 12]
tuple_1 = (1, 2, 3, 4, 10, 11, 12)

print(recursive_max(list_1))
print(recursive_max(tuple_1))


# ----------------------------------------------------------------------------------------------------
# from Aditya Bhargava

def recursive_max2(iterable):
    if len(iterable) == 2:
        return iterable[0] if iterable[0] > iterable[1] else iterable[1]
    else:
        sub_max = recursive_max(iterable[1:])
        return iterable[0] if iterable[0] > sub_max else sub_max


print('\n', '\bRECURSIVE MAX ELEMENT 2')
list_1 = [1, 2, 3, 4, 10, 11, 12]
tuple_1 = (1, 2, 3, 4, 10, 11, 12)

print(recursive_max2(list_1))
print(recursive_max2(tuple_1))

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> xxxxxxxxxxxxxxxxxx <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------
