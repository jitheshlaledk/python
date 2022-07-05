
import re
st="hlhldkfjhghllhhkhlhljhjhlhkehlhlh"
count=0

matching=re.finditer('hl',st)
for i in matching:
    count+=1
    print(i.group())
    print(i.start())
print(count)

