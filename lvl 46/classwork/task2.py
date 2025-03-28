def no_duplicates(user_list):
    return list(dict.fromkeys(user_list))

print(no_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(no_duplicates(["apple", "banana", "apple", "orange", "banana"]))
print(no_duplicates([10, 20, 30, 10, 20, 40, 50]))
