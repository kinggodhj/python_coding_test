N, M=map(int, input().rstrip().split(' '))
array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]

case=[[(1,0),(2,0),(3,0)],[(0,1), (0,2), (0,3)], [(1,0),(2,0),(2,1)], [(1,0), (0,1), (0,2)],\
    [(0,1), (1,1), (2,1)],[(1,-2), (1,-1), (1,0)], [(2,-1),(2, 0), (1, 0)], [(1,0),(0,1),(1,1)], \
    [(1,0),(1,1),(2,1)], [(1,-1),(1,0),(0,1)], [(2,-1),(1,-1),(1,0)], [(0,1),(0,2),(1,1)], \
    [(0,1),(-1,1),(1,1)], [(0,1),(0,2),(-1,1)], [(1,0),(1,1),(2,0)],\
    [(2,0),(1,0),(0,1)], [(1,2),(1,1),(1,0)], [(1,2),(1,1),(0,1)], [(1,2),(0,2),(0,1)]]

result=0
def check_array(array, x, y):
    global result
    for c in case:
        tmp=array[x][y]
        for idx in c:
            if 0<=x+idx[0]<N and 0<=y+idx[1]<M:
                array[x+idx[0]][y+idx[1]]
                tmp+=array[x+idx[0]][y+idx[1]]
            else:
                tmp=-1
                break
        result=max(result, tmp)
    return result

for i in range(N):
    for j in range(M):
        result=check_array(array, i, j)    
print(result)