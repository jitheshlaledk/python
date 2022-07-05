#how to generate a exception
age=int(input("enter age"))
if age>=18:
    print("eligible")
else:
    raise Exception("not allowed")