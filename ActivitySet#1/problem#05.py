def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        fee=40*r+(h-40)*r*1.5
        return fee
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))
p = computepay(hrs, rte)
print("Pay", p)