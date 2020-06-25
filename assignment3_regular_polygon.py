import math
s=float(input("enter the number of sides:"))
l=float(input("enter the length:"))
a=s*(l**2)/(4*math.tan(math.pi/s))
print(a)
