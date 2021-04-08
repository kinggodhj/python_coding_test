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

def eating(sx, sy, time, ate, size, arr, visit):
    queue=deque([])
    queue.appendleft([sx, sy, time])
    visit[sx][sy]=1
    while queue:
        x, y, t=queue.pop()
        for i in range(4):
            dx, dy=df[i]
            if 0<=x+dx<N and 0<=y+dy<N:
                if 0<arr[x+dx][y+dy]<size and visit[x+dx][y+dy]==0:
                    arr[sx][sy]=0
                    arr[x+dx][y+dy]=9
                    ate+=1
                    return [arr, x+dx, y+dy, ate, t+1]
                elif arr[x+dx][y+dy]==0 or arr[x+dx][y+dy]==size:
                    if visit[x+dx][y+dy]==0:
                        visit[x+dx][y+dy]=1
                        queue.appendleft([x+dx, y+dy, t+1])
    return None

time=0
size=2
ate=0
while(1):
    visit=[[0]*N for _ in range(N)]
    visit[shark_x][shark_y]=1
    if time==10:
        breakpoint
    result=eating(shark_x, shark_y, time, ate, size, array, visit)
    if type(result)==list:
        array, shark_x, shark_y, ate, time=result
        if ate==size:
            size+=1
            ate=0 
    else:
        print(time)
        exit(0)