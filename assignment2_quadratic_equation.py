import math
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
d=(b**2)-(4*a*c)
if d>0:
    x1=(((-b)+math.sqrt(d))/(2*a))
    x2=(((-b)-math.sqrt(d))/(2*a))
    print("roots are:",x1,x2)
elif d==0:
    x=float((-b)/(2*a))
    print("roots are:",x)
else:
    print("no roots")
