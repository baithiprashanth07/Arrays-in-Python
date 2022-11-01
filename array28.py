from numpy import *
a=arange(1,6)
b=a
print('Original array:',a)
print('Alias array:',b)
b[0]=99
print('after modification :')
print('Original array:',a)
print('Alias arraay:',b)
