def manual_isdigit(user_str):
    # ცარიელი სტრინგი არ ითვლება ციფრებად
    if not user_str:
        return False
    
    for char in user_str:
        if char not in "0123456789":  # ვამოწმებთ, არის თუ არა სიმბოლო ციფრი
            return False
    return True

# ტესტირება
print(manual_isdigit("12345"))  # True
print(manual_isdigit("12a45"))  # False
print(manual_isdigit(""))      # False
print(manual_isdigit("007"))   # True