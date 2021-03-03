import sys
from itertools import combinations
import copy
from collections import deque

N, M=map(int, sys.stdin.readline().split(' '))
#lab=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

def bfs(start, N, M, lab_c,check, region):
    queue=deque([])
    queue.append(start)
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    check[start[0]][start[1]]=1
    while queue:
        now_x, now_y=queue.popleft()
        for d in range(4):
            if 0<=now_x+dx[d]<N and 0<=now_y+dy[d]<M:
                if check[now_x+dx[d]][now_y+dy[d]]==0 and lab_c[now_x+dx[d]][now_y+dy[d]]==0:
                    queue.append([now_x+dx[d], now_y+dy[d]])
                    check[now_x+dx[d]][now_y+dy[d]]=1
                    if region<0:
                        break
                    else:
                        region-=1

    return check, region

zero=[]
vir=[]
region=0
lab=[]
for row in range(N):
    lab.append(list(map(int, sys.stdin.readline().split(' '))))
    for col in range(M):
        if lab[row][col]==0:
            zero.append([row, col])
            region+=1
        elif lab[row][col]==2:
            vir.append([row, col])

zero_com=list(combinations(zero, 3))

result=[]
for com in zero_com:
    lab_c=copy.deepcopy(lab)
    for c in com:
        lab_c[c[0]][c[1]]=1
    tmp=region-3
    check=[[0]*M for _ in range(N)]
    for v in vir:
        if check[v[0]][v[1]]==0:
            check, tmp=bfs(v, N, M, lab_c, check, tmp)
    result.append(tmp)

print(max(result))    