import copy
N=int(input().rstrip())
array=[[0]*101 for _ in range(101)]
curve=[]
df={0:[0,1], 1:[-1,0], 2:[0,-1], 3:[1,0]}
rotate={0:1, 1:2, 2:3, 3:0}
answer=0

for _ in range(N):
    y, x, d, g=map(int, input().rstrip().split(' '))
    curve.append([x, y, d, g])

for x, y, d, g in curve:
    lst=[]
    lst.append(d)
    for gen in range(1, g+1):
        prev=len(lst)
        tmp=copy.deepcopy(lst)
        for _ in range(prev):
            lst.append(rotate[tmp.pop()])
    now=len(lst)
    for i in range(now):
        array[x][y]=1
        dx, dy=df[lst[i]]
        if 0<=x+dx<=100 and 0<=y+dy<=100:
            x+=dx
            y+=dy
            array[x][y]=1

for i in range(100):
    for j in range(100):
        if array[i][j]==1 and array[i][j+1]==1 and array[i+1][j]==1 and array[i+1][j+1]==1:
            answer+=1

print(answer)