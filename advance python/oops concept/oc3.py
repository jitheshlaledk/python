class person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)

pe1=person()
pe1.setvalue("anu",26,"kochi")
pe1.printvalue()

pe2=person()
pe2.setvalue("rajiv",26,"wayanad")
pe2.printvalue()

pe3=person()
pe3.setvalue("rahul",25,"calicut")
pe3.printvalue()


#same value canot apply in different function
        #converted in to instance argument using self
