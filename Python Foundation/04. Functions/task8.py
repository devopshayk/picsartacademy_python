def largest(lst):
    maX = lst[0]

    for i in lst:
        if maX < i:
            maX = i
    
    return maX

ls = [1, 254, -3, 14]
print(f"Largest element in list: {largest(ls)}")