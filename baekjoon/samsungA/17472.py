from collections import deque
import copy

queue=deque([])
N, M=map(int, input().rstrip().split(' '))
array=[]
island=[]
df=[[0,1], [0,-1], [1,0],[-1,0]]
length=int(1e9)

def connected(arr, d_arr):
    global island
    visit=copy.deepcopy(arr)
    queue.appendleft([island[0][0], island[0][1], ''])
    visit[island[0][0]][island[0][1]]=0
    count=0
    while queue:
        x, y, d=queue.pop()
        if arr[x][y]<0:
            count+=1
            dx, dy=d[0], d[1]
            if 0<=x+dx<N and 0<=y+dy<M:
                if arr[x+dx][y+dy]==1 and visit[x+dx][y+dy]==1:
                    visit[x+dx][y+dy]=0
                    queue.appendleft([x+dx, y+dy, ''])
                elif arr[x+dx][y+dy]<0 and visit[x+dx][y+dy]<0:
                    if len(d_arr[x+dx][y+dy])<2:
                        d_arr[x+dx][y+dy]=0
                    else:
                        if dx==0:
                            d_arr[x+dx][y+dy]=[1]
                        elif dy==0:
                            d_arr[x+dx][y+dy]=[0]
                    visit[x+dx][y+dy]+=1
                    queue.appendleft([x+dx, y+dy, (dx, dy)])
        else:      
            for i in range(len(df)):
                dx, dy=df[i]
                if 0<=x+dx<N and 0<=y+dy<M:
                    if arr[x+dx][y+dy]==0 and visit[x+dx][y+dy]==0:
                        visit[x+dx][y+dy]=1
                    elif arr[x+dx][y+dy]==1 and visit[x+dx][y+dy]==1:
                        visit[x+dx][y+dy]=0
                        queue.appendleft([x+dx, y+dy, '']) 
                    elif arr[x+dx][y+dy]<0 and visit[x+dx][y+dy]<0:
                        if len(d_arr[x+dx][y+dy])<2:
                            if dx==0 and d_arr[x+dx][y+dy]==[0]:
                                d_arr[x+dx][y+dy]=0
                                visit[x+dx][y+dy]+=1
                                queue.appendleft([x+dx, y+dy, (dx, dy)])
                            elif dy==0 and d_arr[x+dx][y+dy]==[1]:
                                d_arr[x+dx][y+dy]=0
                                visit[x+dx][y+dy]+=1
                                queue.appendleft([x+dx, y+dy, (dx, dy)])
                        elif len(d_arr[x+dx][y+dy])==2:
                            if dx==0 and 0 in d_arr[x+dx][y+dy]:
                                d_arr[x+dx][y+dy]=[1]
                                visit[x+dx][y+dy]+=1
                                queue.appendleft([x+dx, y+dy, (dx, dy)])
                            elif dy==0 and 1 in d_arr[x+dx][y+dy]:
                                d_arr[x+dx][y+dy]=[0]
                                visit[x+dx][y+dy]+=1
                                queue.appendleft([x+dx, y+dy, (dx, dy)])

    for i,j in island:
        if visit[i][j]==1:
            return False, count
    return True, count

def makeBridge(x, y, a, d):
    global length
    r, c=connected(a, copy.deepcopy(d))
    if r==True:
        if c<length and c!=0:
            length=c
    else:
        for i in range(x, N):
            for j in range(M):
                if i==x and j<y:
                    continue
                if a[i][j]!=1:
                    continue
                #가로        
                if j+2<=M-1:
                    if a[i][j+1]==1:
                        pass 
                    #elif a[i][j+1]<0 and a[i][j+2]<0:
                    elif type(d[i][j+1])==list:
                        if 0 not in d[i][j+1]:
                            k=j
                            while(a[i][k+1]!=1):
                                k+=1
                                if k==M-1:
                                    break
                            if k-j>1 and k<M-1 and a[i][k+1]==1:
                                arr=copy.deepcopy(a)
                                d_arr=copy.deepcopy(d)
                                for n in range(j+1, k+1):
                                    arr[i][n]-=1
                                    if d_arr[i][n]==0:
                                        d_arr[i][n]=[0]
                                    else:
                                        d_arr[i][n].append(0)
                                makeBridge(i, j, arr, d_arr)
                    else:
                        k=j
                        while(a[i][k+1]!=1):
                            k+=1
                            if k==M-1:
                                break
                        if k-j>1 and k<M-1 and a[i][k+1]==1:
                            arr=copy.deepcopy(a)
                            d_arr=copy.deepcopy(d)
                            for n in range(j+1, k+1):
                                arr[i][n]-=1
                                if d_arr[i][n]==0:
                                    d_arr[i][n]=[0]
                                else:
                                    d_arr[i][n].append(0)
                            makeBridge(i, j, arr, d_arr)
                #세로
                if i+2<=N-1: 
                    if a[i+1][j]==1:
                        pass
                    elif type(d[i+1][j])==list:
                        if 1 not in d[i+1][j]:
                            k=i
                            while(a[k+1][j]!=1):
                                k+=1
                                if k==N-1:
                                    break
                            if i+1<k<N-1 and a[k+1][j]==1:
                                arr=copy.deepcopy(a)
                                d_arr=copy.deepcopy(d)
                                for n in range(i+1, k+1):
                                    arr[n][j]-=1
                                    if d_arr[n][j]==0:
                                        d_arr[n][j]=[1]
                                    else:
                                        d_arr[n][j].append(1)
                                makeBridge(i, j+1, arr, d_arr)
                    else:
                        k=i
                        while(a[k+1][j]!=1):
                            k+=1
                            if k==N-1:
                                break
                        if i+1<k<N-1 and a[k+1][j]==1:
                            arr=copy.deepcopy(a)
                            d_arr=copy.deepcopy(d)
                            for n in range(i+1, k+1):
                                arr[n][j]-=1
                                if d_arr[n][j]==0:
                                    d_arr[n][j]=[1]
                                else:
                                    d_arr[n][j].append(1)
                            makeBridge(i, j+1, arr, d_arr)
                            

for i in range(N):
    tmp=list(map(int, input().rstrip().split(' ')))
    array.append(tmp)
    for j in range(M):
        if tmp[j]==1:
            island.append([i, j])

d_array=[[0]*M for _ in range(N)]
makeBridge(0, 0, array, d_array)

if length==int(1e9):
    print('-1')
else:
    print(length)