import math
entry=input('Enter the number of integers present and the integers seperated by commas: ')

sum=0
line,line1,line2,line3=[],[],[],[]
list=entry.split(',')
n=int(list[0])
line2=list[1]
line3=line2.split()
for i in line3:
       line.append(int(i))
def size(s):
    flag=0
    while s>0:
          b=s%10
          flag=flag+1
          s=s//10
    return flag
for i in range(n):
    if line[i]>0:
        x=line[i]
        l= size(line[i])
        while x>0:
            a=x%10
            sum=sum+(a*(math.pow(10,l)))
            x=x//10
            l=l-1
        if sum==line[i]:
            
            line1.append('True')
        else:
            
            line1.append('False')
    else:
        
        line1.append('False')
print(all(line1)) 
            


