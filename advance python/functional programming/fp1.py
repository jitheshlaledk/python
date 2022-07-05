#functional programming used for reduce length of a programme

#lamda
#map
#filter
#reduce
#list-comprehension


#lambda
#.....................

#its a annonimous function-(non identity)
#variable name lambda
# f=lambda num1,num2:num1+num2
# print(f(10,20))
# print(f(5,60))

# f1=lambda numb1,numb2,numb3:numb1*numb2*numb3

# print(f1(1,6,8))

#find cube of a number
# f=lambda num1:num1**3
# print(f(10))



#map and filter functions
#...............................................................

#map
#corresponding answer of every element of list

#syntax

#variablename=lst(map(angument1,argument2))
#variable name=lst(filter(arg1,arg2))
#arg1=function name
#arg2=iterable

# lst=[1,2,3,4,5,6,7,8,9,10]
# data=list(map(lambda num:num**2,lst))
# print(data)
#filter
# data=list(filter(lambda num:num%2==0,lst))
# print(data)
#add 1 with every value
# d=list(map(lambda num:num+1,lst))
# print(d)

#list comprehension
#............................

# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)
#to reduce length
# lst=[print range]#add numbers to list
# lst=[i for i in range(1,76,4)]
# print(lst)

#one to hundred even numbers

# lst=[(i,"even") for i in range(1,51) if i%2==0]
# print(lst)


