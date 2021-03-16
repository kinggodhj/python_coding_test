from collections import deque
N, K=map(int, input().rstrip().split(' '))
array=list(map(int, input().rstrip().split(' ')))
count=0
zero=0
queue=[deque([]) for _ in range(2*N)]
robot=deque([])

def find_zero():
    global zero
    for a in array:
        if a==0:
            zero+=1
def rotate():
    tmp=array[-1]
    for i in range(2*N-2, -1, -1):
        if i==2*N-2 and len(queue[i])>0:
            queue[i].pop()
        array[i+1]=array[i]
    array[0]=tmp

def robot_move():
    for i in range(2*N):
        if queue[i]:
            if i==2*N-1:
                queue[i].pop()
            else:
                x=queue[i].pop()
                x=(x%2*N)+1
                if array[x]>0:
                    queue[x].appendleft(1)
                    array[x]-=1

time=0
while(zero<K):
    rotate()
    time+=1
    robot_move()
    if array[0]>0:
        queue[0].appendleft(1)
        array[0]-=1
        count+=1
    time+=1
    find_zero()
    time+=1
print(time)