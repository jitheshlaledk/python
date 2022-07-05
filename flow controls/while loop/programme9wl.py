#lower limit&uper limit
#sum of even and odd numbers
# lnum=int(input("enter l num"))
# unum=int(input("enter u num)"))
# even_sum=0
# odd_sum=0
# while(lnum<=unum):
#     if(lnum%2==0):
#         even_sum+=lnum
#     else:
#         odd_sum+=lnum
#     lnum+=1
# print("sum of even number=",even_sum)
# print("sum of odd number=",odd_sum)
























#print sum of odd number and even numbers from lower limit and upper limit


lower_limit=int(input("enter lower limit"))
upper_limit=int(input("enter upper limit"))
evensum=0
oddsum=0

while(lower_limit<=upper_limit):
    if(lower_limit%2==0):
        evensum+=lower_limit
    else:
        oddsum+=lower_limit
    lower_limit+=1
print(evensum,"is even sum")
print(oddsum,"is odd sum")

