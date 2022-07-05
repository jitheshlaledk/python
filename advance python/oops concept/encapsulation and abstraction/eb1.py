#do it as as seminar presentation
#do it on monday



#encapsulation
#its a mechanism to prevent direct modifications for some attributes using double underscore

class person:
    def __init__(self):
        self.__age=22
    def printage(self):
        print("age is",self.__age)
    def setage(self,age):
        self.__age=age


p=person()
p.printage()
p.age=26
p.printage()
p.setage(24)
p.printage()



