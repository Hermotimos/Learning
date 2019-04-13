""""
    This file is for learning and exercise purposes.

    Topics:
        - lists, tuples
        - adding, transformations
        - mutability vs. immutability,
"""


# LISTS VS TUPLES

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]

tuple1 = (10, 20, 30, 40, 50)
tuple2 = ("aa", "bb", "cc", "dd", "ee")

# ADDING NEW ELEMENT TO A LIST (MAY BE A LIST ITSELF)
lista1.append("1 element listy")
print(lista1)
lista1.append(lista2)
print(lista1)

# ADDING NEW ELEMENT-S TO A LIST: '+' OR .extend()
lista1 = [1, 2, 3, 4, 5]
lista1 = lista1 + lista2
print(lista1)
lista1 = [1, 2, 3, 4, 5]
lista1.extend(lista2)
print(lista1)
print()

# ADDING TUPLES: ONLY '+'
tupleN = tuple1 + tuple2
print(tupleN)
print()

# LISTS ARE MUTABLE, TUPLES ARE IMMUTABLE
lista1[0] = "list is mutable"
print(lista1)
# tuple1[0] = "tuple is immutable" THIS WOULD RETURN AN ERROR
print()

# LIST TO STR; STR TO LIST
products = ["milk", "yoghurt", "meat"]
print("Conversion of list into str:", str(products))
print("Conversion of str into list:", list("Some string"))


# IMMUTABLE OBJECTS - EXAMPLE
# Przy obiektach niemutowalnych b = a ma taki skutek, że zmienne a i b są niezależne:
# powstaje kopia wartości przypisanej do pierwszej zmiennej => zmiana jednej, nie pociąga zmiany drugiej
# (możemy przypisać a nową wartość, ale b nadal będzie wskazywać na starą)
print()
a = 1
b = a
print(a)
print(b)

print()
b = "zmiana"
print(a)
print(b)


# MUTABLE OBJECTS - EXAMPLE
# Przy obiektach mutowalnych warm = hot to tylko wskaźniki do tego samego obiektu
# obiekt ten można zmienić zarówno przez modyfikację warm, jaki i przez modyfikację hot
print()
warm = ['red', 'yellow', 'orange']
hot = warm
print(warm)
print(hot)

print()
hot.append('pink')
print(warm)
print(hot)

# CLONINNG A LIST
# Powyższe zachowanie można ominąć przez stworzenie kopii listy:
print()
hot = warm[:]
hot.append('rosa')
print(warm)
print(hot)
print()

# MUTATION AND ITERATION
# avoid iterating over a list in a loop:
# First Example: loop will omit elements cause indexing doesn't follow changes
# Second Example: ok


def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)


List1 = [1, 2, 3, 4]
List2 = [1, 2, 5, 6]
remove_dups(List1, List2)
print(List1)


def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)


List1 = [1, 2, 3, 4]
List2 = [1, 2, 5, 6]
remove_dups(List1, List2)

print(List1)
