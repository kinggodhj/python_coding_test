from itertools import combinations
from collections import deque
import copy
queue=deque([])
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
INF=int(1e9)

N, M=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
chicken=[]
for i in range(N):
    for j in range(N):
        if array[i][j]==2:
            chicken.append([i, j])
            array[i][j]=0

def BFS(city_array):
    check=[[INF]*N for _ in range(N)]
    while queue:
        x, y, d=queue.pop()
        check[x][y]=d
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                if city_array[x+dx[i]][y+dy[i]]==1 and d+1<check[x+dx[i]][y+dy[i]]:
                    check[x+dx[i]][y+dy[i]]=d+1
                    queue.appendleft([x+dx[i], y+dy[i], d+1])
                elif city_array[x+dx[i]][y+dy[i]]==0 and check[x+dx[i]][y+dy[i]]==INF:
                    check[x+dx[i]][y+dy[i]]=d+1
                    queue.appendleft([x+dx[i], y+dy[i], d+1])
    return check

def value(array, check_array):
    v=0
    for i in range(N):
        for j in range(N):
            if array[i][j]==1:
                v+=check_array[i][j]
    return v

com_l=[i for i in range(len(chicken))]
com=list(combinations(com_l, M))
result=INF
for case in com:
    city=copy.deepcopy(array)
    for idx in case:
        x, y=chicken[idx]
        city[x][y]=2
        queue.appendleft([x, y, 0])
    count=value(city, BFS(city))
    result=min(result, count)
print(result)