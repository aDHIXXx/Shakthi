n=int(input('Enter the number of test cases: '))
l,p,b,j=[],0,0,0
for i in range(n):
    l.append(input())
print(l)
for i in range(n):
    x=str(l[i][l[i].index('.')+1: ])
    print(x)
    if x=='png':
        p=p+1
    elif x=='bmp':
        b=b+1
    elif x=='jpeg':
        j=j+1
print(p)
print(b)
print(j)

        
