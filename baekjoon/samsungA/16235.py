from collections import deque
import copy

N, M, K=map(int, input().rstrip().split(' '))
A=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
queue=[[deque([]) for _ in range(N+1)] for _ in range(N+1)]
trees=[]
for _ in range(M):
    x,y,z=map(int, input().rstrip().split(' '))
    queue[x-1][y-1].appendleft(z)
land=[[5]*N for _ in range(N)]
num=M

df=[[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
def spring():
    global num
    global land
    for x in range(N):
        for y in range(N):
            l=len(queue[x][y])
            energy=land[x][y]
            for _ in range(l):
                z=queue[x][y].pop()
                if land[x][y]>=z:
                    queue[x][y].appendleft(z+1)
                    land[x][y]-=z
                    energy-=z
                else:
                    energy+=z//2
                    num-=1
            if l>0:
                land[x][y]=energy

def fall():
    global num
    for x in range(N):
        for y in range(N):
            if queue[x][y]:
                l=len(queue[x][y])
                for i in range(l):
                    if queue[x][y][i]%5==0:
                        for dx, dy in df:
                            if 0<=x+dx<N and 0<=y+dy<N:
                                queue[x+dx][y+dy].append(1)
                                num+=1

def winter():
    for x in range(N):
        for y in range(N):
            land[x][y]+=A[x][y]

while(K>0):
    spring()
    fall()
    winter()
    K-=1

print(num)