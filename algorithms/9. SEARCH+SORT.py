"""
    This file is for learning and exercise purposes.

    Topics:
        - algorithms: recursion
"""


# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>> SEARCH FOR UNORDERED LIST + SELECTION SORT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----------------------------------------------------------------------------------------------------


def search_sorted(list_, searched_elem):

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


unordered_list = [3, 1, 5, 6, 7, 3, 543, 64, 234, 12, 6, 3, 5478, 543, 2]
print(search_sorted(unordered_list, 12))
print(search_sorted(unordered_list, 7))
print(search_sorted(unordered_list, 333))




