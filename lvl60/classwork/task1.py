try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except ValueError:
    print("Please enter numbers only!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception:
    print("Something went wrong.")