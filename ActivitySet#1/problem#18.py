fname=input('Enter the file name: ')
fh=open(fname)
count=0
for line in fh:
    if line.startswith("From"):
        l=line
        l.split()
        print(l[1])
        count =count+1
print(count,'number of times the line started with From')