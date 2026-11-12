age = int(input("Write your age: "))

if age < 18 and age > 0:
    print("You are minor")
elif age >= 18 and age <= 64:
    print("You are adult")
elif age >= 65:
    print("You are senior")
else:
    print("Invalid age:")