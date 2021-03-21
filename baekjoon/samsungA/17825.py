import copy

scores=list(map(int, input().rstrip().split(' ')))
dices=[[int(1e5),int(1e5),False]]*4

red=[[2,4,6,8,10],[12,14,16,18,20], [22,24,26,28,30],[32,34,36,38,40]]
blue=[[10, 13,16,19,25], [20,22,24,25],[30,28,27,26,25], [30,35,40]]
r_in=[[False]*5 for _ in range(4)]
b_in=[[False]*5 for _ in range(4)]
total=0

def turn(dices, i, move, s):
    x=dices[i][0]
    y=dices[i][1]
    check=dices[i][2]
    if check==False:
        if x!=3:
            if y+move>4:
                if r_in[x+1][(y+move)%5]==False:
                    dices[i][0]=x+1
                    dices[i][1]=(y+move)%5
                    s+=red[dices[i][0]][dices[i][1]]
                    r_in[dices[i][0]][dices[i][1]]=True
                    r_in[x][y]=False
                else:
                    return -1
            elif y+move==4:
                if b_in[0][dices[i][1]]==False:
                    dices[i][1]=0
                    dices[i][2]=True
                    s+=red[dices[i][0]][dices[i][1]]
                    b_in[dices[i][0]][dices[i][1]]=True
                    if x!=0 and y!=-1:
                        r_in[x][y]=False
                else:
                    return -1
            else:
                if r_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=red[dices[i][0]][dices[i][1]]
                    r_in[dices[i][0]][dices[i][1]]=True
                    if x!=0 and y!=-1:
                        r_in[x][y]=False
                else:
                    return -1
        elif x==3:
            if y+move>4:
                dices[i][0]=-1
                dices[i][1]=-1
                dices[i][2]=False
                r_in[x][y]=False
            else:
                if r_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=red[dices[i][0]][dices[i][1]]
                    r_in[dices[i][0]][dices[i][1]]=True
                    r_in[x][y]=False
                else:
                    return -1
    else:
        if x==0:
            if y+move>4:
                if (y+move)%5>=3:
                    dices[i][0]=-1
                    dices[i][1]=-1
                    b_in[x][y]=False
                else:
                    if b_in[x+3][(y+move)%5]==False:
                        dices[i][0]=x+3
                        dices[i][1]=(y+move)%5
                        s+=blue[dices[i][0]][dices[i][1]]
                        b_in[dices[i][0]][dices[i][1]]=True
                        if x!=-1 and y!=-1:
                            b_in[x][y]=False
                    else:
                        return -1
            elif y+move<=4:
                if b_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=blue[dices[i][0]][dices[i][1]]
                    b_in[dices[i][0]][dices[i][1]]=True
                    if x!=-1 and y!=-1:
                        b_in[x][y]=False
                else:
                    return -1
        elif x==1:
            if y+move>3:
                if (y+move)%4>=3:
                    dices[i][0]=-1
                    dices[i][1]=-1
                    b_in[x][y]=False
                else:
                    if b_in[x+2][(y+move)%4]==False:
                        dices[i][0]=x+2
                        dices[i][1]=(y+move)%4
                        s+=blue[dices[i][0]][dices[i][1]]
                        b_in[dices[i][0]][dices[i][1]]=True
                        if x!=-1 and y!=-1:
                            b_in[x][y]=False
                    else:
                        return -1
            elif y+move<=3:
                if b_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=blue[dices[i][0]][dices[i][1]]
                    b_in[dices[i][0]][dices[i][1]]=True
                    if x!=-1 and y!=-1:
                        b_in[x][y]=False
                else:
                    return -1
        elif x==2:
            if y+move>4:
                if (y+move)%5>=3:
                    dices[i][0]=-1
                    dices[i][1]=-1
                    b_in[x][y]=False
                else:
                    if b_in[x+1][(y+move)%5]==False:
                        dices[i][0]=x+1
                        dices[i][1]=(y+move)%5
                        s+=blue[dices[i][0]][dices[i][1]]
                        b_in[dices[i][0]][dices[i][1]]=True
                        b_in[x][y]=False
                    else:
                        return -1
            elif y+move<=4:
                if b_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=blue[dices[i][0]][dices[i][1]]
                    b_in[dices[i][0]][dices[i][1]]=True
                    b_in[x][y]=False
                else:
                    return -1
        elif x==3:
            if y+move>3:
                dices[i][0]=-1
                dices[i][1]=-1
                dices[i][2]=False
                b_in[x][y]=False
            else:
                if b_in[dices[i][0]][y+move]==False:
                    dices[i][1]=y+move
                    s+=blue[dices[i][0]][dices[i][1]]
                    b_in[dices[i][0]][dices[i][1]]=True
                    b_in[x][y]=False
                else:
                    return -1
    return s

def combination(order):
    global total
    if len(order)==10:
        tmp=0
        n_dice=copy.deepcopy(dices)
        for i in range(len(order)):
            if n_dice[order[i]][0]==int(1e5) and n_dice[order[i]][1]==int(1e5):
                n_dice[order[i]]=[0, -1, False]
            tmp=turn(n_dice, order[i], scores[i], tmp)
            if tmp>0:
                continue
            return 
        if tmp>total:
            total=tmp
    else:
        for i in range(4):
            combination(order+[i])
combination([])
print(total)