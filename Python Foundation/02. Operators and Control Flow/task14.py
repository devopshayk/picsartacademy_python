word = input("Write strring for check polindromic: ")

if word == word[::-1]:
    print(f"Word {word} is polindrome")
else:
    print(f"Word {word} isn't polindrome")