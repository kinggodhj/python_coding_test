N=int(input().rstrip())
game=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]

green=[[0]*4 for _ in range(6)]
blue=[[0]*6 for _ in range(4)]
score=0

def one_block(x, y):
    nx=0
    for i in range(5):
        if green[i][y]==0 and green[i+1][y]==0:
            nx=i+1
        else:
            break
    green[nx][y]=1
    get_row_score()
    green_remove(nx)

    ny=0
    for j in range(5):
        if blue[x][j]==0 and blue[x][j+1]==0:
            ny=j+1
        else:
            break
    blue[x][ny]=1
    get_col_score()
    blue_remove(ny)

def two_block(x, y):
    nx=0
    for i in range(5):
        if green[i][y]==0 and green[i][y+1]==0:
            if green[i+1][y]==0 and green[i+1][y+1]==0:
                nx=i+1
            else:
                break
        else:
            break
    green[nx][y]=1
    green[nx][y+1]=1
    get_row_score()
    green_remove(nx)

    ny=0
    for j in range(4):
        if blue[x][j]==0 and blue[x][j+1]==0:
            if blue[x][j+2]==0:
                ny=j+1
            else:
                break
        else:
            break
    blue[x][ny]=1
    blue[x][ny+1]=1
    get_col_score()
    get_col_score()
    blue_remove(ny)
                                      
def three_block(x, y):
    nx=0
    for i in range(4):
        if green[i][y]==0 and green[i+1][y]==0:
            if green[i+2][y]==0:
                nx=i+1
            else:
                break
        else:
            break
    green[nx][y]=1
    green[nx+1][y]=1
    get_row_score()
    get_row_score()
    green_remove(nx)

    ny=0
    for j in range(5):
        if blue[x][j]==0 and blue[x+1][j]==0:
            if blue[x][j+1]==0 and blue[x+1][j+1]==0:
                ny=j+1
            else:
                break
        else:
            break
    blue[x][ny]=1
    blue[x+1][ny]=1
    get_col_score()
    blue_remove(ny)
               
def green_remove(i):
    global green
    while(1 in green[1]):
        green=[[0]*4]+green[:-1]

def blue_remove(j):
    global blue
    while(1):
        if blue[0][1]==1 or blue[1][1]==1 or blue[2][1]==1 or blue[3][1]==1:
            for i in range(4):
                blue[i]=[0]+blue[i][:-1]
        else:
            break
        
def get_row_score():
    global score
    global green
    for i in range(6):
        if green[i]==[1,1,1,1]:
            score+=1
            green=[[0,0,0,0]]+green[:i]+green[i+1:]
    
def get_col_score():
    global score
    global blue
    for j in range(6):
        if blue[0][j]==1 and blue[1][j]==1 and blue[2][j]==1 and blue[3][j]==1:
            blue[0]=[0]+blue[0][:j]+blue[0][j+1:]
            blue[1]=[0]+blue[1][:j]+blue[1][j+1:] 
            blue[2]=[0]+blue[2][:j]+blue[2][j+1:] 
            blue[3]=[0]+blue[3][:j]+blue[3][j+1:]
            score+=1 

for t,x,y in game:
    if t==1:
        if 0<=x<4 and 0<=y<4:
            one_block(x,y)
    elif t==2:
        if 0<=x<4 and 0<=y<3:
            two_block(x,y)
    elif t==3:
        if 0<=x<3 and 0<=y<4:
            three_block(x,y)
print(score)
count=0

for i in range(4):
    count+=sum(green[i+2])+sum(blue[i][2:])
print(count)