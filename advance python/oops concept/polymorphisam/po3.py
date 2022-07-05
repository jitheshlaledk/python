class a:
    def printa(self):
        print("inside class A")

class b(a):
    def printa(self):
        print("inside class b")
class c(b):
    def printa(self):
        print("inside class c")
#latest child class will excecute
ob=c()
ob.printa()