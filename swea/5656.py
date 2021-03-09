import copy
from collections import deque

T=int(input())
INF=int(1e9)
queue=deque([])

def remove(start, area, W, H):
    queue.appendleft(start)
    dx=[-1, 1, 0, 0]
    dy=[ 0, 0, -1, 1]
    check=[[0]*W for _ in range(H)]
    while queue:
        x,y=queue.pop()
        value=area[x][y]
        area[x][y]=0
        check[x][y]=1
        if value>1:
            for i in range(1, value):
                case_x=list(map(lambda x:x*i, dx))
                case_y=list(map(lambda x:x*i, dy))
                for d in range(4):
                    if 0<=x+case_x[d]<H and 0<=y+case_y[d]<W:
                        if area[x+case_x[d]][y+case_y[d]]==1:
                            area[x+case_x[d]][y+case_y[d]]=0
                        elif area[x+case_x[d]][y+case_y[d]]>1 and check[x+case_x[d]][y+case_y[d]]==0:
                            queue.appendleft([x+case_x[d], y+case_y[d]])
    return area

def whiteSpace(area, W, H):
    total=0
    for j in range(W):
        num=[]
        for i in range(H):
            if area[i][j]!=0:
                num.append(area[i][j])
                area[i][j]=0
                total+=1
        if len(num)>0:
            for i in range(H-1, H-1-len(num), -1):
                area[i][j]=num.pop()
    return total, area

def comb(count, max_count, lst):
    ans=[]
    if count==max_count:
        return [lst]
    else:
        for num1 in range(W):
            ans.extend(comb(count+1, max_count, lst+[num1]))
    return ans

for test_case in range(1, T+1):
    N,W,H=map(int, input().rstrip().split(' '))
    array=[list(map(int, input().rstrip().split(' '))) for _ in range(H)]
    result=[]
    marvel=comb(0, N, [])
    check=False
    one=INF
    for m in marvel:
        this=copy.deepcopy(array)
        for m_idx in m:
            for i in range(H):
                if this[i][m_idx]!=0:
                    this=remove([i, m_idx], this, W, H)
                    one, this=whiteSpace(this, W, H)
                    check=True
                    break
        if one!=INF and one>=0:
            result.append(one)
            if one==0:
                break

    if check==False:
        print('#%d 0'%(test_case))
    else:
        print('#%d %d'%(test_case,min(result)))