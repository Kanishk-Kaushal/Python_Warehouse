hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter rate:")
r=float(rt)
if h<=40:
    pay=h*r
else:
    dh=h-40
    pay=40*r+(dh*r*1.5)
print(pay) 
