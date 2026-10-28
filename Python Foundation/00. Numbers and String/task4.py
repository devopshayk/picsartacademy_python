from fractions import Fraction
from decimal import Decimal


fraction1_num = Fraction(2, 3)
fraction2_num = Fraction(4, 9)

print("\t Fractions' manipulations")
print(f"Adittion: {fraction1_num + fraction2_num}")
print(f"Subtraction: {fraction1_num - fraction2_num}")
print(f"Multiplication: {fraction1_num * fraction2_num}")
print(f"Division: {fraction1_num / fraction2_num}\n\n")


small_decimal = Decimal("0.1")
normal_decimal = Decimal("2.2")

print("\t Decimals' manipulations")
print(f"Addition:  {small_decimal + normal_decimal}")
print(f"Subtraction:  {small_decimal - normal_decimal}")