"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.dima.to/blog/?p=29
        https://www.python-course.eu/towers_of_hanoi.php
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VERSION 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def hanoi1(size, source, middle, target):
    if size == 0:
        return
    hanoi1(size - 1, source, target, middle)
    if source:
        target.append(source.pop())
    hanoi1(size - 1, middle, source, target)


# VERSION 1 WITH PRINTOUT:
def hanoi1_print(size, source, middle, target):
    if size == 0:
        return
    hanoi1_print(size - 1, source, target, middle)
    if source:
        target.append(source.pop())
    print('\na {}\nb {}\nc {}'.format(*towers))
    hanoi1_print(size - 1, middle, source, target)


height = 4
a, b, c = [*range(height, 0, -1)], [], []
towers = a, b, c
step = 0

print('------------ VERSION 1 ------------')
print('START:\na {}\nb {}\nc {}'.format(*towers))
hanoi1_print(len(a), a, b, c)


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VERSION 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def hanoi2(size, source, target, middle):
    if size == 1:
        target.append(source.pop())
    else:
        hanoi2(size-1, source, middle, target)
        hanoi2(1, source, target, middle)
        hanoi2(size-1, middle, target, source)


# VERSION 2 WITH PRINTOUT:
def hanoi2_print(size, source, target, middle):
    if size == 0:
        print('\na {}\nb {}\nc {}'.format(*towers))
    if size == 1:
        target.append(source.pop())
        print('\na {}\nb {}\nc {}'.format(*towers))
    else:
        hanoi2_print(size - 1, source, middle, target)
        hanoi2_print(1, source, target, middle)
        hanoi2_print(size - 1, middle, target, source)


height = 3
a, b, c = [*range(height, 0, -1)], [], []
towers = a, b, c

print('------------ VERSION 2 ------------')
print('START:\na {}\nb {}\nc {}'.format(*towers))
hanoi2_print(len(a), a, c, b)
