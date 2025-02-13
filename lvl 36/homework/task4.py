def find_character_index(string, char):
    return string.find(char)
string = "Hello, world!"
char = "w"
index = find_character_index(string, char)
print(f"Character '{char}' found at index: {index}" if index != -1 else "Character not found.")