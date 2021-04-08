from collections import deque

N=int(input().rstrip())
array=[]
df=[[-1, 0], [0, -1], [0, 1], [1,0]]

for i in range(N):
    tmp=list(map(int, input().rstrip().split(' ')))
    array.append(tmp)
    for j in range(N):
        if tmp[j]==9:
            shark_x=i
            shark_y=j

def eating(sx, sy, time, size, arr, visit):
    queue=deque([])
    queue.appendleft([sx, sy, time])
    visit[sx][sy]=1
    answer=[]
    cand=None
    while queue:
        x, y, t=queue.pop()
        for i in range(4):
            dx, dy=df[i]
            if 0<=x+dx<N and 0<=y+dy<N:
                if 0<arr[x+dx][y+dy]<size and visit[x+dx][y+dy]==0:
                    if cand==None:
                        cand=t+1
                        visit[x+dx][y+dy]=1
                        answer.append([x+dx, y+dy, t+1])
                    elif t+1==cand:
                        visit[x+dx][y+dy]=1
                        answer.append([x+dx, y+dy, t+1])
                elif arr[x+dx][y+dy]==0 or arr[x+dx][y+dy]==size:
                    if visit[x+dx][y+dy]==0:
                        if cand==None:
                            visit[x+dx][y+dy]=1
                            queue.appendleft([x+dx, y+dy, t+1])
                        elif t+1<cand:
                            visit[x+dx][y+dy]=1
                            queue.appendleft([x+dx, y+dy, t+1])
    return answer

time=0
size=2
ate=0
while(1):
    visit=[[0]*N for _ in range(N)]
    visit[shark_x][shark_y]=1
    result=eating(shark_x, shark_y, time, size, array, visit)
    if len(result)>0:
        result.sort()
        x, y, time=result[0]
        array[shark_x][shark_y]=0
        array[x][y]=9
        shark_x=x
        shark_y=y
        ate+=1
        if ate==size:
            size+=1
            ate=0 
    else:
        print(time)
        exit(0)