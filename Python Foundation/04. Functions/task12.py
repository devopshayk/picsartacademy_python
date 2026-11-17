def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = "level"
print(f"Is palindrome: {is_palindrome(string)}")