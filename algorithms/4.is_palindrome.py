"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - decorators

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
"""
from time_function_decorator import time_function


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME ITERATIVE (LINEAR SEARCH) <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) My own solution before searching on the Internet:


def format_string(palindrome_check_function):
    def wrapper(text):
        digits = 'abcdefghijklmnopqrstuvwxyz0123456789'
        text = str(text).lower()
        for d in text:
            if d not in digits:
                text = text.replace(d, '')
        return palindrome_check_function(text)
    return wrapper


# SHORTER VERSION OF THE ABOVE:
# def format_string_shorter(palindrome_check_function):
#     def wrapper(text):
#         text = str(text).lower()
#         for s in text:
#             if s not in 'abcdefghijklmnopqrstuvwxyz':
#                 text = text.replace(s, '')
#         return palindrome_check_function(text)
#     return wrapper


@format_string
def is_palindrome_iterative(string):
    check = True
    for v in range(len(string) // 2 + 1):
        if string[v] != string[-(v+1)]:
            check = False
            break
    return f' => {check}'


# UPGRADE
@format_string
def is_palindrome_iterative2(string):
    for v in range(len(string) // 2 + 1):
        if string[v] != string[-(v+1)]:
            return f' => {False}'        # This is possible, because the first 'return' called in the function, ends it
    return f' => {True}'                 # So if first return is called, then this one will be avoided


print('\nCHECK PALINDROME ITERATIVE (LINEAR SEARCH)')
str1 = 'abb cdaaXfXaa, dcbba!'
str2 = 'fsdas dasfdas sadsf'
print(str1, is_palindrome_iterative(str1))
print(str2, is_palindrome_iterative(str2))
print('---------------')
print(str1, is_palindrome_iterative2(str1))
print(str2, is_palindrome_iterative2(str2))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) MIT lecture solution

def is_palindrome_recursive(string):

    def to_chars(text):
        text = str(text).lower()
        chars = ''
        for d in text:
            if d in 'abcdefghijklmnopqrstuvwxyz':
                chars += d
        return chars

    def is_pal(chars):
        if len(chars) <= 1:
            return True
        else:
            return chars[0] == chars[-1] and is_pal(chars[1:-1])

    return is_pal(to_chars(string))


print('CHECK PALINDROME RECURSIVE')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
print(is_palindrome_recursive(str1))
print(is_palindrome_recursive(str2))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME SIMPLEST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def is_palindrome_simple(text):
    text = str(text).lower()
    for digit in text:
        if digit not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(digit, '')
    return text == text[::-1]


print('CHECK PALINDROME SIMPLEST')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
print(is_palindrome_simple(str1))
print(is_palindrome_simple(str2))
print()


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


strings = ('abb cdaaXXaa, dcbba!', 'fsdas dasdas sadsf', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 111, 'd',
           'ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCTGC')

print('ITERATIVE')
clocked = time_function(is_palindrome_iterative)
for s in strings:
    clocked(s)
print()

print('RECURSIVE')
clocked = time_function(is_palindrome_recursive)
for s in strings:
    clocked(s)
print()

print('SIMPLEST')
clocked = time_function(is_palindrome_simple)
for s in strings:
    clocked(s)
print()


# CONCLUSION
#
# All of above algorithms take no time to compute for short strings.
