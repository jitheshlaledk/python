#exception handling
#how to handling unexpexted errors in code
n1=int(input("enter n1"))
n2=int(input("enter n2"))

try:
    print(n1/n2)
except Exception as e:
    print("error occured",e)




#three blocks using to handle un expected errors

#1.try block   :  exception chance code define
#2.except      :   solution add
#3.finally