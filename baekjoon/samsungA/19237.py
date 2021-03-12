N, M, k=map(int, input().rstrip().split(' '))
ocean=[list(map(int, input().split(' '))) for _ in range(N)]
sharks=[[[0, 0, 0, 0]]*(5) for _ in range(M+1)]
sharks_dir=list(map(int, input().rstrip().split(' ')))
sharks_dir.insert(0, 0)
dir={1:[-1,0], 2:[1,0], 3:[0,-1], 4:[0, 1]}
smell=[[0]*N for _ in range(N)]
#shark_idx=[[0, 0]]*(M+1)
num=M

for i in range(1, M+1):
    for j in range(1, 5):
        sharks[i][j]=list(map(int, input().rstrip().split(' ')))

def findShark(array, smell_array):
    shark_idx=[[-1, -1]]*(M+1)
    for i in range(N):
        for j in range(N):
            if array[i][j]!=0:
                smell_array[i][j]=k
                shark_idx[array[i][j]]=[i, j]
                array[i][j]=[array[i][j]]
    return shark_idx

def times(array, smell_array):
    for i in range(N):
        for j in range(N):
            if smell_array[i][j]!=0:
                smell_array[i][j]-=1
                '''
                if smell_array[i][j]==0:
                    array[i][j]=0
                '''
def survive(array, idx_l):
    global num
    for i in range(N):
        for j in range(N):
            if type(array[i][j]) is list:
                if len(array[i][j])>1:
                    tmp=min(array[i][j])
                    for nn in array[i][j]:
                        if nn != tmp:
                            idx_l[nn]=[-1, -1]
                    num-=len(array[i][j])-1
                    array[i][j]=[tmp]

def spread(idx_l, dir_l, array, smell_array):
    check=[False]*len(idx_l)
    for s in range(1, len(idx_l)):
        x=idx_l[s][0]
        y=idx_l[s][1]
        if x==-1 and y==-1:
            continue
        d=dir_l[s]
        for next_dir in sharks[s][d]:
            dx, dy=dir[next_dir]
            if 0<=x+dx<N and 0<=y+dy<N:
                if array[x+dx][y+dy]==0:
                    array[x+dx][y+dy]=[s]
                    smell[x+dx][y+dy]=k+1
                    idx_l[s]=[x+dx, y+dy]
                    dir_l[s]=next_dir
                    check[s]=True
                    break
                elif smell[x+dx][y+dy]==k+1:
                    array[x+dx][y+dy].extend([s])
                    idx_l[s]=[x+dx, y+dy]
                    dir_l[s]=next_dir
                    check[s]=True
                    break
                elif smell[x+dx][y+dy]==0:
                    array[x+dx][y+dy]=[s]
                    smell[x+dx][y+dy]=k+1
                    idx_l[s]=[x+dx, y+dy]
                    dir_l[s]=next_dir
                    check[s]=True
                    break

    for s in range(1, len(idx_l)):
        if check[s]==True:
            continue
        x=idx_l[s][0]
        y=idx_l[s][1]
        if x==-1 and y==-1:
            continue
        d=dir_l[s]
        for next_dir in sharks[s][d]:
            dx, dy=dir[next_dir]
            if 0<=x+dx<N and 0<=y+dy<N:
                if array[x+dx][y+dy]==[s]:
                    smell[x+dx][y+dy]=k+1
                    idx_l[s]=[x+dx, y+dy]
                    dir_l[s]=next_dir
                    check[s]=True
                    break

time=0
shark_idx=findShark(ocean, smell)
while(num>1):
    time+=1
    spread(shark_idx, sharks_dir, ocean, smell)
    times(ocean, smell)
    survive(ocean, shark_idx)
    if time>1000:
        print('-1')
        break
if time<=1000:
    print(time)