def list_index_access():
    my_list = [10, 20, 30, 40, 50]
    
    try:
        index = int(input("Enter an index number: "))
        print(f"The element at index {index} is: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

list_index_access()
