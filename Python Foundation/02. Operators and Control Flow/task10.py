num = int(input("Enter number: "))

n_clone = num

while(num):
    if n_clone % num == 0:
        print(num)
    num -= 1
