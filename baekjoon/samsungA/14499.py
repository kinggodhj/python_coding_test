df={1:[0,1],2:[0,-1],3:[-1,0],4:[1,0]}
num=[0]*7
N, M, x, y, K=map(int, input().rstrip().split(' '))
arr=[list(map(int, input().rstrip().split(' '))) for _ in range(N)] 
move=list(map(int, input().rstrip().split(' ')))
dice=[2,1,5,6]
side=[4,3]

def rotate(m):
    global dice
    global side
    if m==1:
        l=side[0]
        r=side[1]
        side=[dice[-1], dice[1]]
        dice[1]=l
        dice[-1]=r
    elif m==2:
        l=side[0]
        r=side[1]
        side=[dice[1], dice[-1]]
        dice[1]=r
        dice[-1]=l
    elif m==3:
        dice=dice[1:]+[dice[0]]
    else:
        dice=[dice[-1]]+dice[0:-1]
    return dice[-1]

for m in move:
    dx, dy=df[m]
    if 0<=x+dx<N and 0<=y+dy<M:
        bottom=rotate(m)
        if arr[x+dx][y+dy]==0:
            arr[x+dx][y+dy]=num[bottom]
        else:
            num[bottom]=arr[x+dx][y+dy]
            arr[x+dx][y+dy]=0
        print(num[7-bottom])
        x+=dx
        y+=dy