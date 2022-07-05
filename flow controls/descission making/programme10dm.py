#largest among three numbers
num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

if(num1>num2)&(num1>num3):
    print("number1 is largest")
elif(num2>num1)&(num2>num3):
    print("number 2 is largest")
else:
    print("number 3 is largest")

