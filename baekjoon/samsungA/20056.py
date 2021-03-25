from collections import deque
import copy 

dir={0:[-1, 0], 1:[-1, 1], 2:[0,1], 3:[1,1], 4:[1,0], 5:[1, -1], 6:[0,-1], 7:[-1,-1]}
N, M, K=map(int, input().rstrip().split(' '))
fireballs=[[deque([]) for _ in range(N)] for _ in range(N)]
answer=0
for _ in range(M):
    r,c,m,s,d=map(int, input().rstrip().split(' '))
    fireballs[r-1][c-1].appendleft([m, s, d])
    answer+=m

def move(array):
    for i in range(N):
        for j in range(N):
            l=len(fireballs[i][j])
            for k in range(l):
                m, s, d=fireballs[i][j].pop()
                nx, ny=dir[d]
                nx=nx*s+i
                ny=ny*s+j
                if nx<0:
                    nx=nx%N
                if ny<0:
                    ny=ny%N
                if nx>=N:
                    nx=nx%N
                if ny>=N:
                    ny=ny%N
                array[nx][ny].appendleft([m, s, d])
    return array

def concat(array):
    global answer
    for i in range(N):
        for j in range(N):
            l=len(array[i][j])
            if l<2:
                continue
            mass=0
            speed=0
            check=[]
            for k in range(l):
                m, s, d=array[i][j].pop()
                mass+=m
                speed+=s
                if d%2==0:
                    check.append(True)
                else:
                    check.append(False)
            answer-=mass
            mass=mass//5
            speed=speed//l
            if check==[True]*l or check==[False]*l:
                velocity=[0,2,4,6]
            else:
                velocity=[1,3,5,7]
            if mass!=0:
                for n in range(4):
                    array[i][j].append([mass, speed, velocity[n]])
                    answer+=mass
    return array
time=0
while(time<K):
    array=[[deque([]) for _ in range(N)] for _ in range(N)]
    array=move(array)
    array=concat(array)
    fireballs=array
    time+=1
print(answer)