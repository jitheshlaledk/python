ll=int(input("enter ll"))
ul=int(input("enter ul"))
od_sum=0
ev_sum=0

for i in range(ll,ul+1):
    if(i%2==0):
        ev_sum+=i
    else:
        od_sum+=i
print(ev_sum)
print(od_sum)
