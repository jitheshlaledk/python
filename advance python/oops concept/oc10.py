#two clss create
#person,name,age,place
#student=roll no,dept

class person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)
class student(person):
    def setvalue1(self,roll,dept):
        self.roll=roll
        self.dept=dept
    def print1(self):
        print(self.name,self.age,self.place,self.roll,self.dept)

s=student()
s.setvalue("vinay",26,"abl")
s.setvalue1("101","data")

s.print1()


#create two clss and inherence
#multiple in heritance

