from collections import deque
import copy
queue=deque([])
turn={1:2, 2:3, 3:4, 4:1}
df={1:[1,1], 2:[1,-1], 3:[-1,-1], 4:[-1,1]}
T=int(input().rstrip())
for test in range(T):
    N=int(input().rstrip())
    array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    kind=-1

    def DFS(x, y, d, c, stack, dessert):
        global kind
        if kind==(N-1)*2:
            return
        eat=copy.deepcopy(dessert)
        if d==1 or d==2:
            dx, dy=df[d]
            if 0<=x+dx<N and 0<=y+dy<N:
                if eat[array[x+dx][y+dy]]!=1:
                    c+=1
                    eat[array[x+dx][y+dy]]=1
                    stack[d].append(1)
                    DFS(x+dx, y+dy, d, c, stack, eat)
                    eat[array[x+dx][y+dy]]=0
                    c-=1
                    stack[d].pop()
            if len(stack[d])<1:
                return
            d=turn[d]
            dx, dy=df[d]
            if 0<=x+dx<N and 0<=y+dy<N:
                if eat[array[x+dx][y+dy]]!=1:
                    c+=1
                    eat[array[x+dx][y+dy]]=1
                    stack[d].append(1)
                    DFS(x+dx, y+dy, d, c, stack, eat)
                    eat[array[x+dx][y+dy]]=0
                    c-=1
                    stack[d].pop()
                    return
                
            else:
                return
        elif d==3:
            dx, dy=df[d]
            repeat=len(stack[1])
            for k in range(repeat-1):
                x+=dx
                y+=dy
                if 0<=x<N and 0<=y<N:
                    if eat[array[x][y]]!=1:
                        c+=1
                        eat[array[x][y]]=1
                    else:
                        return
                else:
                    return
            d=turn[d]
            dx, dy=df[d] 
            repeat=len(stack[2])
            for k in range(repeat-1):
                x+=dx
                y+=dy
                if 0<=x<N and 0<=y<N:
                    if eat[array[x][y]]!=1:
                        c+=1
                        eat[array[x][y]]=1
                    else:
                        return
                else:
                    return
            if c>kind:
                kind=c
            return

    dessert=[0]*101
    for x in range(N-1):
        for y in range(N-1):
            if array[x+1][y+1]==array[x][y]:
                continue
            dessert[array[x][y]]=1
            dessert[array[x+1][y+1]]=1
            DFS(x+1, y+1, 1, 2, [[],[1],[],[],[]], dessert)
            dessert[array[x][y]]=0
            dessert[array[x+1][y+1]]=0
    print('#%d %d'%(test+1, kind))