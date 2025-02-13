def find_character_index(string, char):
    return string.find(char)
string = "Programming is fun!"
char = input("Enter a character to search for: ")
if len(char) == 1:
    index = find_character_index(string, char)
    print(f"The character '{char}' appears first at index: {index}" if index != -1 else "Character not found.")
else:
    print("Please enter a single character.")