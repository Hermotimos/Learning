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


def format_string(palindrome_check_function):
    def wrapper(text):
        text = str(text).lower()
        for d in text:
            if d not in 'abcdefghijklmnopqrstuvwxyz':
                text = text.replace(d, '')
        return palindrome_check_function(text)
    return wrapper


@format_string
def is_palindrome_iterative(string):
    if len(string) == 0:
        return False
    check = True
    for v in range(1, len(string) // 2):
        if string[v-1] != string[-v]:
            check = False
            break
    return f' => {check}'


@format_string
def is_palindrome_iterative2(string):
    if len(string) == 0:
        return False
    for v in range(1, len(string) // 2):
        if string[v-1] != string[-v]:
            return False
    return True


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
# Disadvantage of recursive solutions: returns True for empty str.
# Putting 'if len(text) == 0: return False results in always False in recursive solution.
# Dealing with it would require several lines of code


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


# SIMPLER:
def is_palindrome_recursive2(string):
    string = str(string).lower()
    for d in string:
        if d not in 'abcdefghijklmnopqrstuvwxyz':
            string = string.replace(d, '')
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome_recursive2(string[1:-1])


print('CHECK PALINDROME RECURSIVE 2')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
print(is_palindrome_recursive2(str1))
print(is_palindrome_recursive2(str2))
print()

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME SIMPLEST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def is_palindrome_simple(text):
    if len(text) == 0:
        return False
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
