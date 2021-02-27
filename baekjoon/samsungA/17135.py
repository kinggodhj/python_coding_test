import copy
import sys
from collections import deque

N, M, D=map(int, sys.stdin.readline().rstrip().split(' '))
castle=[list(map(int, sys.stdin.readline().rstrip().split(' '))) for i in range(N)]
select=[0 for _ in range(M)]
archer=[]
dx=[]
dy=[]
def addComb():
    combination=[]
    for i in range(M):
        if select[i]==1:
            combination.append(i)
    return combination

def comb_dfs(idx, cnt):
    if cnt==3:
        archer.append(addComb())
    for i in range(idx, M):
        if select[i]==0:
            select[i]=1  
            comb_dfs(i, cnt+1)
            select[i]=0

comb_dfs(0, 0)

def trav(D):
    for distance in range(1, D+1):
        tmp_x=[]
        tmp_y=[]
        for xx in range(1, distance+1):
            dx.append(-1*xx)
            dy.append(-1*distance+xx)
            if -1*distance+xx !=0:
                tmp_x.insert(0, -1*xx)
                tmp_y.insert(0, -1*(-1*distance+xx))
        dx.extend(tmp_x)
        dy.extend(tmp_y)
            

def findEnemy(arc, castle, N, M, D):
    queue=deque([])
    queue.append([N, arc[0]])
    queue.append([N, arc[1]])
    queue.append([N, arc[2]])
    count=0
    while queue:
        x1, y1=queue.popleft()
        x2, y2=queue.popleft()
        x3, y3=queue.popleft()
        coord=[]
        for i in range(len(dx)):
            if 0<=x1+dx[i]<N and 0<=y1+dy[i]<M:
                if castle[x1+dx[i]][y1+dy[i]]==1:
                    coord.append((x1+dx[i], y1+dy[i]))
                    break
        for i in range(len(dx)):
            if 0<=x2+dx[i]<N and 0<=y2+dy[i]<M:
                if castle[x2+dx[i]][y2+dy[i]]==1:
                    coord.append((x2+dx[i], y2+dy[i]))
                    break
        for i in range(len(dx)):
            if 0<=x3+dx[i]<N and 0<=y3+dy[i]<M:
                if castle[x3+dx[i]][y3+dy[i]]==1:
                    coord.append((x3+dx[i], y3+dy[i]))
                    break
        count+=len(set(coord))
        for idx, cor in enumerate(coord):
            castle[cor[0]][cor[1]]=0

        if x1-1>0:
            queue.append([x1-1, y1])
            queue.append([x2-1, y2])
            queue.append([x3-1, y3])

    return count

trav(D)

w_count=[]
for arc in enumerate(archer):
    w_count.append(findEnemy(arc[1], copy.deepcopy(castle), N, M, D))
print(max(w_count))