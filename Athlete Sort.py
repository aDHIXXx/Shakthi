n,m = list(map(int, input().split(',')))

table = [ list(map(int, input().split(','))) for _ in range(n) ]
k = int(input())

table.sort(key = lambda x: x[k])
for i in table:
    print(*i)
