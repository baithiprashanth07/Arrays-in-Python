from numpy import *
a= arange(10,16)
print(a)
a=a[1:6:2]
print(a)
i=0
while(i<len(a)):
    print(a[i])
    i+=1
