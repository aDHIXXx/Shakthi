from itertools import combinations
initial_list,sum_list,sorted_list=[],[],[]
initial_list = [int(integers) for integers in input("Enter the list items : ").split(',')]
comb = combinations(initial_list,4)  
for i in list(comb):
    s= sum(i)
    sum_list.append(s)
sorted_list=sorted(sum_list)
print(sorted_list[0],' ',sorted_list[len(sorted_list)-1])

