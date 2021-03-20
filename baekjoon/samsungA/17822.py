from collections import deque
import copy
N, M, T=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
rotation=[list(map(int, input().rstrip().split(' ' ))) for _ in range(T)]
queue=deque([])
count=N*M

def rotate(x, d, k, arr):
    now=arr[x]
    case=0
    if d==0:
        case=k
    else:
        case=M-k
    now=now[-case:]+now[:(M-case)]
    arr[x]=now

def up(x, y):
    if x<N-1:
        return x+1, y
    return None

def down(x, y):
    if x!=0:
        return x-1, y
    return None

def left(x, y):
    if y==0:
        return x, M-1
    return x, y-1

def right(x, y):
    if y==M-1:
        return x, 0
    return x, y+1

def BFS(i, j, check, visited):
    global count
    queue.appendleft([i,j])
    next_check=False
    while queue:
        remove=False
        x, y=queue.pop()
        next_c=up(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==array[x][y] and check[next_c[0]][next_c[1]]!=0:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1]])
                check[next_c[0]][next_c[1]]=0
                count-=1
                remove=True
        next_c=down(x, y)
        if next_c is not None:
            visited[next_c[0]][next_c[1]]=1
            if array[next_c[0]][next_c[1]]==array[x][y] and check[next_c[0]][next_c[1]]!=0:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1]])
                check[next_c[0]][next_c[1]]=0
                count-=1
                remove=True
        next_c=right(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==array[x][y] and check[next_c[0]][next_c[1]]!=0:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1]])
                check[next_c[0]][next_c[1]]=0
                count-=1
                remove=True
        next_c=left(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==array[x][y] and check[next_c[0]][next_c[1]]!=0:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1]])
                check[next_c[0]][next_c[1]]=0
                count-=1
                remove=True
        if remove==True:
            next_check=True
            check[x][y]=0
            count-=1
    return visited, check, next_check

def find_mean(arr):
    global count
    total=0
    for _ in range(len(arr)):
        total+=sum(arr[_])
    mean=total/count
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                if arr[i][j] > mean:
                    arr[i][j]-=1
                else:
                    arr[i][j]+=1 

total=0
for x,d,k in rotation:
    m=1
    while(x*m-1<N):
        rotate((x*m-1), d, k, array)
        m+=1
    check=copy.deepcopy(array)
    visited=[[0]*M for _ in range(N)]
    not_mean=False
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0:
                visited[i][j]=1
                visited, array, rem=BFS(i, j, check, visited)
                if rem==True:
                    not_mean=True
    if not_mean==False:
        find_mean(array)
for i in range(len(array)):
    total+=sum(array[i])
print(total)