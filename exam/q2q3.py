#question 3

for num in range(0,101):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)