def safe_list_removal():
    my_list = ['apple', 'banana', 'cherry', 'date']
    
    try:
        item = input("Enter an item to remove: ")
        my_list.remove(item)
        print(f"The item '{item}' has been removed.")
    except ValueError:
        print("Error: The item is not in the list.")

safe_list_removal()
