N=int(input().rstrip())
array=[]
total_dust=0
for _ in range(N):
    tmp=list(map(int, input().rstrip().split(' ')))
    array.append(tmp)
    total_dust+=sum(tmp)
start_x, start_y=N//2, N//2
dust=[[0]*N for _ in range(N)]
ratio={0:0.02, 1:0.1, 2:0.07, 3:0.01, 4:0.05, 5:0.1, 6:0.07, 7:0.01, 8:0.02}
coord=[[-2,-1], [-1,-2], [-1,-1], [-1,0], [0,-3], [1,-2], [1,-1], [1, 0], [2,-1], [0,-2], [0,-1], [0,-2]]
arrow=[[0,-1], [1,0], [0,1], [-1,0]]

def rotate(d):
    if d==0:
        r_coord=coord
    elif d==1:
        r_coord=list(map(lambda x:[-1*x[1], x[0]], coord))        
    elif d==2:
        r_coord=list(map(lambda x:[-1*x[0], -1*x[1]], coord))
    elif d==3:
        r_coord=list(map(lambda x:[x[1], -1*x[0]], coord))
    return r_coord

def move(r, c, arr, d):
    r_coord=rotate(d)
    yx, yy=r_coord[-2]
    y_dust=arr[r+yx][c+yy]
    a=y_dust
    arr[r+yx][c+yy]=0
    while(1):
        for i in range(10):
            nx, ny=r_coord[i]
            if 0<=r+nx<N and 0<=c+ny<N:
                if i==9:
                    arr[r+nx][c+ny]+=a
                else:
                    arr[r+nx][c+ny]+=int(y_dust*ratio[i])
                    a-=int(y_dust*ratio[i])
            else:
                if i<9:
                    a-=int(y_dust*ratio[i])
        break

sx, sy=N//2, N//2
i=1
d=0
while(i<N):
    for _ in range(2):
        for r in range(i):
            nx, ny=arrow[d]
            move(sx, sy, array, d)
            sx+=nx
            sy+=ny

        d=(d+1)%4
    i+=1
for i in range(N-1, -1, -1):
    move(sx, i, array, 0)

for i in range(N):
    total_dust-=sum(array[i])
print(total_dust)