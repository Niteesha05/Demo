import math
d=float(input("enter the value of diameter:"))
c=float(input("enter the value of chord:"))
r=(d/2)
s=math.sqrt(d**2+c**2)
h=(s/2-r)
i=(2/3*c*h)
j=(h**3/2*c)
area=i+j
print(area)
