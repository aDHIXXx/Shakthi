String1=input('Enter the first string; ')
String2=input('Enter the second string; ')
sum1,sum2=0,0
for i in range(len(String1)):
    sum1=sum1+ord(String1[i])
for i in range(len(String2)):
    sum2=sum2+ord(String2[i])
if sum1==sum2:
    print('They are equal')
    print('Yes')
else:
    print('They are not equal')
    print('No')
