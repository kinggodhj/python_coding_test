from collections import deque
N, K=map(int, input().rstrip().split(' '))
array=list(map(int, input().rstrip().split(' ')))
queue=[deque([]) for _ in range(2*N)]

def rotate():
    tmp=array[-1]
    tmp_q=queue[-1]
    for i in range(2*N-2, -1, -1):
        array[i+1]=array[i]
        queue[i+1]=queue[i]
    array[0]=tmp
    queue[0]=tmp_q
    if len(queue[N-1])>0:
        queue[N-1].pop()

def robot_move():
    for i in range(2*N-2, -1 ,-1):
        if len(queue[i])>0 and len(queue[i+1])<1 and array[i+1]>0:
            queue[i].pop()
            queue[i+1].appendleft(1)
            array[i+1]-=1
    if len(queue[N-1])>0:
        queue[N-1].pop()

time=1
while(1):
    rotate()
    robot_move()
    if array[0]>0 and len(queue[0])<1:
        queue[0].appendleft(1)
        array[0]-=1
    zero=0
    for a in array:
        if a==0:
            zero+=1
    if zero>=K:
        print(time)
        break 
    time+=1