group1 = {"Anna", "Tom", "John", "Lilit"}
group2 = {"Tom", "Karen", "Anna", "Meri"}

new_list = []

for i in group1:
    for j in group2:
        if i == j:
            new_list.append(i)

for i in new_list:
    print(i)