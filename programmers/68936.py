zero=0
one=0
def compress(x, y, n, arr):
    global zero, one
    tmp=0
    if n==1:
        if arr[x][y]==1:
            one+=1
        else:
            zero+=1
    else:
        for i in range(x, x+n):
            tmp+=sum(arr[i][y:y+n])
        if tmp==0:
            zero+=1
        elif tmp==n*n:
            one+=1
        else:
            compress(x, y, n//2, arr)
            compress(x+n//2, y, n//2, arr)
            compress(x, y+n//2, n//2, arr)
            compress(x+n//2, y+n//2, n//2, arr)
def solution(arr):
    global zero, one
    compress(0, 0, len(arr), arr)
    return [zero, one]

#solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
#solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])