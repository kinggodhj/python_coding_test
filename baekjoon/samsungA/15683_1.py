from itertools import product
import copy
from collections import deque

#cctv={1:[(1),(2),(3),(4)], 2:[(1,2),(3,4)], 3:[(1,3),(3,2),(2,4),(4,1)], 4:[(1,3,4),(3,1,2),(3,4,2),(1,2,4)], 5:[(1,2,3,4)]}
cctv={1:[[1],[2],[3],[4]], 2:[[1,2],[3,4]], 3:[[1,3],[3,2],[2,4],[4,1]], 4:[[1,3,4],[3,1,2],[3,4,2],[1,2,4]], 5:[[1,2,3,4]]}
df={1:[-1,0], 2:[1,0], 3:[0,1], 4:[0,-1]}

N, M=map(int, input().rstrip().split(' '))
array=[]
camera=[]
camera_idx=[]
for i in range(N):
    tmp=list(map(int, input().rstrip().split(' ')))
    array.append(tmp)
    for j in range(M):
        if 0<tmp[j]<6:
            camera.append(cctv[tmp[j]])
            camera_idx.append([i, j])

def BFS(case, idx, arr):
    sx, sy=idx
    queue=deque([])
    visit=[[0]*M for _ in range(N)]
    visit[sx][sy]=1
    for d in case:
        queue.appendleft([sx, sy, d])
    while queue:
        x,y,d=queue.pop()
        dx, dy=df[d]
        if 0<=x+dx<N and 0<=y+dy<M:
            if visit[x+dx][y+dy]==0:
                visit[x+dx][y+dy]=1
                if arr[x+dx][y+dy]==0:
                    arr[x+dx][y+dy]=-1
                    queue.appendleft([x+dx, y+dy, d])
                elif arr[x+dx][y+dy]==-1 or 0<arr[x+dx][y+dy]<6:
                    queue.appendleft([x+dx, y+dy, d])
    return arr

case=list(product(*camera))
answer=int(1e9)
for c in case:
    arr=copy.deepcopy(array)
    for num in range(len(c)):
        arr=BFS(c[num], camera_idx[num], arr)
    count=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                count+=1
    if count<answer:
        answer=count
print(answer)