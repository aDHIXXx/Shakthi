s=input()
q=input()
s1=s[ :s.index('@')]
s2=s[s.index('@')+1: ]
q1=q[ :q.index('@')]
q2=q[q.index('@')+1:]
def local(A):
    for i in  range(len(A)):
        x=str(A[i])
        if (ord(x)>64 and ord(x)<91) or (ord(x)>96 and ord(x)<123) or (ord(x)>47 and ord(x)<57) or x=='!' or x=='#' or x=='$' or x=='%' or x=='^' or x=='&' or x=='*' or x=='{' or x=='}' or x=='_' or x=='+' or x=='-' or x=='=' or x=='/' or x=="'" or ord(x)==126:
            x1=0
        else:
            x=1
    if A[0]=='.' or A[len(A)-1]=='.':
        x2=1
    else:
        x2=0
    if len(A)>64:
       x3=1
    else:
       x3=0
    if x1+x2+x3==0:
        return 0
    else:
        return 1
def domain(A):
    x1,x2,x3,x4,x5=0,0,0,0,0
    A1=A[ :A.index('.')]
    A2=A[A.index('.')+1: ]
    for i in range(len(A1)):
        x=str(A1[i])
        if (ord(x)>64 and ord(x)<91) or (ord(x)>96 and ord(x)<123) or (ord(x)>47 and ord(x)<57) or x=='-':
            x1=x1+0
        else:
            x1=x1+1
            P=x1
    for i in range(1,len(A1)-1):
        if A1[i]=='-':
            x2=x2+1
        else:
            x2=x2+0
    if A1.isdigit=='True':
        x3=x3+1
    else:
        x3=x3+0
    if len(A2)>3:
        x4=x4+1
    else:
        x4=x4+0
    for i in range(len(A2)):
        a=A2[i]
        if a=='!' or a=='#' or a=='$' or a=='%' or a=='^' or a=='&' or a=='*' or a=='{' or a=='}' or a=='_' or a=='+' or a=='-' or a=='=' or a=='/' or a=="'" or ord(a)==126:
           x5=x5+1
        else:
            x5=x5+0
    if x1+x2+x3+x4+x5==0:
        return 0
    else:
        return 1
if (local(s1))+(domain(s2))==0:
    print(s)
    
if (local(q1))+(domain(q2))==0:
    print(q)


    

        
