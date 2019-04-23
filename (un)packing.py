"""
    This file is for learning and exercise purposes.

    Topics:
        - packing and unpacking arguments
        - multiple assignment

    Sources:
        https://jpt-pynotes.readthedocs.io/en/latest/functions.html#argument-lists
        https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
"""


print('UNPACKING TUPLE')
tuple_1 = [1, 2, 3, 4]
print(tuple_1)
print(*tuple_1)

print('UNPACKING LIST')
list_1 = (1, 2, 3, 4)
print(list_1)
print(*list_1)

print('UNPACKING DICT')
dict_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(dict_1)
print(*dict_1)
print(*dict_1.values())
dict_2 = {'a': 'orange', 'b': 'apple', 'c': 'kiwi', 'd': 'banana'}
print(dict_2)
print(*dict_2)
print(*dict_2.values())


print('##########################################################################')
print('UNPACKING FOR FUNCTIONS')
tuple_1 = [1, 2, 3, 4]
list_1 = (1, 2, 3, 4)
dict_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict_2 = {'a': 'orange', 'b': 'apple', 'c': 'kiwi', 'd': 'banana'}


def forfun(a, b, c, d):
    print(a, b, c, d)


forfun(*tuple_1)
forfun(*list_1)
print('*dict accesses keys')
forfun(*dict_1)
forfun(*dict_2)
print('**dict accesses values - but keys need to be str for values to be printed out without error')     # WHY?
# forfun(**dict_1)  # - generates error: TypeError: forfun() keywords must be strings
forfun(**dict_2)


print('##########################################################################')
print('PACKING WITH FUNCTIONS - arbitrary number of args')
tuple_1 = [1, 2, 3, 4]
list_1 = (1, 2, 3, 4)
dict_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict_2 = {'a': 'orange', 'b': 'apple', 'c': 'kiwi', 'd': 'banana'}


def sumup(*args):
    """Function packs all provided arguments into a tuple, so then it can iterate over them."""
    summ = 0
    for a in args:
        summ += a
    return summ


print(sumup(1, 4, 6, 7, 8, 11))
print(sumup(*tuple_1))              # Here *tuple_1 unpack arguments, which are then packed again by sumup(*args)
print(sumup(*dict_1))
print(sumup(*tuple_1, *list_1, *dict_1))


print('##########################################################################')
print('PACKING WITH FUNCTIONS - arbitrary number of kwargs')


def unpack_dict(**kwargs):
    index = ''
    for key in kwargs:
        index += "{} {}\n".format(key, ', '.join(kwargs[key]))
    return index


dict_citations = {'Malinowski, Bronislaw': ('3', '5', '17', '167'),
                  'Levi-Strauss, Claude': ('4', '9', '89', '134'),
                  'Geertz, Clifford': ('3', '5', '78', '89')}
print(unpack_dict(**dict_citations))     # **dict_citations unpacks dict items


print('##########################################################################')
print('MORE UNPACKING')

(x, y), color = ((1, 2), 'red')
print(x)
print(y)
print(color)
print()


def color_of_point(point):
    (_, _), colour = point
    return colour


points = [((1, 2), 'red'), ((3, 4), 'green'), ((7, 9), 'blue')]
for p in points:
    print(color_of_point(p), '// ', end='')

print()
sorted_by_color = sorted(points, key=color_of_point)
print(sorted_by_color)
