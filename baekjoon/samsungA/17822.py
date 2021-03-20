from collections import deque
import copy
N, M, T=map(int, input().rstrip().split(' '))
array=[deque([]) for _ in range(N)]
queue=deque([])
total=0
for i in range(N):
    l=list(map(int, input().rstrip().split(' ')))
    array[i].extend(l)
    total+=sum(l)
rotation=[list(map(int, input().rstrip().split(' ' ))) for _ in range(T)]
count=N*M

def rotate(x, d, k):
    case=0
    if d==0:
        case=k
    else:
        case=M-k
    array[x].rotate(case)

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

def BFS(visited):
    global count
    global total
    next_check=False
    while queue:
        remove=False
        x, y, v=queue.pop()
        if v==0:
            continue
        next_c=up(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==v:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1], v])
                array[next_c[0]][next_c[1]]=0
                total-=v
                count-=1
                remove=True
        next_c=down(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==v:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1], v])
                array[next_c[0]][next_c[1]]=0
                total-=v
                count-=1
                remove=True
        next_c=right(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==v:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1], v])
                array[next_c[0]][next_c[1]]=0
                total-=v
                count-=1
                remove=True
        next_c=left(x, y)
        if next_c is not None:
            if array[next_c[0]][next_c[1]]==v:
                visited[next_c[0]][next_c[1]]=1
                queue.appendleft([next_c[0], next_c[1], v])
                array[next_c[0]][next_c[1]]=0
                total-=v
                count-=1
                remove=True
        if remove==True and array[x][y]!=0:
            next_check=True
            array[x][y]=0
            total-=v
            count-=1
    return visited, next_check

def find_mean(arr):
    global count
    global total
    mean=total/count
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                continue
            if arr[i][j] > mean:
                arr[i][j]-=1
                total-=1
            elif arr[i][j]<mean:
                arr[i][j]+=1 
                total+=1

for x,d,k in rotation:
    m=x
    while(x-1<N):
        rotate((x-1), d, k)
        x+=m
    visited=[[0]*M for _ in range(N)]
    not_mean=False
    for i in range(N):
        for j in range(M):
            if visited[i][j]!=0:
                continue
            visited[i][j]=1
            if array[i][j]==0:
                continue
            queue.appendleft([i, j, array[i][j]])
            visited, rem=BFS(visited)
            if not_mean==True:
                continue
            if rem==True:
                not_mean=True
    if total==0 and count==0:
        print(total)
        exit(0)
    if not_mean==False:
        find_mean(array)

print(total)