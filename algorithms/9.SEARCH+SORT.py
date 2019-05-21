"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion

    Sources:
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
"""
from time_function_decorator import time_function


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>> SEARCH IN UNORDERED LIST + SELECTION SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def search_selection_sorted(list_, searched_elem):

    def selection_sort(listx):
        index = 0
        while index < len(listx):
            for n in range(index, len(listx)):
                if listx[index] > listx[n]:
                    listx[index], listx[n] = listx[n], listx[index]
            index += 1
        return listx

    def bisection_search(listx, element, low=0, high=0):
        if high == 0:
            high = len(listx)

        if len(listx) == 0:
            return False
        elif len(listx[low:high]) == 1:
            return listx[0] == element
        else:
            middle = (low + high) // 2
            if listx[middle] == element:
                return True
            elif listx[middle] > element:
                high = middle
            else:
                low = middle
            return bisection_search(listx, element, low, high)

    list_ = selection_sort(list_)
    return bisection_search(list_, searched_elem)


print('\n', '\bSEARCH IN UNORDERED LIST + SELECTION SORT')
unordered_list = [3, 1, 5, 6, 7, 3, 543, 64, 234, 12, 6, 3, 5478, 543, 2]
print(search_selection_sorted(unordered_list, 12))
print(search_selection_sorted(unordered_list, 7))
print(search_selection_sorted(unordered_list, 333))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> SEARCH IN UNORDERED LIST + MERGE SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------

def search_merge_sorted(list_, searched_elem):

    def merge_sort(listx):

        def merge(left, right):
            a, b, result = 0, 0, []
            while a < len(left) and b < len(right):
                if left[a] < right[b]:
                    result.append(left[a])
                    a += 1
                else:
                    result.append(right[b])
                    b += 1
            while a < len(left):
                result.append(left[a])
                a += 1
            while b < len(right):
                result.append(right[b])
                b += 1
            return result

        if len(listx) < 2:
            return listx
        else:
            mid = len(listx) // 2
            half1 = merge_sort(listx[:mid])
            half2 = merge_sort(listx[mid:])
            return merge(half1, half2)

    def bisection_search(listx, element, low=0, high=0):
        if high == 0:
            high = len(listx)

        if len(listx) == 0:
            return False
        elif len(listx[low:high]) == 1:
            return listx[0] == element
        else:
            middle = (low + high) // 2
            if listx[middle] == element:
                return True
            elif listx[middle] > element:
                high = middle
            else:
                low = middle
            return bisection_search(listx, element, low, high)

    list_ = merge_sort(list_)
    return bisection_search(list_, searched_elem)


print('\n', '\bSEARCH IN UNORDERED LIST + MERGE SORT')
unordered_list = [3, 1, 5, 6, 7, 3, 543, 64, 234, 12, 6, 3, 5478, 543, 2]
print(search_merge_sorted(unordered_list, 12))
print(search_merge_sorted(unordered_list, 7))
print(search_merge_sorted(unordered_list, 333))


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>> COMPARISON: SORT+SEARCH vs LINEAR SEARCH <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def linear_search(listx, element):
    for e in listx:
        if e == element:
            return True
    return False


ul1 = [3, 1, 5, 6, 7, 3, 543, 64, 234, 12]                          # len 10
ul2 = ul1 + ul1 + ul1 + ul1 + ul1 + ul1 + ul1 + ul1 + ul1 + ul1     # len 100
ul3 = ul2 + ul2 + ul2 + ul2 + ul2 + ul2 + ul2 + ul2 + ul2 + ul2     # len 1000
ul4 = ul3 + ul3 + ul3 + ul3 + ul3 + ul3 + ul3 + ul3 + ul3 + ul3     # len 10000
ul5 = ul4 + ul4 + ul4 + ul4 + ul4 + ul4 + ul4 + ul4 + ul4 + ul4     # len 100000
ul_list = [ul1, ul2, ul3, ul4]


# Performance will be tested for the worst case scenario (element is absent from the list)


print('\n', '\bCOMPARISON: SORT+SEARCH vs LINEAR SEARCH')
print('COMPARISON 1')
for ul in ul_list:
    time_function(linear_search, print_args=False)(ul, 333)

for ul in ul_list:
    time_function(search_selection_sorted, print_args=False)(ul, 333)

for ul in ul_list:
    time_function(search_merge_sorted, print_args=False)(ul, 333)


"""

COMPARISON 1
Linear search performs better than selection search and merge search for lists 10000 elements long
Selection search cannot handle 100000 in less than a couple of minutes (or more - I didn't wait)

COMPARISON: SORT+SEARCH vs LINEAR SEARCH
COMPARISON 1
Time for linear_search(): 0.0000019910 secs
Time for linear_search(): 0.0000051200 secs
Time for linear_search(): 0.0000426640 secs
Time for linear_search(): 0.0005378520 secs
Time for search_selection_sorted(): 0.0000366910 secs
Time for search_selection_sorted(): 0.0009661990 secs
Time for search_selection_sorted(): 0.0616080540 secs
Time for search_selection_sorted(): 6.2539294320 secs
Time for search_merge_sorted(): 0.0000315720 secs
Time for search_merge_sorted(): 0.0003632140 secs
Time for search_merge_sorted(): 0.0047505020 secs
Time for search_merge_sorted(): 0.0576872260 secs

"""
ul6 = ul5 + ul5 + ul5 + ul5 + ul5 + ul5 + ul5 + ul5 + ul5 + ul5     # len 1000000 (1mln)
ul_list_2 = [ul1, ul2, ul3, ul4, ul5, ul6]

print('\n', '\bCOMPARISON: SORT+SEARCH vs LINEAR SEARCH')
print('COMPARISON 2')
for ul in ul_list_2:
    time_function(linear_search, print_args=False)(ul, 333)

for ul in ul_list_2:
    time_function(search_merge_sorted, print_args=False)(ul, 333)


"""
COMPARISON 2

Linear search is still faster than merge search.
This is because order of growth for linear search is O(n) and for sort + search algorithms it's ......

- complexity of sorting (via bisection): O(n) - in order to sort must look at each element at least once
- complexity of searching (via bisection without copying): O(log n)

If collection is unsorted, it's never efficient to sort it before searching for an element. 
The complexity of search may be less than O(n), however the complexity of sort cannot be less than O(n).


COMPARISON: SORT+SEARCH vs LINEAR SEARCH
COMPARISON 2
Time for linear_search(): 0.0000022760 secs
Time for linear_search(): 0.0000039820 secs
Time for linear_search(): 0.0000324250 secs
Time for linear_search(): 0.0002949510 secs
Time for linear_search(): 0.0035069870 secs
Time for linear_search(): 0.0312804430 secs
Time for search_merge_sorted(): 0.0000327090 secs
Time for search_merge_sorted(): 0.0003444410 secs
Time for search_merge_sorted(): 0.0042618560 secs
Time for search_merge_sorted(): 0.0555565820 secs
Time for search_merge_sorted(): 0.7909321210 secs
Time for search_merge_sorted(): 9.2948038860 secs
"""