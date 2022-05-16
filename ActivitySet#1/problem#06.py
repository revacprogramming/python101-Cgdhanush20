large=0
small=1111111111111111110
a= None
while True:
    a=input("Enter the number: ")
    if a == 'Done' or a == 'done':
        break
    try:
        if int(a)>0 or int(a) <=0:
            if int(a)>large:
                 large=int(a)
            if int(a)<small:
                 small=int(a)
    except:
        pass    
print("Maximum =",large,"\nMinimum=",small)