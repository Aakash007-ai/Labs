#program to calculate roots of equation

#importing math library for sqrt module
import math

#taking coefficient of equation as input
print("Quadrtic equation ax**2 +bx +c=0")
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))

#calculating determinant of equation
d=b**2 - 4*a*c

#condition based roots
if d<0:
    print("Imaginary roots")

elif d==0:
    printf("Real and equal roots i.e %f"%(-b/2*a))    #string formatting

else :
    x_1=(-b+math.sqrt(d))/(2*a)
    x_2=(-b-math.sqrt(d))/(2*a)
    print(x_1,x_2)
