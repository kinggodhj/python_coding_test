from collections import deque

N, K=map(int, input().split(' '))
virus=[list(map(int, input().split(' '))) for _ in range(N)]
S, X, Y=map(int, input().split(' '))

vir_idx=[]
for row in range(N):
    for col in range(N):
        if virus[row][col]!=0:
            vir_idx.append([row, col, 0, virus[row][col]])

def bfs(queue, target_x, target_y):
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    while queue:
        x, y, time, _=queue.popleft()
        if time==S:
            if x==target_x and y==target_y:
                return virus[x][y]
            
        elif time<S:
            for d in range(4):
                if 0<=x+dx[d]<N and 0<=y+dy[d]<N and virus[x+dx[d]][y+dy[d]]==0:
                    queue.append([x+dx[d], y+dy[d], time+1, virus[x][y]])
                    virus[x+dx[d]][y+dy[d]]=virus[x][y]
    return virus[target_x][target_y]

vir_idx.sort(key=lambda x: (x[3], x[2]))

queue=deque([])
queue.extend(vir_idx)

print(bfs(queue, X-1, Y-1))