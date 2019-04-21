"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: iteration, recursion
        - decorators

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
        https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME ITERATIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) My own solution before searching on the Internet:


def format_string(palindrome_check_function):
    def wrapper(text):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        text = text.lower()
        for s in text:
            if s not in letters:
                text = text.replace(s, '')
        return palindrome_check_function(text)
    return wrapper


# SHORTER VERSION OF THE ABOVE:
# def format_string_shorter(palindrome_check_function):
#     def wrapper(text):
#         for s in text.lower():
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
    return f' => {check}'


print('CHECK PALINDROME ITERATIVE')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
print(str1, is_palindrome_iterative(str1))
print(str2, is_palindrome_iterative(str2))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME RECURSIVE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


# 1) MIT lecture solution

def is_palindrome_recursive(string):

    def to_chars(text):
        text = text.lower()
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


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHECK PALINDROME SIMPLEST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def is_palindrome_simple(n1):
    for let in n1.lower():
        if let not in 'abcdefghijklmnopqrstuvwxyz':
            n1 = n1.replace(let, '')
    n2 = n1[::-1]
    return n1 == n2


print('CHECK PALINDROME NO RECURSION OR ITERATION EXPLICITLY')
str1 = 'abb cdaaXXaa, dcbba!'
str2 = 'fsdas dasdas sadsf'
print(is_palindrome_simple(str1))
print(is_palindrome_simple(str2))