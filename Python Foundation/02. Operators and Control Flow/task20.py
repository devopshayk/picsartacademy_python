numbers = (4, 7, 1, 8, 2)

min_el = numbers[0]

for i in range(len(numbers)):
    if min_el > numbers[i]:
        min_el = numbers[i]

print(f"Min element: {min_el}")