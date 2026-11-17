def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

num1 = int(input("Write num1: "))
num2 = int(input("Write num2: "))

op = input("Write operation: + - / * ")
if(op == '+'):
    print(f"Result is: {add(num1, num2)}")

elif(op == '-'):
    print(f"Result is: {subtract(num1, num2)}")

elif(op == '*'):
    print(f"Result is: {multiply(num1, num2)}")

elif(op == '/'):
    print(f"Result is: {divide(num1, num2)}")

else:
    print("Invalid::::")