
# 1)

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.y)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

print('\n', '#' * 22, '1-2', '#' * 22, '\n')
coord1 = Coordinate(0, 0)
coord2 = Coordinate(1, 1)
print(coord1.distance(coord2))

coord2 = Coordinate(2, 2)
print(coord1.distance(coord2))

# Another way to use class:
coord1 = Coordinate(0, 0)
coord2 = Coordinate(1, 1)
print(Coordinate.distance(coord1, coord2))

coord2 = Coordinate(2, 2)
print(Coordinate.distance(coord1, coord2))

# As no __str__ method is defined for the class print returns default uninformative statement:
print(coord2)
print()


# 2)

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.y)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


coord1 = Coordinate(7, 4)
print(coord1)
print('\n', '#' * 22, '3', '#' * 22, '\n')

# 3)


class Fraction(object):
    def __init__(self, numerator, denominator):
        assert type(numerator) == int and type(denominator) == int, "ints not used !"
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        top = self.numerator * other.denominator + other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = self.numerator * other.denominator - other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        return Fraction(top, bottom)

    def __float__(self):
        return self.numerator/self.denominator

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


a = Fraction(2, 4)
b = Fraction(3, 7)
c = a + b
print(a)
print(c)
print(type(c))
print()

# Ways of using methods:
print(float(a), '=', a.__float__())
print(c.inverse(), '=', c.inverse().__float__())
print(c.inverse(), '=', float(c.inverse()))