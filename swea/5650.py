from collections import deque
T=int(input().rstrip())
queue=deque([])
dir=[{-1:-1}, {1:2, 2:4, 3:1, 4:3}, {1:4, 2:1, 3:2, 4:3}, {1:3, 2:1, 3:4, 4:2}, {1:2, 2:3, 3:4, 4:1}, {1:2, 2:1, 3:4, 4:3}]
df={1:[-1,0],2:[1,0],3:[0,-1],4:[0,1]}
answer=[]
for test_case in range(1, T+1):
    N=int(input().rstrip())
    array=[]
    warm=[[0]]*11
    for i in range(N):
        tmp=list(map(int, input().rstrip().split(' ')))
        array.append(tmp)
        for j in range(N):
            if tmp[j]==0:
                continue
            if tmp[j]>5:
                if warm[tmp[j]]==[0]:
                    warm[tmp[j]]=[[i, j]]
                else:
                    warm[tmp[j]].append([i, j])
    def BFS(sx, sy, sd):
        score=0
        nx, ny=df[sd]
        queue.appendleft([sx+nx, sy+ny, sd])
        while queue:
            x, y, d=queue.pop()
            if 0<=x<N and 0<=y<N:
                if x==sx and y==sy or array[x][y]==-1:
                    queue.clear()
                    return score
                if array[x][y]==0:
                    queue.appendleft([x+df[d][0], y+df[d][1], d])
                else:
                    if array[x][y]<6:
                        score+=1
                        d=dir[array[x][y]][d]
                        queue.appendleft([x+df[d][0], y+df[d][1], d])
                    elif array[x][y]>=6:
                        w=warm[array[x][y]]
                        for n in w:
                            if n!=[x, y]:
                                queue.appendleft([n[0]+df[d][0], n[1]+df[d][1], d])
            else:
                score+=1
                d=dir[-1][d]
                if x+df[d][0]==sx and y+df[d][1]==sy:
                    queue.clear()
                    return score
                queue.appendleft([x+df[d][0], y+df[d][1], d])
    result=0
    for i in range(N):
        for j in range(N):
            if array[i][j]==0:
                for d in range(1,5):
                    c=BFS(i, j, d)
                    if c>result:
                        result=c
    answer.append(result)

for t in range(T):
    print('#%d %d'%(t+1, answer[t]))