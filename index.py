# name = input("Write your name: ")
# age = int(input("Write your age: "))

# if(age >= 18):
#     print(f"{name} is adult")
# else:
#     print(f"{name} is minor")

numbers = [3, 7, 2, 9, 4, 1, 8]

sum = 0
max = numbers[0]
count_z = 0

for i in range(len(numbers)):
   # print(numbers[i])
    sum += numbers[i]
    if(max < numbers[i]):
        max = numbers[i]

    if(numbers[i] % 2 == 0):
        count_z += 1

print(f"Sum = {sum}")
print(f"Maximum element: {max}")
print(f"Zuygeri qanak: {count_z}")