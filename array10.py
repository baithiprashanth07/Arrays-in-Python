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
flag=False
for i in range(len(x)):
    if s == x[i]:
        print('found at position=',i+1)
        flag=True
if flag==False:
    print('not founnd in the array')
