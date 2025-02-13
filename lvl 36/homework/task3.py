string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

index = string.find(substring)

print(f"Substring found at index: {index}" if index != -1 else "Substring not found.")