hrs = float(input("Enter hours "))

if hrs<= 40:
    fee=hrs*1.5
elif hrs>40:
    hrs2=hrs-40
    fee=40*10.5+hrs2*10.5
else:
    fee=0
print(fee) 
          