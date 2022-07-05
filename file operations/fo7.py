f=open("C:/Users/jithe/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    loac=data[-1]
    if loac not in dic:
        dic[loac]=1
    else:
        dic[loac]+=1
print(dic)