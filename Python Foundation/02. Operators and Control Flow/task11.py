num = int(input("Write number for sum digits: "))

digit_sum = 0

while(num):
    digit_sum += num % 10
    num //= 10

print(digit_sum)