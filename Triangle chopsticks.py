user_input=input("Enter the lengths and number chosen: ");
a,b,r=user_input.split()
n=int(input("Enter the number of chopsticks in the jar: "));

flag=0
print('Enter the lengths in the jar: ')
lst=[]
for i in range(0,n):
    ele= int(input())
    lst.append(ele)
for i in range(0,n):
   if(((int(a)+int(b))<=lst[i])or((int(b)+lst[i])<=int(a))or((lst[i]+int(a))<=int(b))):
          flag=flag+1
print("Total no.of triangels possible: ", flag)    
if flag>int(r):
   print('Natsu won')
else:
   print('Grey won')

   
