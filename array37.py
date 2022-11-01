from array import *
x=array('i',[])
print('how many elements?', end='')
n=int(input())
for i in range(n):
    print('enter element :',end='')
    x.append(int(input()))
print('original array',x)
print('enter element to search :',end='')
s=int(input())
try:
    pos=x.index(s)
    print('found at position =',pos+1)
except ValueError:
    print('not founnd in the array')
