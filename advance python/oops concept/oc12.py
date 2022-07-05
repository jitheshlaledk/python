#person
#name age
#parent
#place phone no
#employ
#id designation salary
#print employ name age place phone id design salary


class person:
    def set1(self,name,age):
        self.name=name
        self.age=age
class parent:
    def set2(self,place,phno):
        self.place=place
        self.phno=phno
class employ(person,parent):
    def set3(self,id,degin,salary):
        self.id=id
        self.design=degin
        self.salary=salary
        print(self.name,self.age,self.place,self.phno,self.id,self.design,self.salary)

s=employ()
s.set1("jithesh",23)
s.set2("wyd",85645)
s.set3("df","manager",25000)
