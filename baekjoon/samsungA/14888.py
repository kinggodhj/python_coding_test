from itertools import permutations
N=int(input().rstrip())
numbers=list(map(str, input().rstrip().split(' ')))
op=list(map(int, input().rstrip().split(' ')))
#+, -, x, /
operations=[]
for i in range(4):
    if op[i]==0:
        continue
    if i==0:
        operations.extend(['+']*op[i])
    elif i==1:
        operations.extend(['-']*op[i])
    elif i==2:
        operations.extend(['*']*op[i])
    elif i==3:
        operations.extend(['/']*op[i])
num_op=len(operations)

case=list(set(list(permutations(operations,N-1))))
max_n=-1*int(1e9)
min_n=int(1e9)
for i in range(len(case)):
    result=numbers[0]
    for n in range(1, N):
        result+=case[i][n-1]
        result+=numbers[n]
        result=str(int(eval(result)))
    if int(result)>max_n:
        max_n=int(result)
    if int(result)<min_n:
        min_n=int(result)
print(max_n)
print(min_n)