N = int(input("Enter num for calculate factorial: "))

nn = N
sum = 1

while(N):
    sum *= N
    N -= 1

print(f"{nn}'s factorial = {sum}")