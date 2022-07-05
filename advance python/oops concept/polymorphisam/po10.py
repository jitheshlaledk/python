
# id fname lname age proff locat
lst=[]
class empoly:
    def __init__(self,id,fname,lname,age,proff,location):
        self.id=id
        self.fname=fname
        self.lnmae=lname
        self.age=age
        self.proffession=proff
        self.location=location
    def print1(self):
        print(self.id,self.fname,self.lnmae,self.age,self.proffession,self.location)

f=open("C:/Users/jithe/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    proffession=data[4]
    location=data[5]

    ob=empoly(id,fname,lname,age,proffession,location)
    for i in data:
        lst.append(data[1:5])
print(lst)