#linear search
#complexity increase  - draw back

#using binary search instead of linear search

#binary search

# lst=[7,4,3,1,2]
# #sort the given list(ascending order)
# lst=sorted(lst)
#lower=0
#upper=length(lst)-1

#calculate mid
#mid=(lower+upper)//2


#three condition

#1.search element>lst[mid]   if its true
       #low=mid+1
#search element<lst[mid]
       #upper=mid-1
#search element==lst[mid]   element found
    #return lst



lst=[1,6,8,10,2,9,7,32]
lst.sort()
value=int(input("enter a value"))
low=0
upp=len(lst)-1
flag=0





while(low<=upp):
    mid = (low + upp) // 2
    if(value>lst[mid]):
        low=mid+1
    elif(value<lst[mid]):
        upp=mid-1
    elif(value==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")






