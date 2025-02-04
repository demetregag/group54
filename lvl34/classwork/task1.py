def კალკულატორი(num1, num2, ოპერატორი):
    if ოპერატორი == '+':
        print(num1 + num2)
    elif ოპერატორი == '-':
        print(num1 - num2)
    elif ოპერატორი == '*':
        print(num1 * num2)
    elif ოპერატორი == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("გაყოფა ნულზე შეუძლებელია")
    else:
        print("მიუთითეთ სწორი ოპერატორი")

# ფუნქციის გამოძახება სხვადასხვა არგუმენტებით
კალკულატორი(10, 5, '+')  # 15
კალკულატორი(20, 4, '-')  # 16
კალკულატორი(6, 3, '*')   # 18