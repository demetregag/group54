def count_character_occurrences(string, char):
    return string.count(char)
string = "Hello, how are you doing today?"
char = input("Enter a character to search for: ")
if len(char) == 1:
    count = count_character_occurrences(string, char)
    print(f"The character '{char}' appears {count} times in the string.")
else:
    print("Please enter a single character.")