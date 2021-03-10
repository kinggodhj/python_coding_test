from collections import deque
T=int(input())
for test in range(1,T+1):
    queue=deque([])
    dx=[-1, 1, 0, 0]
    dy=[0 , 0, -1, 1]


    N,M,K=map(int, input().rstrip().split(' '))
    array=[[0]*(M+600) for _ in range(N+600)]
    check=[[0]*(M+600) for _ in range(N+600)]
    time_check=[[0]*(M+600) for _ in range(N+600)]

    for i in range(N):
        tmp=list(map(int, input().rstrip().split(' ')))
        for j in range(len(tmp)):
            array[300+i][300+j]=tmp[j]

    def spread(time, lst):
        if time==K:
            next_lst=set()
        else:
            next_lst=[]
        while queue:
            x,y,value=queue.pop()
            if time>check[x][y]:
                if time < (check[x][y]+array[x][y]):
                    if time==K:
                        next_lst.add((x, y))
                    else:
                        next_lst.append([x, y, array[x][y]])
                if value==array[x][y]:
                    time_check[x][y]=time
                    for i in range(4):
                        if 0<=x+dx[i]<N+600 and 0<=y+dy[i]<M+600:
                            if array[x+dx[i]][y+dy[i]]==0:
                                array[x+dx[i]][y+dy[i]]=array[x][y]
                                check[x+dx[i]][y+dy[i]]=time+array[x][y]
                                time_check[x+dx[i]][y+dy[i]]=time+1
                                
                                if time==K:
                                    next_lst.add((x+dx[i], y+dy[i]))
                                else:
                                    next_lst.append([x+dx[i], y+dy[i], array[x][y]])
                            else:
                                if array[x+dx[i]][y+dy[i]]<array[x][y] and time_check[x+dx[i]][y+dy[i]]==time+1:
                                    array[x+dx[i]][y+dy[i]]=array[x][y]
                                    check[x+dx[i]][y+dy[i]]=time+array[x][y]
                                   
                                    if time==K:
                                        next_lst.add((x+dx[i], y+dy[i]))
                                    else:
                                        next_lst.append([x+dx[i], y+dy[i], array[x][y]])
            else:
                if time==K:
                    next_lst.add((x, y))
                else:
                    next_lst.append([x, y, value])
        return next_lst

    lst=[]
    for num in range(1, 11):
        for i in range(300, 300+N):
            for j in range(300, 300+M):
                if array[i][j]==num:
                    lst.append([i, j, num])
                    check[i][j]=array[i][j]
                    time_check[i][j]=1
    queue.extendleft(lst)

    ans=0
    for t in range(1, K+1):
        lst=spread(t, lst)
        if t==K:
            print("#%s %d"%(test, len(lst)))
            break
        queue.extendleft(lst)