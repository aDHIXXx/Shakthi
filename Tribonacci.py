n=int(input('Your desired number of divisors: '))
e1,e2,e3,flag=0,0,1,0
def divisors(a):
    flag=0
    for i in range(1,a):
        if a%i==0:
            flag=flag+1
    return flag
for i in range(1,10000):
   e4= e1+e2+e3
   if(divisors(e4)==n):
           print(e4)
           break
   e1=e2
   e2=e3
   e3=e4
   e4=0
   flag=0

   
   
