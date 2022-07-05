#name roll no dept college

class student:
    def setvalue(self,name,roll_no,dept,college):
        self.name=name
        self.rollno=roll_no
        self.dept=dept
        self.college=college
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.dept)
        print(self.college)

st1=student()
st1.setvalue("anu",26,"che","cochin")
st1.printvalue()

st2=student()
st2.setvalue("ann",27,"bio","thrissur")
st2.printvalue()

st3=student()
st3.setvalue("aparna",14,"phy","tvm")
st3.printvalue()
