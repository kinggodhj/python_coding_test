T=int(input().rstrip())
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for test in range(T):
    N, K=map(int, input().rstrip().split(' '))
    array=[]
    count=0
    top=[]
    top_v=0
    for i in range(N):
        tmp=list(map(int, input().rstrip().split(' ')))
        array.append(tmp)
        for t in range(N):
            if top_v<tmp[t]:
                top=[]
                top_v=tmp[t]
                top.append([i, t])
            elif top_v==tmp[t]:
                top.append([i, t])
    
    def DFS(x, y, c, v, visit, shear):
        global count
        global K
        for d in range(4):
            if 0<=x+dx[d]<N and 0<=y+dy[d]<N:
                nv=array[x+dx[d]][y+dy[d]]
                if visit[x+dx[d]][y+dy[d]]==0:
                    if v>nv:
                        visit[x+dx[d]][y+dy[d]]=1
                        DFS(x+dx[d], y+dy[d], c+1, nv, visit, shear)
                        visit[x+dx[d]][y+dy[d]]=0
                    else:
                        if shear==False:
                            for k in range(1, K+1):
                                if nv-k<v:
                                    shear=True
                                    visit[x+dx[d]][y+dy[d]]=1
                                    DFS(x+dx[d], y+dy[d], c+1, nv-k, visit, shear)
                                    visit[x+dx[d]][y+dy[d]]=0
                                    shear=False
                        else:
                            if count<c:
                                count=c
        if count<c:
            count=c
            
    for x,y in top:
        visit=[[0]*N for _ in range(N)]
        visit[x][y]=1
        DFS(x, y, 1, array[x][y], visit, False)

    print('#%d %d'%(test+1, count))