from collections import deque
N, L, R=map(int, input().split(' '))
contries=[list(map(int, input().split(' '))) for _ in range(N)]

def findCont(start, check):
    queue=deque([])
    queue.appendleft([start[0],start[1]])
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    visited=[]
    visited.append([start[0],start[1]])
    check[start[0]][start[1]]=1
    v=contries[start[0]][start[1]]
    num=1
    while queue:
        x, y=queue.pop()
        for d in range(len(dx)):
            if 0<=x+dx[d]<N and 0<=y+dy[d]<N:
                if check[x+dx[d]][y+dy[d]]==0:
                    if L<=abs(contries[x+dx[d]][y+dy[d]]-contries[x][y])<=R:
                        queue.appendleft([x+dx[d], y+dy[d]])
                        visited.append([x+dx[d], y+dy[d]])
                        check[x+dx[d]][y+dy[d]]=1
                        v+=contries[x+dx[d]][y+dy[d]]
                        num+=1
    return visited, v//num, check

count=0
while(1):
    c=False
    check=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j]==0:
                visited, value, check=findCont([i, j], check)
                if len(visited)>1: 
                    c=True
                    for id in visited:
                        contries[id[0]][id[1]]=value
                
    if c==True:
        count+=1
    else:
        break
print(count)