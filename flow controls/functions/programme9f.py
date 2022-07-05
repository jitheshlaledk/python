#create a calculator

#1 for addition
#2 for substraction
#3 multiplication
#4 division
#enter ur choice
#num1
#nu

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("1.addition\n"
      "substraction\n"
      "multiplication\n"
      "division")
choice=int(input("enter your choice"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
if(choice==1):
    print(num1,"+",num2,add(num1,num2))
elif(choice==2):
    print(num1,"-",num2,sub(num1,num2))
elif(choice==3):
    print(num1,"*",num2,mul(num1,num2))
elif(choice==4):
    print(num1,"/",num2,div(num1,num2))

else:
    print("invalid")
