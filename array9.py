from array import *
str=input('enter marks:').split(' ')
marks=[int(num) for num in str]
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total marks:',sum)
n=len(marks)
percent=sum/n
print('percentage:',percent)
