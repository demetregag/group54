def check_lowercase(user_str):
    if user_str.islower():
        print(user_str)
    else:
        print("ტექსტი არ არის მთლიანად პატარა ასოებით.")

text = input("შეიყვანეთ ტექსტი: ")

check_lowercase(text)
