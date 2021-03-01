import sys
from itertools import combinations
from itertools import permutations

N=int(sys.stdin.readline())
arr=[list(map(int, sys.stdin.readline().split(' ')))for _ in range(N)]

l=[i for i in range(N)]
comb=combinations(l, N//2)
 
result=[]
for com in comb:
    start=list(com)
    link=list(set(l)-set(com))
    per_1=permutations(start, 2)
    per_2=permutations(link, 2)
    s_sum=0
    l_sum=0
    for p in per_1:
        s_sum+=arr[p[0]][p[1]]
    for p in per_2:
        l_sum+=arr[p[0]][p[1]]
    result.append(abs(s_sum-l_sum))

print(min(result))