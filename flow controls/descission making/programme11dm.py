sub1=int(input("enter sub1 mark"))
sub2=int(input("enter sub2 mark"))
sub3=int(input("enter sub3 mark"))
sub4=int(input("enter sub4 mark"))

total=sub1+sub2+sub3+sub4

if(total>=180):
    print("A+")
elif(total>=160)&(total<=179):
    print("A")
elif(total>=140)&(total<=-159):
    print("B+")
elif(total>=120)&(total<=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(total>=80)&(total<=99):
    print("c")
else:
    print("failed")