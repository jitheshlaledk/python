#read three numbers fron console
#second largest number

num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

# if(num1>num2)&(num1<num3):
#     print("second largest number is",num1)
# elif(num2>num3)&(num2<num1):
#     print("second largest number is",num2)
# elif(num2<num3)&(num2>num1):
#     print("second largest number is",num2)
# elif(num1<num2)&(num1>num3):
#     print("second largest number is",num1)
# elif(num3>num2)&(num3<num1):
#     print("second largest number is",num3)
# else:
#     print("second largest number is",num3)

    #nested if
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("second largest is number2",num2)
    else:
        print("second largest is num3",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("second largest is number1",num1)
    else:
        print("second largest is num3",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largest is number1",num1)
    else:
        print("second largest is number2",num2)

