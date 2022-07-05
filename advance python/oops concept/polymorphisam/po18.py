dic1={'physics':56,
      'maths':65,
      'history':80}
lst={}
res=lst.fromkeys(dic1)
print(min(dic1,key=dic1.get))
#lowest score subject name

