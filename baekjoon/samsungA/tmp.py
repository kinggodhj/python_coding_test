N=int(input().rstrip())
game=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]

green=[[0]*4 for _ in range(6)]
blue=[[0]*6 for _ in range(4)]
score=0

def one_block(x, y):
    global green
    global blue
    s_g=False
    s_b=False
    for i in range(2, 6):
        if s_g==True and s_b==True:
            break
        if s_g==False:
            if green[i][y]==0:
                if i==5 or green[i+1][y]==1:
                    green[i][y]=1
                    get_row_score(i)
                    s_g=True
            else:
                green[1][y]=1
                green=[[0]*4]+green[:-1]
                s_g=True
        if s_b==False:            
            if blue[x][i]==0:
                if i==5 or blue[x][i+1]==1:
                    blue[x][i]=1
                    get_col_score(i)
                    s_b=True
            else:
                blue[x][1]=1
                for i in range(4):
                    blue[i]=[0]+blue[i][:-1]
                    s_b=True

def two_block(x, y):
    global green
    global blue
    s_g=False
    s_b=False
    for i in range(2, 6):
        if s_g==True and s_b==True:
            break
        if s_g==False:
            if green[i][y]==0 and green[i][y+1]==0:
                if i==5 or green[i+1][y]==1 or green[i+1][y+1]==1:
                    green[i][y]=1
                    green[i][y+1]=1
                    s_g=True
                    get_row_score(i)
            else:
                green[1][y]=1
                green[1][y+1]=1
                green=[[0]*4]+green[:-1]
                s_g=True
        if s_b==False:
            if i<5:
                if blue[x][i]==0 and blue[x][i+1]==0:
                    if i==4 or blue[x][i+2]==1:
                        blue[x][i]=1
                        blue[x][i+1]=1
                        get_col_score(i)
                        get_col_score(i+1)
                        s_b=True
                else:
                    if blue[x][i]==1:    
                        blue[x][0]=1
                        blue[x][1]=1    
                        for i in range(4):
                            blue[i]=[0]*2+blue[i][:-2]
                            s_b=True
                    else:
                        blue[x][i]=1
                        blue[x][1]=1
                        for i in range(4):
                            blue[i]=[0]+blue[i][:-1]
                            s_b=True
                                          
def three_block(x, y):
    global green
    global blue
    s_g=False
    s_b=False
    for i in range(2, 6):
        if s_g==True and s_b==True:
            break
        if s_g==False:
            if i<5:
                if green[i][y]==0 and green[i+1][y]==0:
                    if i==4 or green[i+2][y]==1:
                        green[i][y]=1
                        green[i+1][y]=1
                        get_row_score(i)
                        get_row_score(i+1)
                        s_g=True
                else:
                    if green[i][y]==1:
                        green[0][y]=1
                        green[1][y]=1
                        green=[[0]*4]*2+green[:-2]
                        s_g=True
                    else:
                        green[1][y]=1
                        green=[[0]*4]+green[:-1]
                        s_g=True
        if s_b==False:
            if blue[x][i]==0 and blue[x+1][i]==0:
                if i==5 or blue[x+1][i]==1 or blue[x+1][i+1]==1:
                    blue[x][i]=1
                    blue[x+1][i]=1
                    get_col_score(i)
                    s_b=True
            else:
                blue[x][1]=1
                blue[x+1][1]=1
                for i in range(4):
                    blue[i]=[0]+blue[i][:-1]
                    s_b=True

def get_row_score(i):
    count=0
    global score
    global green
    for j in range(4):
        if green[i][j]==1:
            count+=1
    if count==4:
        score+=1
        green=[[0]*4]+green[:i]+green[i+1:]

def get_col_score(j):
    count=0
    global score
    global blue
    for i in range(4):
        if blue[i][j]==1:
            count+=1
    if count==4:
        score+=1
        for i in range(4):
            blue[i]=[0]+blue[i][:j]+blue[i][j+1:]    

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