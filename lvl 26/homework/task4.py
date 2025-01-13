password="GOA BEST"
count=0
something=input("enter your password")
while password != something:
    count+=1
    print("password is incorrect")
    break
print("password is correct")
print(count)