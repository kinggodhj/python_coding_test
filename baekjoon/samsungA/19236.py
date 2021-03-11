import copy
dir={1:[-1,0], 2:[-1, -2], 3:[0, -2], 4:[1, -2], 5:[1,0], 6:[1,2], 7:[0, 2], 8:[-1, 2]}
a1=[list(map(int, input().rstrip().split(' '))) for _ in range(4)]

result=0
def DFS(x, y, c, array):
    global result
    array=copy.deepcopy(array)
    c+=array[x][y]
    array[x][y]=-1
    fish_turn(array)
    possibles=possible_fish(x, y, array)
    if len(possibles)==0:
        result=max(result, c)
        return
    for pos in possibles:
        array[x][y]=0
        array[x][y+1]=0
        DFS(pos[0],pos[1], c, array)

def possible_fish(x, y, array):
    d=array[x][y+1]
    dx, dy=dir[d]
    possible=[]
    while(1):
        x+=dx
        y+=dy
        if 0<=x<4 and 0<=y<8:
            if 1<=array[x][y]<=16:
                possible.append([x, y])
        else:
            break
    return possible

def find_fish(k, ocean):
    for i in range(4):
        for j in range(0, 8, 2):
            if ocean[i][j]==k:
                return [i , j]
    return None

def fish_turn(ocean):
    for k in range(1, 17):
        ans=find_fish(k, ocean)
        if ans is None:
            continue 
        x=ans[0]
        y=ans[1]
        now_dir=ocean[x][y+1]
        for _ in range(8):
            dx, dy=dir[now_dir]
            if 0<=x+dx<4 and 0<=y+dy<8:
                if 0<=ocean[x+dx][y+dy]<=16:
                    ocean[x][y], ocean[x+dx][y+dy]=ocean[x+dx][y+dy], ocean[x][y]
                    ocean[x][y+1], ocean[x+dx][y+dy+1]=ocean[x+dx][y+dy+1], now_dir
                    break                   
            now_dir=(now_dir%8)+1
            ocean[x][y+1]=now_dir

DFS(0, 0, 0, a1)
print(result)