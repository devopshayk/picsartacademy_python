number = int(input("Enter number: "))

if number % 3 == 0 and number % 5 == 0:
    print("3 and 5")
elif number % 3 == 0:
    print("3")
elif number % 5 == 0:
    print("5")
else:
    print("---Nothing---")