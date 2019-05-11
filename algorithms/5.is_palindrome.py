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
import functools

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME ITERATIVE (LINEAR SEARCH) <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def format_string(palindrome_check_function):
    @functools.wraps(palindrome_check_function)                 # preserves decorated function's name
    def wrapper(text):
        text = str(text).lower()
        for d in text:
            if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                text = text.replace(d, '')
        return palindrome_check_function(text)
    return wrapper


@format_string
def is_palindrome_iter1(string):
    if len(string) == 0:
        return False
    check = True
    for v in range(1, len(string) // 2):
        if string[v-1] != string[-v]:
            check = False
            break
    return f' => {check}'


@format_string
def is_palindrome_iter11(string):
    if len(string) == 0:
        return False
    for v in range(1, len(string) // 2):
        if string[v-1] != string[-v]:
            return False
    return True


print('\nCHECK PALINDROME ITERATIVE (LINEAR SEARCH)')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_iter1(str1))
print(is_palindrome_iter1(str2))
print(is_palindrome_iter1(int1))
print(is_palindrome_iter1(''))

print('---------------')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_iter11(str1))
print(is_palindrome_iter11(str2))
print(is_palindrome_iter11(int1))
print(is_palindrome_iter11(''))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

# 1) MIT lecture solution
#    Disadvantage of recursive solutions: returns True for empty str.
#    Putting 'if len(text) == 0: return False' results in always False in recursive solution.
#    Dealing with it would require several lines of code.

def is_palindrome_recur1(string):

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


print('\nCHECK PALINDROME RECURSIVE 1')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_recur1(str1))
print(is_palindrome_recur1(str2))
print(is_palindrome_recur1(int1))
print(is_palindrome_recur1(''))


# ----------------------------------------------------------------------------------------------------

# 2) Simplified version based on MIT algorithm

def is_palindrome_recur2(string):
    string = str(string).lower()
    for d in string:
        if d not in 'abcdefghijklmnopqrstuvwxyz':
            string = string.replace(d, '')
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome_recur2(string[1:-1])


print('\nCHECK PALINDROME RECURSIVE 2')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_recur2(str1))
print(is_palindrome_recur2(str2))
print(is_palindrome_recur2(int1))
print(is_palindrome_recur2(''))


# ----------------------------------------------------------------------------------------------------

# 3) Best recursive version
#    Avoids applying text formatting in each recursive step AND deals with empty strings (returns False)
#    TODO Test it's performance in comparison to others


def is_palindrome_recur3(text):
    def convert_to_digits(string):
        string = str(string).lower()
        for d in string:
            if d not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                string = string.replace(d, '')
        return string

    def is_palindrome(string):
        if len(string) <= 1:
            return True
        return string[0] == string[-1] and is_palindrome(string[1:-1])

    text = convert_to_digits(text)
    if len(text) == 0:
        return False
    return is_palindrome(text)


print('\nCHECK PALINDROME RECURSIVE 3')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_recur3(str1))
print(is_palindrome_recur3(str2))
print(is_palindrome_recur3(int1))
print(is_palindrome_recur3(''))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME SIMPLEST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def is_palindrome_simple(text):
    text = str(text).lower()
    for digit in text:
        if digit not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text.replace(digit, '')

    if len(text) == 0:
        return False
    return text == text[::-1]


print('\nCHECK PALINDROME SIMPLEST')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
int1 = 3
print(is_palindrome_simple(str1))
print(is_palindrome_simple(str2))
print(is_palindrome_simple(int1))
print(is_palindrome_simple(''))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PERFORMANCE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


strings = ('abb cdaaXXaa, dcbba!', 'fsdas dasdas sadsf', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 111, '', 'd', 3,
           'ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAGGGTGGGGGTCCCGGGTACTGGTAGGGGTAGCTGC')

print('\nITERATIVE')
clocked = time_function(is_palindrome_iter1)
for s in strings:
    clocked(s)

print('\nRECURSIVE')
clocked = time_function(is_palindrome_recur1)
for s in strings:
    clocked(s)

print('\nSIMPLEST')
clocked = time_function(is_palindrome_simple)
for s in strings:
    clocked(s)

# CONCLUSION
#
# All of above algorithms take no time to compute for short strings.
