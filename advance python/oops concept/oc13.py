#multi level inheritance
class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printb(self):
        print("inside class B")
class C(B):
    def printc(self):
        print("inside class C")

ob=C()
ob.printa()
ob.printb()
ob.printc()