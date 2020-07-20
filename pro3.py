#program to calculate sum of elements of list

import math
n=int(input("enter numbers of element to enter in list"))
print("enter elements in list")

#creating empty list
lst=[]

#passing elements to list
for i in range(n):        #range function iterate and return number from 0 to n-1
    i=int(input())        #explicitly taking input as integers
    lst.append(i)         #passing input to list

print("sum of all elements")

#summing elemnts of list
add=0
for i in lst:
    add += i

#print sum of elements of list
print(add)
