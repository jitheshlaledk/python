#inheritance
#method and variables
#features(method and variables) of one(parent) class assigned to another(child) class
#class a (parent)
#class b(child)

class a:
    def printa(self,num1):
        self.num1=num1
        print("inside class a",self.num1)
class  b(a):
    def printb(self,num2):
        self.num2=num2
        print("inside class b",self.num2,self.num1)

s=b()
s.printa(65)
s.printb(64)
#a is parent class/base class/super class
#b is child class/sub class/derived class

