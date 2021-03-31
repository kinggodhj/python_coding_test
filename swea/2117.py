cost=[0]*41
cost[0]=0
cost[1]=1
for i in range(2, 41):
    cost[i]=cost[i-1]+(i-1)*4
T=int(input().rstrip())
answer=[]
for test_case in range(T):
    N, M=map(int, input().rstrip().split(' '))
    array=[]
    city=0
    for i in range(N):
        tmp=list(map(int, input().rstrip().split(' ')))
        array.append(tmp)
        for j in range(N):
            if tmp[j]==1:
                city+=1
    budget=city*M
    max_k=0
    for i in range(1, 40):
        if cost[i]<=budget<cost[i+1]:
            max_k=i
    
    def check(k):        
        count=0
        for i in range(N):
            for j in range(N):
                tmp=0
                if array[i][j]==1:
                    tmp+=1
                ny1=j+1
                ny2=j-1
                for _ in range(k-1):
                    if 0<=ny1<N:
                        if array[i][ny1]==1:
                            tmp+=1
                    if 0<=ny2<N:
                        if array[i][ny2]==1:
                            tmp+=1
                    ny1+=1
                    ny2-=1
                for step in range(1, k):
                    x1=i-step
                    x2=i+step
                    if 0<=x1<N:
                        if array[x1][j]==1:
                            tmp+=1
                    if 0<=x2<N:
                        if array[x2][j]==1:
                            tmp+=1
                    y1=j
                    y2=j    
                    for t in range(k-1-step):
                        y1+=1
                        y2-=1
                        if 0<=x1<N and 0<=y1<N: 
                            if array[x1][y1]==1:
                                tmp+=1
                        if 0<=x1<N and 0<=y2<N: 
                            if array[x1][y2]==1:
                                tmp+=1
                        if 0<=x2<N and 0<=y1<N: 
                            if array[x2][y1]==1:
                                tmp+=1
                        if 0<=x2<N and 0<=y2<N: 
                            if array[x2][y2]==1:
                                tmp+=1    
                if tmp>count:
                    count=tmp
        return count

    while(max_k>0):
        num_house=check(max_k)
        if cost[max_k]>num_house*M:
            max_k-=1
        else:
            answer.append(num_house)
            break

for t in range(T):
    print('#%d %d'%(t+1, answer[t]))