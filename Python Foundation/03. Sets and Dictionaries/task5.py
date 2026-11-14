numbers = [5, 8, 2, 8, 5, 10, 2, 7]

set_numbers = set(numbers)

new_dict = {}


for i in set_numbers:
    new_dict[i] = numbers.count(i)

print(new_dict)