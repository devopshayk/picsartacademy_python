from decimal import Decimal
from fractions import Fraction


a = 5
b = 5.0

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = Decimal("0.1")
b = 0.2

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = Fraction(1, 2)
b = Fraction(2, 3)

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)