def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

# Example usage:
print(greet("John", "John"))  # Output: Hello boss
print(greet("Alice", "Bob"))  # Output: Hello guest