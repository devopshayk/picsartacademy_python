student = {
    "math":90,
    "physics":85,
    "english":95
}

gpa = 0

for i in student.values():
    gpa += i


gpa //= len(student)
print(f"GPA = {gpa}")