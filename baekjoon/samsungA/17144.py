R,C,T=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(R)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1 ,1]

def purification_up(x, y, arr):
    value=arr[x][C-1]
    value2=arr[0][C-1]
    value3=arr[0][0]
    dy=C-1
    while(dy>(y+1)):
        arr[x][dy]=arr[x][dy-1]
        dy-=1
    dx=0
    arr[x][y+1]=0
    while(dx<(x-1)):
        arr[dx][C-1]=arr[dx+1][C-1]
        dx+=1
    arr[dx][C-1]=value
    dy=0
    dx=0
    while(dy<(C-2)):
        arr[dx][dy]=arr[dx][dy+1]
        dy+=1
    arr[dx][dy]=value2
    dx=x-1
    while(dx>1):
        arr[dx][0]=arr[dx-1][0]
        dx-=1
    arr[dx][0]=value3

def purification_down(x, y, arr):
    value=arr[x][C-1]
    value2=arr[R-1][C-1]
    value3=arr[R-1][0]
    dy=C-1
    while(dy>(y+1)):
        arr[x][dy]=arr[x][dy-1]
        dy-=1
    arr[x][y+1]=0
    dx=R-1
    while(dx>(x+1)):
        arr[dx][C-1]=arr[dx-1][C-1]
        dx-=1
    arr[dx][C-1]=value
    dy=0
    dx=R-1
    while(dy<(C-2)):
        arr[dx][dy]=arr[dx][dy+1]
        dy+=1
    arr[dx][dy]=value2
    dx=x+1
    while(dx<(R-2)):
        arr[dx][0]=arr[dx+1][0]
        dx+=1
    arr[dx][0]=value3

def dust_spread(x, y, array, tmp):
    dust=array[x][y]//5
    count=0
    if dust!=0:
        for i in range(4):
            if 0<=x+dx[i]<R and 0<=y+dy[i]<C:
                if array[x+dx[i]][y+dy[i]]!=-1: 
                    count+=1
                    tmp[x+dx[i]][y+dy[i]]+=dust
        if count>0:
            tmp[x][y]+=array[x][y]-(dust)*count
    else:
        tmp[x][y]+=array[x][y]
    return tmp

t=0
while(t<T):
    dust_arr=[]
    pur=[]
    for i in range(R):
        for j in range(C):
            if array[i][j]>0:
                dust_arr.append([i, j])
            elif array[i][j]==-1:
                pur.append([i, j])

    res=[[0]*C for _ in range(R)]
    res[pur[0][0]][pur[0][1]]=-1
    res[pur[1][0]][pur[1][1]]=-1
    for x,y in dust_arr:
        res=dust_spread(x, y, array, res)
    purification_up(pur[0][0], pur[0][1], res)
    purification_down(pur[1][0], pur[1][1], res)
    t+=1
    array=res

answer=0
for i in range(R):
    for j in range(C):
        if array[i][j]>0:
            answer+=array[i][j]
 
print(answer)