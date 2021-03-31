T=int(input().rstrip())
dir={1:2, 2:1, 3:4, 4:3}
df={1:[-1,0], 2:[1,0], 3:[0,-1], 4:[0,1]}

test=[]
for test_case in range(T):
    N, M, K=map(int, input().rstrip().split(' '))
    virus=[list(map(int, input().rstrip().split(' '))) for _ in range(K)]
    array=[[0]*N for _ in range(N)]
    for i in range(len(virus)):
        x, y, num, d=virus[i]
        array[x][y]=num

    def move(arr):
        global virus
        result=[[0]*N for _ in range(N)]
        for i in range(len(virus)):
            x, y, num, d=virus[i]
            if num==0:
                continue
            dx, dy=df[d]
            if x+dx==0 or x+dx==N-1 or y+dy==0 or y+dy==N-1:
                virus[i]=[x+dx, y+dy, num//2, dir[d]]
                result[x+dx][y+dy]+=num//2
            else:
                if 0<x+dx<N-1 and 0<y+dy<N-1:
                    virus[i]=[x+dx, y+dy, num, d]
                    result[x+dx][y+dy]+=num
        return result
    
    def concat():
        global virus
        virus.sort(key=lambda x:[int(x[0]), int(x[1])])
        s=0
        while(s<len(virus)):
            px, py, pnum, pd=virus[s]
            tmp=[[virus[s][2], virus[s][3]]]
            i=s
            if i==len(virus)-1:
                break
            while(virus[i+1][0]==px and virus[i+1][1]==py):
                tmp.append([virus[i+1][2], virus[i+1][3]])
                pnum+=virus[i+1][2]
                i+=1
                if i==len(virus)-1:
                    break
            if len(tmp)>1:
                tmp.sort(reverse=True)
                d=tmp[0][-1]
                virus[s][2]=pnum
                virus[s][3]=d
                for t in range(s+1, i+1):
                    virus[t][2]=0
                    virus[t][3]=d
                s=i+1
            else:
                s+=1
    time=0
    while(time<M):
        array=move(array)
        concat()
        time+=1
    answer=0
    for arr in array:
        answer+=sum(arr)
    test.append(answer)

for t in range(T):
    print('#%d %d'%(t+1, test[t]))