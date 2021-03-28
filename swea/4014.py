T=int(input().rstrip())
a=[]
for test_case in range(T):  
    N, x=map(int, input().rstrip().split(' '))
    answer=N*2
    array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    def rowslope(i, j, x, N, arr):
        global answer
        k=1
        while(k<x):
            if j+k>=N:
                answer-=1
                return False
            if arr[i][j+k]!=arr[i][j]:
                answer-=1
                return False
            else:
                k+=1
        j=j+x-1
        if j+1<N:
            if arr[i][j]!=arr[i][j+1]:
                if arr[i][j]<arr[i][j+1]:
                    answer-=1
                    return False
                else:
                    if abs(arr[i][j]-arr[i][j+1]==1):
                        return True
                    else:
                        answer-=1
                        return False
            else:
                return True 
        else:
            return True

    def colslope(i, j, x, N, arr):
        global answer
        k=1
        while(k<x):
            if i+k>=N:
                answer-=1
                return False
            if arr[i+k][j]!=arr[i][j]:
                answer-=1
                return False
            else:
                k+=1
        i=i+x-1
        if i+1<N:
            if arr[i][j]!=arr[i+1][j]:
                if arr[i][j]<arr[i+1][j]:
                    answer-=1 
                    return False
                else:
                    if abs(arr[i][j]-arr[i+1][j]==1):
                        return True
                    else:
                        answer-=1
                        return False
            else:
                return True 
        else:
            return True

    for i in range(N):
        pivot=array[i][0]
        idx=0
        c=None
        for j in range(1,N):
            if idx>j:
                continue
            if pivot==array[i][j]:
                continue
            if abs(pivot-array[i][j])>1:
                answer-=1
                break
            if pivot>array[i][j]:
                c=rowslope(i, j, x, N, array) 
                if c==False:
                    break
                if j+x==N:
                    break
                if array[i][j+x-1]==array[i][j+x]:
                    pivot=array[i][j+x]
                    idx=j+x
                else:
                    pivot=array[i][j+x-1]
                    idx=j+x-1
            elif pivot<array[i][j]:
                if j-idx<x:
                    answer-=1
                    break
                else:
                    pivot=array[i][j]
                    idx=j

    for j in range(N):
        pivot=array[0][j]
        idx=0
        for i in range(1,N):
            if idx>i:
                continue
            if pivot==array[i][j]:
                continue
            if abs(pivot-array[i][j])>1:
                answer-=1
                break
            if pivot>array[i][j]:
                c=colslope(i, j, x, N, array) 
                if c==False:
                    break
                if i+x==N:
                    break
                if array[i+x-1][j]==array[i+x][j]:
                    pivot=array[i+x][j]
                    idx=i+x
                else:
                    pivot=array[i+x-1][j]
                    idx=i+x-1
            elif pivot<array[i][j]:
                if i-idx<x:
                    answer-=1
                    break
                else:
                    pivot=array[i][j]
                    idx=i
    a.append(answer)

for t in range(T):
    print('#%d %d'%(t+1, a[t]))