numbers = [4, 7, 2, 9, 8, 5]

count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 != 1:
        count += 1

print(count)