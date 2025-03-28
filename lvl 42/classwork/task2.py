# ვარიანტი 1: max() ფუნქციის გამოყენებით
def max_number(lst):
    return max(lst)

# ვარიანტი 2: ციკლით პოვნა
def max_number_manual(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# ტესტი
numbers = [3, 7, 1, 9, 4]
print(max_number(numbers))         # 9
print(max_number_manual(numbers))  # 9




def positive_squares_sum(lst):
    return sum(x**2 for x in lst if x > 0)

# ტესტი
numbers = [-3, 4, -1, 2, -5, 6]
print(positive_squares_sum(numbers))  # 4² + 2² + 6² = 16 + 4 + 36 = 56