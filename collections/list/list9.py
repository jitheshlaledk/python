#1-75 add
#create a even&odd list
#sum of list odd sum list and even list

list=[]
evenlist=[]
oddlist=[]

for i in range(1,76):
    list.append(i)
    if(i%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)
print(list)
print(evenlist)
print(oddlist)
print(sum(list))
print(sum(evenlist))
print(sum(oddlist))