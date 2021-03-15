N=int(input().rstrip())
array=[[0]*N]
for _ in range(N):
    array.append([0]+list(map(int, input().rstrip().split(' '))))

def G(x, y, d1, d2, check, count):
    num=[0]*5
    for r in range(1, N+1):
        for c in range(1, N+1):
            if check[r][c]!=0:
                continue
            if 1<=r<x+d1 and 1<=c<=y:
                check[r][c]=1
                count[0]+=array[r][c]
                num[0]+=1
            elif 1<=r<=x+d2 and y<c<=N:
                check[r][c]=2
                count[1]+=array[r][c]
                num[1]+=1
            elif x+d1<=r<=N and 1<=c<y-d1+d2:
                check[r][c]=3
                count[2]+=array[r][c]
                num[2]+=1
            elif x+d2<r<=N and y-d1+d2<=c<=N:
                check[r][c]=4
                count[3]+=array[r][c]
                num[3]+=1
    return count, num, check

def G5(x, y, d1, d2, check):
    count=0
    num=0
    for d in range(d1+1):
        r=x+d
        for c in range(y-d, y+1):
            if check[r][c]!=0:
                continue
            check[r][c]=5
            count+=array[r][c]
            num+=1
    
    for d in range(d1+1):
        r=x+d2+d
        for c in range(y+d2-d1, y+d2-d+1): 
            if check[r][c]!=0:
                continue
            check[r][c]=5
            count+=array[r][c]
            num+=1

    for d in range(d2+1):
        r=x+d
        for c in range(y, y+d+1):
            if check[r][c]!=0:
                continue
            check[r][c]=5
            count+=array[r][c]
            num+=1
    for d in range(d2+1):
        r=x+d1+d
        for c in range(y-d1+d, y-d1+d2+1):
            if check[r][c]!=0:
                continue
            check[r][c]=5
            count+=array[r][c]
            num+=1

    return count, num, check
                  
def find(x,y,d1,d2):                  
    check=[[0]*(N+1) for _ in range(N+1)]
    count=[0]*5
    g, g5_num, check=G5(x, y, d1, d2, check)
    count[4]=g
    count, num, check=G(x, y, d1, d2, check, count)
    num[4]=g5_num
    if 0 in num:
        return int(1e9)
    min_v=min(count)
    max_v=max(count)
    return(max_v-min_v)

answer=int(1e9)
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1<=x<x+d1+d2<=N and 1<=y-d1<y<y+d2<=N:
                    tmp=find(x,y,d1,d2)
                    answer=min(answer, tmp)
print(answer)