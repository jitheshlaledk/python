#polymorphism
#many forms
#check inside method(handle same method name but different functions)
#method overloading
#method overriding

#method overloading
#in python latest method will support
#in python method overloading does not support
#same method name and different number of arguments
#.......................................
class add:
    def arg1(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class add1(add):
    def arg1(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
ob=add1()
ob.arg1(10,20,30)



