def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    print(lst)
my_list = [10, 20, 30, 40, 50]
remove_one_element(my_list, 2)