f=open("C:/Users/jithe/PycharmProjects/april_python_django/file operations/numbers","r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(sum(lst))
#sum
#odd
#eeven
#odd sum
#even sum
