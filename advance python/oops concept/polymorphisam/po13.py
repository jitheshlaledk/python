#sum values

def printvalue(*args):
    print(sum(args))
printvalue(10,20,30)


def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(5,10))
