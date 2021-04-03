from collections import defaultdict

N=int(input().rstrip())
people=list(map(int, input().rstrip().split(' ')))
people.insert(0, 0)
region=[i for i in range(1, N+1)]
graph=defaultdict(list)
answer=int(1e9)
def dif(lst1, lst2):
    d1=0
    d2=0
    for l in lst1:
        d1+=people[l]
    for l in lst2:
        d2+=people[l]
    return abs(d1-d2)

def DFS(root, lst, visit):
    for node in graph[root]:
        if visit[node]==0 and node in lst:
            visit[node]=1
            DFS(node, lst, visit)
    return visit

def check(lst, visit):
    for l in lst:
        if visit[l]==0:
            return False
    return True

def permute(numA, start, lst):
    global answer
    if len(lst)==numA:
        visit=[0]*(N+1)
        visit[lst[0]]=1
        res1=check(lst, DFS(lst[0], lst, visit))
        if res1==True:
            lst2=list(set(region)-set(lst))
            visit[lst2[0]]=1
            res2=check(lst2, DFS(lst2[0], lst2, visit)) 
            if res2==True:
                differ=dif(lst, lst2)
                if differ<answer:
                    answer=differ
    else:
        for i in range(start, N+1):
            permute(numA, i+1, lst+[i])

for i in range(N):
    tmp=list(map(int, input().rstrip().split(' ')))
    for t in tmp[1:]:
        graph[i+1].append(t)

for numA in range(1, N//2+1):
    permute(numA, 1, [])

if answer==int(1e9):
    print(-1)
else:
    print(answer)