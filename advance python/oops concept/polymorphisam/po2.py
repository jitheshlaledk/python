#method overriding
#add 2  inherit add   sum
#same method name and same number of arguments
class add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

class add2(add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
ob=add2()
ob.sum(15,20)

