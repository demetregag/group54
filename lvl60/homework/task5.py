def add_two_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

add_two_numbers()
