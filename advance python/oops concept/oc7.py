#static variable related to class
#luminar class
#name roll age institution name fees

class luminar:
    institution="luminar"
    fees=29500
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,luminar.institution,luminar.fees)

s1=luminar()
s1.setvalue("anu",21,26)
s1.printvalue()

s2=luminar()
s2.setvalue("rahul",38,20)
s2.printvalue()