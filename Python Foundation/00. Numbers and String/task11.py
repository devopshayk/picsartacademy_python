string = input("Write word for check A-Z: ")

first_expression = string[0] == 'A' or string[0] == 'a'
second_expression = string[-1] == 'Z' or string[-1] == 'z'

print(f"Starts with A or a: {first_expression}, Ends with Z or z: {second_expression}")