#how to identify an exception
lst=[1,2,3,4]
i=int(input("enetr a range"))
try:
    print(lst[i])
except Exception as e:
    print("exception occured",e)