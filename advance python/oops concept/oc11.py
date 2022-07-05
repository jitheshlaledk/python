#multiple inheritance
#one child class and more than one parent class
class A:
    def printa(self):
        print("inside class A")
class B:
    def printb(self):
        print("inside class b")
class D:
    def printd(self):
        print("inside class D")
class C(A,B,D):
    def printc(self):
        print("inside class C")


ob=C()
ob.printc()
ob.printb()
ob.printa()
ob.printd()