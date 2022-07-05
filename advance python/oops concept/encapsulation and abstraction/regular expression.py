#regular expression
#package in python language
# using pattern matching(comparing string)
#validation(should follow the format is called validation)
#eg: mobile number:(10 digit must enetr)
count=0
import re
s="jitheshabababbaaaabab"
#finditer(argument 1,argument2)
#argument 1=  find which pattern iter
#argument2=   that string name
matcher=re.finditer('ab',s)
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())#for matching in which indexnumber
print(count)


