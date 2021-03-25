from collections import deque
N, M, gas=map(int, input().rstrip().split(' '))
road=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
car_x, car_y=map(lambda x: int(x)-1, input().rstrip().split(' '))
rider=[]
target=[]
for _ in range(M):
    rx, ry, tx, ty=map(lambda x: int(x)-1, input().rstrip().split(' '))
    rider.append([rx, ry])
    target.append([tx, ty])

move=[0]*M

dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]

def BFS_rider(sx, sy):
    next_r=[]
    queue=deque([])
    queue.appendleft([sx, sy, 0])
    visit=[[0]*N for _ in range(N)]
    visit[sx][sy]=1
    min_time=int(1e9)
    while queue:
        x, y, t=queue.pop()
        if t>=min_time:
            continue
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<N and 0<=ny<N:
                if road[nx][ny]==0 and visit[nx][ny]==0:
                    l=len(next_r)
                    for i in range(M):
                        if move[i]==1:
                            continue
                        if rider[i]==[nx, ny] and t+1<=min_time:
                            visit[nx][ny]=1
                            next_r.append([t+1, nx, ny, i])
                            min_time=t+1
                    if len(next_r)==l:
                        visit[nx][ny]=1
                        queue.appendleft([nx, ny, t+1])
    next_r.sort(key=lambda x:[int(x[0]), int(x[1]), int(x[2])])
    return next_r

def BFS_destination(sx, sy, idx):
    queue=deque([])
    queue.appendleft([sx, sy, 0])
    visit=[[0]*N for _ in range(N)]
    visit[sx][sy]=1
    while queue:
        x, y, t=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if road[nx][ny]==0 and visit[nx][ny]==0:
                    if [nx, ny]==target[idx]:
                        return t+1, nx, ny
                    visit[nx][ny]=1
                    queue.appendleft([nx, ny, t+1])
    return -1, -1, -1

def next_rider(car_x, car_y):
    global gas
    for i in range(M):
        if move[i]==1:
            continue
        if rider[i]==[car_x, car_y]:
            d=0
            cx, cy=car_x, car_y
            move[i]=1
            gas-=d
            if gas<0:
                print('-1')
                exit(0)
            d, tx, ty=BFS_destination(cx, cy, i)
            if d==-1:
                print('-1')
                exit(0)
            gas-=d
            if gas<0:
                print('-1')
                exit(0)
            gas+=d*2
            return tx, ty
    next_l=BFS_rider(car_x, car_y)
    if len(next_l)>0:
        d, cx, cy, i=next_l[0]
        move[i]=1
        gas-=d
        if gas<0:
            print('-1')
            exit(0)
        d, tx, ty=BFS_destination(cx, cy, i)
        gas-=d
        if gas<0:
            print('-1')
            exit(0)
        gas+=d*2
        return tx, ty
    else:
        print('-1')
        exit(0)

while(move!=[1]*M):
    car_x, car_y=next_rider(car_x, car_y)
print(gas)