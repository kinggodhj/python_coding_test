import sys
from itertools import product
from itertools import combinations
import copy

N, M=map(int, sys.stdin.readline().split(' '))
work=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

case=[([1],[2],[3],[4]), ([1,2],[3,4]), ([1,4], [2,4], [2,3], [1,3]), ([1,2,3],[1,2,4],[1,3,4], [2,3,4]), ([1,2,3,4])]

def up(x, y, array, zero):
    x-=1
    while(0<=x):
        if array[x][y]==0:
            array[x][y]='#'
            zero-=1
            x-=1
        elif array[x][y]==6:
            break
        else:
            x-=1
    return array, zero

def down(x, y, array, zero):
    x+=1
    while(x<N):
        if array[x][y]==0:
            array[x][y]='#'
            zero-=1
            x+=1
        elif array[x][y]==6:
            break
        else:
            x+=1
    return array, zero

def left(x, y, array, zero):
    y-=1
    while(0<=y):
        if array[x][y]==0:
            array[x][y]='#'
            zero-=1
            y-=1
        elif array[x][y]==6:
            break
        else:
            y-=1
    return array, zero

def right(x, y, array, zero):
    y+=1
    while(y<M):
        if array[x][y]==0:
            array[x][y]='#'
            zero-=1
            y+=1
        elif array[x][y]==6:
            break
        else:
            y+=1
    return array, zero

def dir_case(dir, x, y, area, zero):
    if dir==1:
        return up(x, y, area, zero)
    elif dir==2:
        return down(x, y, area, zero)
    elif dir==3:
        return left(x, y, area, zero)
    else:
        return right(x, y, area, zero)

def find_area(area, case, cctv_list, zero):
    for i in range(len(cctv_list)):
        x=cctv_list[i][0]
        y=cctv_list[i][1]
        if area[x][y]!=5:
            c=case[i]
            for _ in range(len(c)):
                for cc in c[_]:
                    area, zero=dir_case(cc, x, y, area, zero)
        else:
            area,zero=right(x, y, area, zero)
            area,zero=left(x, y, area, zero)
            area,zero=up(x, y, area, zero)
            area,zero=down(x, y, area, zero)
    return area, zero

cctv=[]
five=[]
zero=0
com_case=[]
for row in range(N):
    for col in range(M):
        if work[row][col]==0:
            zero+=1
        elif work[row][col]==5:
            five.append([row, col])
        elif work[row][col]!=6:
            cctv.append([row, col])
            com_case.append(list(combinations(case[work[row][col]-1], 1)))

result=[]
whole=list(product(*com_case))
if len(five)>0:
        work, zero=find_area(work, case, five, zero)
for w in whole:
    tmp=zero
    _, tmp=find_area(copy.deepcopy(work), w, cctv, tmp)
    result.append(tmp)
print(min(result))