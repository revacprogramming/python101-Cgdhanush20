import re
fname=input("Enter the file name:")
fh=open(fname)
sum = 0
l=list()
for line in fh:
    line=line.strip()
    x=re.findall('[0-9]+',line)
    l+=x
for i in l:
    sum+=int(i)
print(sum)