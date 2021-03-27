from collections import deque
import copy
N, Q=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(2**N)]
L=list(map(int, input().rstrip().split(' ')))                        
queue=deque([])
count=0

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def rotate(l, arr):
    new=[[0]*2**N for _ in range(2**N)]    
    m=2**l
    for x in range(2**N):
        for y in range(2**N):
            xm=0
            ym=0
            nx=x
            ny=y
            if x>=m:
                xm=x//m
                nx=x%m
            if y>=m:
                ym=y//m
                ny=y%m
            new[xm*m+ny][ym*m+m-1-nx]=arr[x][y]
    return new

def removeIce(arr):
    new=copy.deepcopy(arr)
    for x in range(0, 2**N):
        for y in range(0, 2**N):
            check=0
            for k in range(4):
                if 0<=x+dx[k]<2**N and 0<=y+dy[k]<2**N:
                    if arr[x+dx[k]][y+dy[k]]>0:
                        check+=1
            if check<3 and arr[x][y]>0:
                new[x][y]-=1
    return new

def BFS(sx,sy,arr,visit):
    global count
    c=1
    queue.appendleft([sx,sy])
    visit[sx][sy]=1
    while queue:
        x, y=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<2**N and 0<=ny<2**N:
                if visit[nx][ny]==0 and arr[nx][ny]>0:
                    queue.appendleft([nx, ny])
                    visit[nx][ny]=1
                    c+=1
    if count<c:
        count=c
    return visit

for l in L:
    array=rotate(l, array)
    array=removeIce(array)

visit=[[0]*(2**N) for _ in range(2**N)]
for i in range(0, 2**N):
    for j in range(0, 2**N):
        if array[i][j]>0 and visit[i][j]==0:
            visit=BFS(i,j,array,visit)
ice=0
for row in array:
   ice+=sum(row)
print(ice)
print(count) 