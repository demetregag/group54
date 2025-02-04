def manual_capitalize(user_str):
    if not user_str:
        return ""
    first_letter = user_str[0].upper()  # პირველი სიმბოლო დიდ ასოში
    remaining_letters = user_str[1:].lower()  # დანარჩენი სიმბოლოები პატარა ასოებში
    return first_letter + remaining_letters


user_input = input("გთხოვთ, შეიყვანეთ სთრინგი: ")


capitalized_str = manual_capitalize(user_input)
print(capitalized_str)