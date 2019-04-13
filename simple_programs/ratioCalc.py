"""
    Calculate proportion. Ex. 700g berries cost 24.99 => 1100g berries cost x.
    This simple program was written for learning and exercise purposes.

    Used features:
        - user defined functions
        - multiple assignment/tuple unpacking
        - format()
        - assertion, exception handling
"""


def print_example():
    print('EXAMPLE')
    print('\t\t{:^9}{:3}{:^9}'.format(24.99, ' ' * 3, 'n'))
    print('\t\t{:^9}{:^3}{:^9}'.format('-'*9, ' = ', '-'*9))
    print('\t\t{:^9}{:3}{:^9}'.format(700, ' ' * 3, 900))
    print('\tOR')
    print('\t\t{:^9}{:3}{:^9}'.format(24.99, ' ' * 3, 120))
    print('\t\t{:^9}{:^3}{:^9}'.format('-'*9, ' = ', '-'*9))
    print('\t\t{:^9}{:3}{:^9}'.format(700, ' ' * 3, 'n'))


def ask_known_part():
    value1 = float(input("Known ratio's 1st attribute: "))
    value2 = float(input("Known ratio's 2nd attribute: "))
    return value1, value2


def ask_other_part():
    value1 = float(input("Searched ratio's 1st attribute (if unknown type '0' or 'n'): "))
    value2 = float(input("Searched ratio's 2nd attribute (if unknown type '0' or 'n'): "))
    return value1, value2


def calculate_proportion(ratio1=tuple, ratio2=tuple):
    ratio1_value1, ratio1_value2 = ratio1
    ratio2_value1, ratio2_value2 = ratio2
    try:
        assert not (ratio2_value1 == 0 and ratio2_value2 == 0)
        if ratio2_value1 == 0:
            ratio2_value1 = ratio1_value1/ratio1_value2 * ratio2_value2
            ratio2_value1 = round(ratio2_value1, 2)
        elif ratio2_value2 == 0:
            ratio2_value2 = ratio2_value1 * ratio1_value2 / ratio1_value1
            ratio2_value2 = round(ratio2_value2, 2)
        print(ratio1_value1, "/", ratio1_value2, "=", ratio2_value1, "/", ratio2_value2)
    except AssertionError:
        print("Wrong data entered! Ratio 0/0 cannot be resolved!")


def main():
    print_example()
    left = ask_known_part()
    right = ask_other_part()
    calculate_proportion(left, right)


# todo works fine, what's the deal?
# todo exception: user types str instead of number
main()
