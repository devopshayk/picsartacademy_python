N = int(input("Enter num for sum: "))
nums_sum = 0

for i in range(0, N + 1):
    if i % 2 == 0:
        nums_sum += i

print(nums_sum)