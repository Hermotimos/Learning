"""
    This is sandbox file for learning and exercise purposes.
"""

# # y/n function for TV series database with recursion :)
#
#
# def yesno_choice(text):
#     try:
#         assert text in ('y', 'n')
#         return text
#     except AssertionError:
#         text = input("Please answer with one of the following keys: 'y' for 'yes' or 'n' for 'no': ")
#         return yesno_choice(text)
#
#
# text = input(" y or n ? ")
# print(yesno_choice(text))
#
#
#
# # EXERCISE
#
# first_name = input("What is you first name? ")
# first_name.capitalize()
# print(first_name.isalpha())
# if first_name[-1] == 'a':
#     print("If your name is Polish, is seems you're a women.")
# else:
#     pass
#
# last_name = input("What is you last name? ")
# last_name.capitalize()
# print(last_name.isalpha())
#
# phone = input("What is you telephone number? ")
# phone_digits_only = ""
# for elem in phone:
#     if elem.isdigit():
#         phone_digits_only += elem
# print(phone_digits_only)
# print(phone_digits_only.isdigit())
#
# personal = first_name + ' ' + last_name + ' ' + phone_digits_only
# print(personal)
# print(len(personal))
#
# letters_cnt = 0
# for elem in personal:
#     if elem.isalpha():
#         letters_cnt += 1
# print(letters_cnt)
#
#
#
# # List comprehension: constructing a list in a shorter way
#
# words = 'The quick brown fox jumps over the lazy dog'.split()
# print(words)
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# for i in stuff:
#     print(i)


# # SPOJ half of the half
# values = open('sandbox_SPOJ_input').read().splitlines()
# times = int(values[0])
# words = tuple(str(v) for v in values[1:])
#
# for t in range(times):
#     word = words[t]
#     out = ''
#     for letter in (word[i] for i in range(0, len(word) // 2, 2)):
#         out += letter
#     print(out)
#
#
# # Fizz Buzz
# def fizzbuzz():
#     for n in range(1, 101):
#         if n % 3 == 0 and n % 5 == 0:
#             print('Fizz Buzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         elif n % 5 == 0:
#             print('Buzz')
#         else:
#             print(n)
#
#
# fizzbuzz()
