numbers = [4, 8, 15, 16, 23, 42]

user_num = int(input("Write num for detection: "))

for i in range(len(numbers)):
    if numbers[i] == user_num:
        print(f"{user_num} has been found")
        break
print(f"{user_num} hasn't been found")