def count_vowels(text):
    count = 0

    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or \
           i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
           
            count += 1

    return count


string = "PoghOsyann HAyk"
print(f"Count of vowels: {count_vowels(string)}")