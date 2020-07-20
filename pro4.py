#program to convert list to tuple

import math
n=int(input("enter numbers of element to enter in list"))
print("enter elements in list")

#creating empty list
lst=[]
for i in range(n):  
    i=int(input())          
    lst.append(i)

#converting list to tuple by explicitly assigning
y=tuple(lst)

#printing tuple 
print(y)
