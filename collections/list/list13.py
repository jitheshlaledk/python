#lst=[4,3,2,1]
#read a element in console
#print pairs of elements


#6

lst=[4,3,2,1]
read=int(input("enter a number"))
lst.sort()
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==read):
        print("pairs are",lst[low],lst[upp])
        break
    elif(data>read):
        upp=upp+1
    else:
        low=low+1
