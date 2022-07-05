employ=['vinay','arun']
default={'designation':'python','salary':1000}
dic={}
#new function fromkeys:it returns a dictionary with specified key and specified values
res=dic.fromkeys(employ,default)
print(res)

print(res['arun'])


#     dic[i]=default
# print(dic)