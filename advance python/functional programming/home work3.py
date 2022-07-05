f=open("interview1","r")
s="!@#$%^&*()/"
for i in f:
    data=i.rstrip("\n").split(",")
    string=""
    if s not in data:
        string+=data
print(string)

