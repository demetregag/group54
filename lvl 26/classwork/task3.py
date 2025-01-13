num=int(input("enter your grade"))

if num >=90:
    print("A")
elif num<=89 :
    if num>=80:
        print("B")
elif num<=79:
    if num>=70:
        print("C")
elif num<=69:
    if num>=60:
        print("D")
else:
    print("F")