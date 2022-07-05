#nested list

lst=[[101,'arun','k',26,'bigdata',1900],
     [102,'amal','l',27,'python',1500],
     [103,'vishnu','t',24,'bigdata',1250]]

#print seperate list

# for i in lst:
#     print(i[1],i[2],i[3],i[4])#for collect a aprticular data

# for i in lst:
#     print(i[1:5])

# for i in lst:
#     if(i[3]>25):
#         print(i[1],i[2],i[3],i[4],i[5])

# for i in lst:
#     if(i[4]=='bigdata'):
#         print(i[1],i[2],i[3],i[5])

# #salary above 1750&age above25
# for i in lst:
#     if(lst[5]>1750 and i[3>25]):
#       print(i[1],i[2],i[3],i[4],i[5])


#total salary
su=0
for i in lst:
    su+=i[5]
print(su)



