PI = 3.14159

def circle_area(radius):
    return PI * (radius ** 2)

num = int(input("Write num for calculate radius: "))
print(f"Area = {circle_area(num)}")