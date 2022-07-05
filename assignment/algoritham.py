#sentiment analysis algoritham
#comments calculate  poitive or negative

#type comments on file
#fetch comments and analyse positive or negative

#split
#two dictionary on eis positive and another negative
#1.tokenisation[good company] split
# create dictionary positive and negative
#comapre with dictionay
#         if positrive dictionary word +1
#         neutral value 0
#         negative value  -1
#final count positive value the comment is positive comment
sp=["@","#","(",")"]


v = 0
objects=open("C:/Users/jithe/PycharmProjects/april_python_django/assignment/algorithamfile","r")
positive=["good","awesome"]
negative=["bad","small"]
for object in objects:
    data=object.rstrip("\n").split(" ")
    # print(len(data))
    if positive in data:
        v+=1
    elif negative in data:
        v-=1
print(v)












