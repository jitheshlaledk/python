#question6

ll=int(input("enter lower limit"))
ul=int(input("enter upper limit"))
odd=0
even=0

for i in range(ll,ul+1):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)
