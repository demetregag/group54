def string_to_integer():
    try:
        user_input = input("Enter a number: ")
        result = int(user_input)
        print(f"The integer value is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

string_to_integer()
