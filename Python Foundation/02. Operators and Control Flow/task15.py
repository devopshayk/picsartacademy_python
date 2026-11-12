numbers = [3, 7, 1, 9, 4]

max = numbers[0]

for i in range(len(numbers)):
    if max < numbers[i]:
        max = numbers[i]

print(f"Max element = {max}") 