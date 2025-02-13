def is_all_uppercase(string):
    return string.isupper()
string = input("Enter a string: ")
if is_all_uppercase(string):
    print("All characters in the string are uppercase.")
else:
    print("The string contains lowercase characters.")