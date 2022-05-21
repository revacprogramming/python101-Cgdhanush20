fname=input("Enter the file name: ")
fh=open(fname)
counts=dict()
for line in fh:
    if line.startswith("From"):
        words=line.split()
        words=words[1]
        if words not in counts:
                counts[words] = 1
        else:
                counts[words] += 1
        counts[words]=int(counts[words])
max=0
value=""
for i in counts:
    if counts[i]>max:
        max=counts[i]
        value=i
print(value,max)              