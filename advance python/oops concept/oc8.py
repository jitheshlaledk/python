#cnstructor
#.........................
#used to define a instance variable inside a object
#init

class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=person("arun",26,"ekm")
pe1.printvalue()
pe2=person("rahul",24,"tsr")
pe2.printvalue()