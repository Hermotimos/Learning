"""
    This file is for learning and exercise purposes.

    Topics:
        - exceptions: syntax and catching
        - examples: ZeroDivisionError, AssertionError
"""


############################################################################################
# 1)


def get_ratios(list1, list2):
    ratios = []
    for index in range(len(list1)):
        try:
            ratios.append(list1[index] / list2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with wrong argument(s)')
    return ratios


lista1 = [0, 1, 2, 3, 4, 5]
lista2 = [0, 4, 4, 4, 4, 4]

print(get_ratios(lista1, lista2))

# special float value 'nan' - to secure coherence in the list (only floats)
print(type(float('nan')))
print('#'*30)


############################################################################################
# 2)


def yearly_scores_with_avg(scores):
    list_with_scores = []
    for elem in scores:
        list_with_scores.append([elem[0], elem[1], round(avg(elem[1]), 2)])
    return list_with_scores


def avg(list):
    try:
        return sum(list)/len(list)
    except ZeroDivisionError:
        print("Warning: some students have no results data (indicated by 0 as average score)")
        return 0.0


test_grades = [[['Peter', 'Parker'], [80.0, 70.0, 85.0]],
               [['Bruce', 'Wayne'], [100.0, 80.0, 74.0]],
               [['Clint', 'Eastwood'], [25.0, 80.0, 85.0]],
               [['Mr.', 'Nobody'], []],
               [['Clint', 'Westwood'], [25.0, 82.0, 85.0]]]
print(test_grades)
print(yearly_scores_with_avg(test_grades))
print('#'*30)


############################################################################################
# 3) ASSERTIONS:


def yearly_scores_with_avg(scores):
    list_with_scores = []
    for elem in scores:
        list_with_scores.append([elem[0], elem[1], round(avg(elem[1]), 2)])
    return list_with_scores


def avg(list):
    try:
        assert len(list) > 0                                        # here comes assertion
        return sum(list)/len(list)
    except AssertionError:                                          # here comes assertion handling
        print("Warning: some students have no results data (indicated by 0 as average score)")
        return 0.0
    except Exception as exception1:                                 # handling of other exceptions
        print(f"An error occured: {exception1}")


test_grades = [[['Peter', 'Parker'], [80.0, 70.0, 85.0]],
               [['Bruce', 'Wayne'], [100.0, 80.0, 74.0]],
               [['Clint', 'Eastwood'], [25.0, 80.0, 85.0]],
               [['Mr.', 'Nobody'], []],
               [['Clint', 'Westwood'], [25.0, 82.0, 85.0]]]
print(test_grades)
print(yearly_scores_with_avg(test_grades))
print()


# ZADANIE [my version]
def celcius_to_kelvin(temp):
    try:
        assert temp >= -273.15
        temp += 273.15
        return temp
    except AssertionError:
        return "Wrong temperature given: lower than absolute zero !"


print(celcius_to_kelvin(20))
print(celcius_to_kelvin(-400))

