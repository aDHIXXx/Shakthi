new_string=input('Enter the sentence: ')
withoutspace_string,even_string,odd_string,reversed_string='','','',''
withoutspace_string=new_string.replace(' ','')
for i in range(len(withoutspace_string)):
    if (i+1)%2==0:
        even_string=even_string+withoutspace_string[i]
    else:
        odd_string=odd_string+withoutspace_string[i]
for i in range(-1,-((len(even_string))+1),-1):
    reversed_string=reversed_string+even_string[i]
print(odd_string,end='')
print(reversed_string)

