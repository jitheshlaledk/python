cost_of_bike=int(input("enter cost of bike"))

if(cost_of_bike>100000):
    print("tax of bike=",cost_of_bike/100*15)
elif(cost_of_bike>50000)&(cost_of_bike<=100000):
    print("tax of bike=",cost_of_bike/100*10)
else:
    print("tax of bike=",cost_of_bike/100*5)
    