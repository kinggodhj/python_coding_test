import sys
from collections import deque

N=int(sys.stdin.readline())
home=[list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

def findWay(home, N):
    queue=deque([])
    #가로:0, 세로:1, 대각선:2
    dx=[0, 1, 1]
    dy=[1, 0, 1]
    queue.append([0, 1, 0])
    count=0
    while queue:
        x, y, case=queue.pop()
        if x==N-1 and y==N-1:
            count+=1
        else:
            if 0<=x+dx[2]<N and 0<=y+dy[2]<N:
                if home[x+dx[2]][y+dy[2]]==0 and home[x+dx[0]][y+dy[0]]==0 and home[x+dx[1]][y+dy[1]]==0:
                    queue.append([x+dx[2], y+dy[2], 2])
            if case!=2: 
                if 0<=x+dx[case]<N and 0<=y+dy[case]<N:
                    if home[x+dx[case]][y+dy[case]]==0:
                        queue.append([x+dx[case], y+dy[case], case])
            elif case==2:
                for i in range(case):
                    if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                        if home[x+dx[i]][y+dy[i]]==0:
                            queue.append([x+dx[i], y+dy[i], i])
    return count

print(findWay(home, N))