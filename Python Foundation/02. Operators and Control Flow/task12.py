N = int(input("Write num for calculate digits: "))

count = 0

while(N):
    count += 1
    N //= 10

print(count)