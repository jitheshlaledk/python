#set some basic rules inside regular expression

import re
count=0
rule='[^0-9]'#^except that word
matcher=re.finditer(rule,'jithesh Lal is a Builder')
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)


#hacker rank

