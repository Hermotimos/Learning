
# MRO - Method Resolution Order
# Rules for determining which attribute/method of a set of classes in inheritance apply


"""
MRO search rules:
    1) children precede parents
    2) when child inherits from multiple parents and grandparents,
        the search follows the order specified in __bases__ attribute:
            A. first level bases are listed in the order they are provided in class definition
            B. others: more complicated algorithms

The first class that has the searched attribute / method is chosen

* 'object' is always the ultimate class in MRO.
* __bases__ returns class from which a class directly inherits

"""



# --------------------------------------
# [1]

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(C, B):         # mind the order: first C, then B
    pass

"""
      A
    /   \
   /     \
  B       C
   \     /
    \   /
      D
"""
print()
print(D.__bases__)      # (<class '__main__.C'>, <class '__main__.B'>)
print(B.__bases__)      # (<class '__main__.A'>,)

print(D.mro())
print(D.__mro__)
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


# --------------------------------------
# [2]

class Stock:
    pass

class Warehouse:
    pass

class Produce(Stock, Warehouse):
    pass

class Fruit(Produce):
    pass

"""
    Stock   Warehouse
       \     /
        \   /
       Produce
          |
          |
        Fruit
"""
print()
print('Stock:', Stock.__bases__)
print('Warehouse:', Warehouse.__bases__)
print('Produce:', Produce.__bases__)
print('Fruit:', Fruit.__bases__)
print('MRO:', Fruit.__mro__)
print()


# --------------------------------------
# [3]

class Supplier:
    pass

class Distributor:
    pass

class ShopWarehouse(Supplier, Distributor):
    pass

class ShopDispatch(ShopWarehouse):
    pass

# class Shelf(Distributor, ShopDispatch)
#     pass
# >> TypeError: Cannot create a consistent method resolution order (MRO) for bases Distributor, ShopDispatch

class Shelf(ShopDispatch, Distributor):
    pass
    # this one works, but it's messy:
    # Dispatch stuff is already accessible via Dispatch -> ShopWarehouse -> ShopDispatch -> Shelf
    # SOLUTION: remove inheritance from Distributor in Shelf class

"""
      Supplier    Distributor
          |      /    /
          |     /    /
    ShopWarehouse   /
          |        /
          |       /
    ShopDispatch /
          |     /
          |    /
         Shelf
"""







"""
https://www.youtube.com/watch?v=X1PQ7zzltz4
"""

# ---------------------------------
# super() #1

class Basic:
    def func(self):
        print('Basic')

class Derived(Basic):
    def func(self):
        print('Derived - before')
        super().func()
        print('Derived - after')

obj = Derived()
obj.func()

# super() is for calling methods of the superclass ?? Not exactly.
# More precisely, super() follows the MRO, so it calls the 'next in MRO superclass'



# We want a dictionary that prints out info each time it's modified.
# We achieve that by subclassing the builtin 'dict' and addint prints.
# super() ensures that we preserve all the original functionalities of 'dict'.

class LoggingDict(dict):
    def __setitem__(self, __key, __value):
        print(f"Setting {__key}: {__value}")
        super().__setitem__(__key, __value)

    def __getitem__(self, __key):
        print(f"Getting {__key}")
        super().__getitem__(__key)

    def __delitem__(self, __key):
        print(f"Deleting {__key}")
        super().__delitem__(__key)


print()
mydict = LoggingDict()
mydict['a'] = "aaaaa"
mydict['b'] = "bbbbb"
mydict['c'] = "ccccc"
mydict['a']
del mydict['a']


# ---------------------------------
# super() #2

# super() follows MRO until it finds the method or reaches the end


class Lvl1(dict):
    pass

class Lvl2(Lvl1):
    pass

class Lvl3(Lvl2):
    def __setitem__(self, __key, __value):
        print(f"Setting {__key}: {__value}")
        super().__setitem__(__key, __value) # this still calls dict's __setitem__()

print()
mydict = Lvl3()
mydict['a'] = "aaaaa"



"""

Important by using super():
    1) ensure all classes in the hierarchy also call super in the overriden method,
        so that it can reach further and further until it actually finds the method
    2) use *args, **kwargs apartfrom named parameters to ensure compatibility of overriden methods
    3) super() does not return the superclass or the 'next in line' class of the hierarchy tree;
        it returns a Super object - a proxy that wraps that class and forwards
        the search for attributes/methods to it

"""

class SimpleProxyObj:
    """A basic example of a proxy class."""

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        # __getattr__() is called when you do: someobject.somemethod/attribute
        return getattr(self.obj, item)


obj = [1, 2, 3]
proxy = SimpleProxyObj(obj)
proxy.append(4)     # it's forwarded to obj, where from it gets attribute 'append'
print()
print(obj)
print(proxy)
assert obj == [1, 2, 3, 4]

# But super() does something different.
# I inspects the stack frame to find meta info and move through the inheritance structure.
# More on how super() actually works: https://youtu.be/X1PQ7zzltz4?t=721
