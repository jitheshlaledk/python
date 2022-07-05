lst=[5,6,7,4,3]
try:
    print(lst[5])
except:
    print("out of range")
finally:
    print("inside")