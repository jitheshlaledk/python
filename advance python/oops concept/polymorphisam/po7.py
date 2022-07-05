#three class
#person   name age place
#employ   empid dept salary
#student  roll  college
#student person and employ

class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class employ:
    def __init__(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary
class student(person,employ):
    def __init__(self,roll,college,name,age,place,id,dept,salary):
        person.__init__(self,name,age,place)
        employ.__init__(self,id,dept,salary)
        self.roll=roll
        self.college=college
    def printstu(self):
        print(self.roll,self.college,self.name,self.age,self.place,self.id,self.salary)

ob=student("jithesh",26,"abl",124,"che2",6000,26,"wyd")
ob.printstu()