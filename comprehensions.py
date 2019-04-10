
print('LIST COMPREHENSION')
x = [x * 2 for x in range(10)]
print(x)
x = list(range(0, 19, 2))
print(x)


print('SET COMPREHENSION')
x = {x * x for x in range(-9, 10)}
print(x)

print('DICT COMPREHENSION')
x = {x: x * x for x in range(5)}
print(x)

print('TUPLE COMPREHENSION')
x = tuple(x for x in range(5))
print(x)
x = tuple(range(5))
print(x)


print('COMBINING LISTS WITH LIST COMPREHENSION')
nums = [1, 2, 3]
letters = ['a', 'b', 'c', 'd', 'e']
nums_letters = [[num, let] for num in nums for let in letters]
print(nums_letters)
