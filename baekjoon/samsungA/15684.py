import copy
import sys
from itertools import combinations

N, M, H=map(int, sys.stdin.readline().split(' '))
graph=[[0]*N for j in range(H)]
for _ in range(M):
    a, b=map(int, sys.stdin.readline().split(' '))
    graph[a-1][b-1]=1
    graph[a-1][b]=-1
    
def findRoute(g):
    for i in range(N):
        y=i
        for x in range(H):
            if g[x][y]==1:
                y+=1
            elif g[x][y]==-1:
                y-=1
        if y!=i:
            return False
    return True

def combination(array, n, count, i_idx, j_idx):
    if n==1:
        for i in range(i_idx, H):
            for j in range(N-1): 
                if i_idx==i and j<j_idx:
                    continue
                if array[i][j]!=0 or array[i][j+1]!=0:
                    continue
                array[i][j]=1
                array[i][j+1]=-1
                if findRoute(array):
                    print(count)
                    exit(0)
                else:
                    array[i][j]=0
                    array[i][j+1]=0
    else:
        for i in range(i_idx, H):
            for j in range(N-1): 
                if i_idx==i and j<j_idx:
                    continue
                if array[i][j]!=0 or array[i][j+1]!=0:
                    continue
                array[i][j]=1
                array[i][j+1]=-1
                combination(array, n-1, count+1, i, j)
                array[i][j]=0
                array[i][j+1]=0

if findRoute(graph):
    print("0")
else:
    for adding in range(1, 4):
        combination(graph, adding, 1, 0, 0)
    print("-1")

'''
comb=[]
for i in range(H):
    for j in range(N-1):
        if graph[i][j]==0:
            comb.append([i, j])

for adding in range(4):
    add_com=list(combinations(comb, adding))
    answer=-1
    for add in add_com:
        check=True
        this=copy.deepcopy(graph)
        for a in add:
            if this[a[0]][a[1]]==0:
                this[a[0]][a[1]]=1
                this[a[0]][a[1]+1]=-1
            else:
                check=False
                break
        if check==False:
            continue
        if findRoute(this):
            answer=(len(add))
            break
    if answer==-1:
        continue
    else:
        break
print(answer)
'''