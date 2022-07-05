
#print highest mark student details
lst = [('vinay', 45), ('arjun', 35), ('amal', 65), ('vipin', 56)]
# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def print(self):
#         print(self.name,self.mark)


m=[]
for i in lst:
    m.append(i[1])
maxi=max(m)
for j in lst:
    if j[1]==maxi:
        print(j[0],maxi)














