l,S1,final=[],[],[]
S=input('Enter the numbers: ')
S1=S.split()
for i in S1:
    l.append(int(i))
final=str("['"+str(l)+"']")
print(final)
