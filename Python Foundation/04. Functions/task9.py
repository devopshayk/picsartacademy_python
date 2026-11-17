def sum_list(numbers):
    sum = 0

    for i in numbers:
        sum += i

    return sum


lst = [33, 123, -31, 2, 9]
print(f"Sum of list: {sum_list(lst)}")