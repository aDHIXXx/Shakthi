n=int(input())
table , table1,final= [],[] ,[]
for _ in range(n):
    name = input()
    grade = float(input())
    table.append([name, grade])

table.sort(key = lambda x: x[1])

for x in range(n):
    table1.append(table[x][1])
    
if (table1[1]!=table[0][1]):
    lowest=table1[1]
else:
    for i in range(2,n):
        if table1[i]!=table1[0]:
            lowest = table1[i]
            break

for i in range(n):
    if table[i][1]==lowest:
        final.append(table[i][0])
print(final)
    


