def check_all_lowercase(string):
    return string.islower()
string = input("Enter a string: ")
if check_all_lowercase(string):
    print("All characters in the string are lowercase.")
else:
    print("The string contains uppercase characters.")