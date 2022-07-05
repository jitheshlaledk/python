#inheritance with constructor
#person
#arg=name age place
#student=roll no,dept,college(parent)
#super keyword

class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print1(self):
        print(self.name,self.age,self.place)
class student(person):
    def __init__(self,roll,dept,college,name,age,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dept=dept
        self.college=college
    def print2(self):
        print(self.roll,self.dept,self.college)
ob=student("jithesh",26,"abl",29,"abc","wyd")
ob.print2()
ob.print1()