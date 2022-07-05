class person:
    def printper(self,name,age):
        self.name=name
        self.age=age
class child(person):
    def printch(self,place,school):
        self.place=place
        self.school=school
class student(child):
    def printstu(self,roll,dept,college):
        self.roll=roll
        self.dept=dept
        self.college=college
        print(self.name,self.age,self.place,self.dept,self.college)
s=student()
s.printper("jl",23)
s.printch("abl","gv")
s.printstu(26,"che","sby")


