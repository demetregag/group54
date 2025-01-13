num1=float(input("put any number"))
num2=float(input("put any number"))

if num1>num2: range1 = range(num2,num1+1)
elif num2 >num1: range1 = range (num1, num2+1)
else:print("numbers are equal")

for i in range1: print(i)