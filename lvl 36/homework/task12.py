def is_lowercase_only(string):
    return string.islower() and string.isalpha()
string = input("Enter a string: ")
if is_lowercase_only(string):
    print("The string contains only lowercase letters.")
else:
    print("The string does not contain only lowercase letters.")