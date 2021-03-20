from collections import deque

N, K=map(int, input().rstrip().split(' '))
chess_map=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
chess=[[deque([]) for _ in range(N)] for _ in range(N)] 
coord=[]
dir={1:[0, 1], 2:[0, -1], 3:[-1, 0], 4:[1, 0]}
queue=deque([])
time=1

for i in range(K):
    x,y,d=map(int, input().rstrip().split(' '))
    chess[x-1][y-1].append([i, d])
    coord.append([x-1, y-1])

def end():
    for i in range(N):
        for j in range(N):
            if not chess[i][j]:
                continue
            if len(chess[i][j])>=4:
                return False
    return True

def move(number):
    global time
    x,y=coord[number]
    l=len(chess[x][y])-1
    idx=0
    for c in range(l, -1 , -1):
        if chess[x][y][c][0]==number:
            i, d=chess[x][y][c]
            idx=c
            break
    t=0
    while(1):
        dx, dy=dir[d]
        if 0<=x+dx<N and 0<=y+dy<N:
            if chess_map[x+dx][y+dy]==0:
                for _ in range(l, idx, -1):
                    n_i, n_d=chess[x][y].pop()
                    coord[n_i]=[x+dx, y+dy] 
                    queue.appendleft([n_i , n_d])
                chess[x][y].pop()
                coord[i]=[x+dx, y+dy]
                queue.appendleft([i ,d])
                chess[x+dx][y+dy].extend(list(queue))
                if len(chess[x+dx][y+dy])>=4:
                    print(time)
                    exit(0)
                queue.clear()
                break
            elif chess_map[x+dx][y+dy]==1:
                for _ in range(l, idx, -1):
                    n_i, n_d=chess[x][y].pop()
                    coord[n_i]=[x+dx, y+dy] 
                    queue.append([n_i , n_d])
                chess[x][y].pop()
                coord[i]=[x+dx, y+dy]
                queue.append([i ,d])
                chess[x+dx][y+dy].extend(list(queue))
                if len(chess[x+dx][y+dy])>=4:
                    print(time)
                    exit(0)
                queue.clear()
                break
        if t==0:
            if d==1:
                t+=1
                d=2
            elif d==2:
                t+=1
                d=1
            elif d==3:
                t+=1
                d=4
            else:
                t+=1
                d=3
        else:
            for _ in range(l, idx, -1):
                queue.appendleft(chess[x][y].pop())
            chess[x][y].pop()
            queue.appendleft([i ,d])
            chess[x][y].extend(list(queue))
            if len(chess[x][y])>=4:
                print(time)
                exit(0)
            queue.clear()
            break
            
while(1):
    for number in range(K):
        move(number)
    if time>1000:
        print('-1')
        exit(0)
    time+=1