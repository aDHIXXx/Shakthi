n=input('Enter the string: ')
l=len(n)
lower,upper,even,odd,finall,final=[],[],[],[],[],[]
for i in range(l):
    if 123>ord(n[i]) and ord(n[i])>96:
        lower=lower+list(n[i])
for i in range(l):
    if 91>ord(n[i]) and ord(n[i])>64:
       upper=upper+list(n[i])
for i in range(l):
    if 57>ord(n[i]) and ord(n[i])>47:
        if ord(n[i])== 48:
            even= even+n[i]
        elif int(n[i])%2==0 :
           even= even+list(n[i])
        else:
            odd=odd+list(n[i])
final=sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)
finall=''.join(map(str, final))
print(finall)
    



