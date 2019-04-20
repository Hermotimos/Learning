"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, TODO recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""


some_str = 'abb cdaaXXaa, dcbba!'


def format_string(text=''):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for s in text:
        if s not in letters:
            text = text.replace(s, '')
    return text


# My own ITERATIVE algorithm before looking at the solution
def is_palindrome(string):
    string = format_string(string)
    check = True
    for v in range(len(string) // 2 + 1):
        if string[v] != string[-(v+1)]:
            check = False
    return check


print(is_palindrome(some_str))


# My own RECURSIVE algorithm before looking at the solution.
def is_palindrome_2(string):
    # string = format_string(string)   # todo AttributeError: 'list' object has no attribute 'lower'. Ask StackOverflow
    string = list(string)
    check = True
    while len(string) > 0:
        if string.pop(0) == string.pop(-1):
            is_palindrome_2(string)
        else:
            check = False
            break
    return check


print(is_palindrome_2(format_string(some_str)))
