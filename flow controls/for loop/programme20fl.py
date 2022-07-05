#read a lower limit and upper limit
#print prime numbers between lower and uper
lnum=int(input("enetr lower limit"))
unum=int(input("enter upper limit"))

for i in range(lnum,unum+1):
    rr=0
    for j in range(2,i):
        if(i%j==0):
            rr=1
            break
    if(rr==0):
        print(i,end=' ')
