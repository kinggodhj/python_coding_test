from collections import deque
import copy
N, M=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
min_time=int(1e9)
queue=deque([])
def spread(time, start_l):
    queue.extendleft(start_l)
    ans=0
    while queue:
        x,y,t=queue.pop()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<N and 0<=ny<N:
                if t+1<time[nx][ny]:
                    if array[nx][ny]!=1:
                        time[nx][ny]=t+1
                        queue.appendleft([nx, ny, t+1])
                        if array[nx][ny]==0:
                            ans=max(ans, t+1)
                    else:
                        time[nx][ny]=-1
    return ans, time

time=[[int(1e9)]*N for _ in range(N)]

def check(this_time):
    for i in range(N):
        for j in range(N):
            if this_time[i][j]==int(1e9) and array[i][j]==0:
                return False
    return True

def select(M, x, y, time, result):
    global min_time
    if len(result)==M:
        t, time=spread(copy.deepcopy(time), result)
        if check(time)==True:
            min_time=min(min_time, t)
            if min_time==0:
                print(min_time)
                exit(0)
    else:
        for i in range(x, N):
            for j in range(N):
                if i==x and j<y:
                    continue
                if array[i][j]==2:
                    time[i][j]=0
                    if j==N-1:
                        select(M, i+1, 0, time, result+[[i, j, 0]])
                    else:
                        select(M, i, j+1, time, result+[[i, j, 0]])
                    time[i][j]=int(1e9)
                    
select(M, 0, 0, time, [])
if min_time==int(1e9):
    print('-1')
else:
    print(min_time)