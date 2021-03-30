from collections import deque
import copy
import itertools
T=int(input().rstrip())
result=[]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
for test_case in range(T):
    N=int(input().rstrip())
    array=[]
    people=[]
    stair=[]
    answer=int(1e9)
    for i in range(N):
        tmp=list(map(int, input().rstrip().split(' ')))
        array.append(tmp)
        for j in range(N):
            if tmp[j]==0:
                continue
            if tmp[j]==1:
                people.append([i, j])
            elif tmp[j]>1:
                stair.append([i, j])
    def BFS(sx, sy, arr):
        visited=[[0]*N for _ in range(N)]
        queue=deque([])
        queue.appendleft([sx, sy, 0])
        visited[sx][sy]=0
        wait=[]
        while queue:
            x, y, t=queue.pop()
            idx=None
            for check in range(len(wait)):
                if wait[check]>t+1:
                    idx=check
                    break
            if idx is not None:
                wait=wait[idx:]
            for d in range(4):
                if 0<=x+dx[d]<N and 0<=y+dy[d]<N:
                    if arr[x+dx[d]][y+dy[d]]==1:
                        if len(wait)<3:
                            if visited[x+dx[d]][y+dy[d]]==0:
                                visited[x+dx[d]][y+dy[d]]=t+2+arr[sx][sy]
                                queue.appendleft([x+dx[d], y+dy[d], t+1])
                                wait.append(t+2+arr[sx][sy])
                        else:
                            if visited[x+dx[d]][y+dy[d]]==0:
                                visited[x+dx[d]][y+dy[d]]=t+1+arr[sx][sy]+(wait[-3]-t-1)
                                queue.appendleft([x+dx[d], y+dy[d], t+1])
                                wait.append(t+1+arr[sx][sy]+(wait[-3]-t-1))
                    elif arr[x+dx[d]][y+dy[d]]==0 and visited[x+dx[d]][y+dy[d]]==0:
                        visited[x+dx[d]][y+dy[d]]=t+1
                        queue.appendleft([x+dx[d], y+dy[d], t+1])
        return visited
    
    case=[[0,1]]*len(people)
    caselist=list(itertools.product(*case))
    for lst in caselist:
        s1=0
        s2=0
        arr1=copy.deepcopy(array)
        arr2=copy.deepcopy(array)
        for i in range(len(people)):
            x, y=people[i]
            if lst[i]==0:
                arr2[x][y]=0
                s1+=1
            elif lst[i]==1:
                arr1[x][y]=0
                s2+=1

        if s1>0 and s2>0:
            v1=BFS(stair[0][0], stair[0][1], arr1)
            v2=BFS(stair[1][0], stair[1][1], arr2)
            m1=0
            m2=0
            for i in range(N):
                for j in range(N):
                    if arr1[i][j]==1:
                        if v1[i][j]>m1:
                            m1=v1[i][j]
                    if arr2[i][j]==1:
                        if v2[i][j]>m2:
                            m2=v2[i][j]
            if max(m1, m2)<answer:
                answer=max(m1, m2)
        elif s1>0 and s2==0:
            v1=BFS(stair[0][0], stair[0][1], arr1)
            m1=0
            for i in range(N):
                for j in range(N):
                    if arr1[i][j]==1:
                        if v1[i][j]>m1:
                            m1=v1[i][j]
            if m1<answer:
                answer=m1
        elif s1==0 and s2>0:
            v2=BFS(stair[1][0], stair[1][1], arr2)
            m2=0
            for i in range(N):
                for j in range(N):
                    if arr2[i][j]==1:
                        if v2[i][j]>m2:
                            m2=v2[i][j]
            if m2<answer:
                answer=m2
    result.append(answer)

for t in range(T):
    print("#%d %d"%(t+1, result[t]))