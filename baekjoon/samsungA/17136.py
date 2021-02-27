import copy
import sys
from collections import deque

N=10
board=[list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

one_list=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            one_list.append([i,j])

def findpaper(board, one_list, size):
    x=one_list[0][0]
    y=one_list[0][1]
    cnt=0
    check=False
    for y_idx in range(size): #y
        for x_idx in range(size): #x 
            if 0<=x+x_idx<N and y+y_idx<N:
                if board[x+x_idx][y+y_idx]==0:
                    check=True
                    break
            else:
                check=True
                break
        if check==True:
            break
    if check==False:
        for y_idx in range(size): #y
            for x_idx in range(size): #x 
                board[x+x_idx][y+y_idx]=0
        one_list=one_list[size*size:]
        cnt+=1  
        findpaper(copy.deepcopy(board), copy.deepcopy(one_list), size-1)  
    return cnt

ss=findpaper(board, one_list)

count=0
ans=True
for i in range(len(ss)):
    if ss[i]<6:
        count+=ss[i]
    else:
        ans=False
if ans==True:
    print(count)
else:
    print(-1)