correct_num=10
password_num=int (input("entre password"))
while password_num!=correct_num:
    print("incorrect password")
    password_num=int(input("enter password"))
print("correct guess")