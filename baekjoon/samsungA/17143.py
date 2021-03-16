from collections import deque

R, C, M=map(int, input().rstrip().split(' '))
queue=[[deque([]) for _ in range(C+1)] for _ in range(R+1)]
sharks=[[0]*(C+1) for _ in range(R+1)]
shark_count=0
for _ in range(M):
    r,c,s,d,z=map(int, input().rstrip().split(' '))
    queue[r][c].appendleft([s,d,z])
    sharks[r][c]=1
    shark_count+=1

answer=0
def fishing(c, shark):
    global answer
    global shark_count
    for r in range(1, R+1):
        if queue[r][c]:
            _, _, a=queue[r][c].pop()
            answer+=a
            shark[r][c]=0
            shark_count-=1
            break

def move(shark):
    next_s=[[0]*(C+1) for _ in range(R+1)]
    big=[]
    for r in range(1, R+1):                                                                              
        for c in range(1, C+1):
            if shark[r][c]!=0:
                s,d,z=queue[r][c].pop()
                x, y=r, c
                count=0
                tmp=s
                if d==1 or d==2:
                    tmp=tmp%((R-1)*2)
                    if tmp==0:
                        if d==1:
                            queue[r][c].appendleft([s, 2, z])
                        else:
                            queue[r][c].appendleft([s, 1, z])
                    else:
                        while(count!=tmp):
                            if d==2:
                                if x<R:
                                    x+=1
                                    count+=1
                                elif x==R:
                                    d=1
                            elif d==1:
                                if x>1:
                                    x-=1
                                    count+=1
                                elif x==1:
                                    d=2
                        queue[x][y].appendleft([s,d,z])
                elif d==3 or d==4:
                    tmp=tmp%((C-1)*2)
                    if tmp==0:
                        if d==3:
                            queue[r][c].appendleft([s, 4, z])
                        else:
                            queue[r][c].appendleft([s, 3, z])
                    else:
                        while(count!=tmp):
                            if d==3:
                                if y<C:
                                    y+=1
                                    count+=1
                                elif y==C:
                                    d=4
                            elif d==4:
                                if y>1:
                                    y-=1
                                    count+=1
                                elif y==1:
                                    d=3
                        queue[x][y].appendleft([s,d,z])
                next_s[x][y]+=1
                if next_s[x][y]>1:
                    big.append([x, y])
    return next_s, big

def biggest(b_list):
    #shark=[[0]*(C+1) for _ in range(R+1)]
    global shark_count
    for r, c in b_list:
        s_m, d_m, z_m=0,0,-1
        shark_count-=(len(queue[r][c])-1)
        while queue[r][c]:
            s,d,z=queue[r][c].pop()
            if z>z_m:
                s_m=s
                d_m=d
                z_m=z
        queue[r][c].appendleft([s_m, d_m, z_m])

for c in range(1, C+1):
    if shark_count==0:
        break
    fishing(c, sharks)
    sharks, b_list=move(sharks)
    biggest(b_list)
print(answer)