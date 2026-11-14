employees = {
    "Alice": 850000,
    "Bob": 620000,
    "Charlie": 910000,
    "Diana": 540000,
    "Eve": 730000
}


money = 0

for i in employees:
    money += employees[i]
    
    if employees[i] >= 700000:
        print(i)

print(f"Whole amount = {money}")
print(len(employees))