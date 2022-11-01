from numpy import *
a=arange(1,6)
b=a.view()
print('Original array:',a)
print('new array:',b)
b[0]=99
print('after modification :')
print('Original array:',a)
print('new array :',b)
