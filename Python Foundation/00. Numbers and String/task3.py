from fractions import Fraction
from decimal import Decimal


int_num = 1
float_num = 1.1

print(int_num == float_num)


decimal_num = Decimal("2.2")
float_num = 2.2

print(decimal_num == float_num)


fraction1_num = Fraction(1, 2)
fraction2_num = Fraction(2, 4)

print(fraction1_num == fraction2_num)