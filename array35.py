from numpy import *
r, c=[int(a) for a in input(" enter rows, cols:").split()]
str= input('enter the matrix element:\n')
x=reshape(matrix(str),(r,c))
print('the orginal matrix:')
print(x)
print('the transpose matrix:')
y=x.transpose()
print(y)
