#low to uper
#print even numbers
lowerlimit=int(input("enter lower limit"))
uperlimit=int(input("enter uper limit"))

while(lowerlimit<=uperlimit):
    if(lowerlimit%2==0):
        print(lowerlimit)
    lowerlimit+=1

