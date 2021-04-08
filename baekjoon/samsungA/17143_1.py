R, C, M=map(int, input().rstrip().split(' '))
array=[[0]*C for _ in range(R)]
shark=[]
for _ in range(M):
    r,c,s,d,z=map(int, input().rstrip().split(' '))
    array[r-1][c-1]=[s,d,z]

df={1:[-1,0], 2:[1,0], 3:[0,1], 4:[0,-1]}
rotate={1:2, 2:1, 3:4, 4:3}

def move(arr):
    result=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if array[i][j]==0:
                continue
            s,d,z=array[i][j]
            dx, dy=df[d]
            nx=i+dx*s
            ny=j+dy*s
            if d==1 or d==2:
                nx=nx%((R-1)*2)
                if nx<0 or nx>=R:
                    nx=(R-1)-(nx%(R-1))
                    d=rotate[d]
                if result[nx][j]==0:
                    result[nx][j]=[s,d,z]
                elif result[nx][j][-1]<z:
                    result[nx][j]=[s,d,z]
            elif d==3 or d==4:
                ny=ny%((C-1)*2)
                if ny<0 or ny>=C:
                    ny=(C-1)-(ny%(C-1))
                    d=rotate[d]
                if result[i][ny]==0:
                    result[i][ny]=[s,d,z]
                elif result[i][ny][-1]<z:
                    result[i][ny]=[s,d,z]
    return result
 
catch=0
start=0
while(start<C):
    for i in range(R):
        if array[i][start]==0:
            continue
        catch+=array[i][start][-1]
        array[i][start]=0
        break
    array=move(array)
    start+=1

print(catch)