from collections import deque
N=int(input().rstrip())
K=int(input().rstrip())
array=[[0]*N for _ in range(N)]
for _ in range(K):
    x,y=map(int, input().rstrip().split(' '))
    array[x-1][y-1]=1
L=int(input().rstrip())
times=[]
direction=[]
queue=deque([])

dx=[0, -1, 0, 1, 0]
dy=[0, 0, 1, 0, -1]

for _ in range(L):
    t, d=input().rstrip().split(' ')
    times.append(int(t))
    direction.append(d)

def rotate(d, C):
    if C=='D':
        d=d%4+1
    else:
        d-=1
        if d==0:
            d=4
    return d

time=1
dir=2
x, y=0, 0
c=0
array[x][y]=2
l=1
queue.appendleft([x, y])
while(1):
    nx=x+dx[dir]
    ny=y+dy[dir]
    if nx>=N or nx<0 or ny>=N or ny<0:
        break
    if array[nx][ny]==2:
        break
    if array[nx][ny]==1:
        l+=1
        array[nx][ny]=2
        queue.appendleft([nx, ny])
    else:
        queue.appendleft([nx, ny])
        array[nx][ny]=2
        tail_x, tail_y=queue.pop()
        array[tail_x][tail_y]=0

    for i in range(c, len(times)):
        if times[i]==time:
            dir=rotate(dir, direction[i])
            c+=1
        elif times[i]>time:
            break
    x=nx
    y=ny
    time+=1
print(time)