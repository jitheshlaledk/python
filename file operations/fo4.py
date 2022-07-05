f=open("C:/Users/jithe/PycharmProjects/april_python_django/file operations/numbers","r")
lst=[]
even=[]
odd=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(sum(lst))
for i in lst:
    if(int(i%2==0)):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print(sum(odd))
print(sum(even))