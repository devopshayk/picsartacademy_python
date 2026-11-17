

# parz tiv, calculator, random range game


# for num in range(2, 101):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num)

#######################


# a = float(input("First number: "))
# op = input("Operation: ")
# b = float(input("Second number: "))

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)

#######################

# import random

# number = random.randint(0, 10)

# while True:
#     n = int(input("Write the number: "))

#     if n == number:
#         print("You found it! ")
#         break



######################



# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

# unique = set(numbers)

# for i in unique:
#     print(i)


# text = "apple banana apple orange banana apple"
# dict1 = {}

# for word in text.split():
#     if word in dict1:
#         dict1[word] += 1
#     else:
#         dict1[word] = 1

# print(dict1)



# scores = {
#     "John": 85,
#     "Mike": 92,
#     "Anna": 78,
#     "David": 95,
#     "Kate": 88
# }

# max = 0
# max_name = ""

# for key, value in scores.items():
#     if max < value:
#         max = value
#         max_name = key

# print(max_name, max)


# is_prime = True

# n = 8

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break


# if is_prime:
#     print(True)
# else:
#     print(False)


# text = "programming"

# dictionary = {}

# for i in text:
#     if i in dictionary:
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1

# print(dictionary)

# students = {
#     "Hayk": {
#         "Python": 90,
#         "Math": 85,
#         "English": 75
#     },
#     "Aram": {
#         "Python": 80,
#         "Math": 95,
#         "English": 90
#     },
#     "David": {
#         "Python": 95,
#         "Math": 75,
#         "English": 85
#     }
# }


# dicti = students.copy()
# #print(dicti)

# numbers = (1, 2, 3, 4)

# a, *b = numbers

# print(a, b)


