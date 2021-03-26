import copy
N=int(input().rstrip())
array=[list(map(int, input().rstrip().split(' '))) for _ in range(N)]
max_v=0

def up(arr):
    for j in range(N):
        tmp=[]
        i=0
        while(i<N-1):
            if arr[i][j]!=0:
                value=arr[i][j]
                i+=1
                while(arr[i][j]==0):
                    i+=1
                    if i>N-1:
                        tmp.append(value)
                        break
                if i>N-1:
                    break
                if arr[i][j]!=value:
                    tmp.append(value)
                    if i==N-1:
                        tmp.append(arr[i][j])
                else:
                    tmp.append(value*2)
                    i+=1
                    if i==N-1:
                        tmp.append(arr[i][j])
            else:
                i+=1
                if i==N-1 and arr[i][j]!=0:
                    tmp.append(arr[i][j])
        if len(tmp)>0:
            for i in range(N):
                if i<len(tmp):
                    arr[i][j]=tmp[i]
                else:
                    arr[i][j]=0
    return arr

def down(arr):
    for j in range(N):
        tmp=[]
        i=N-1
        while(i>0):
            if arr[i][j]!=0:
                value=arr[i][j]
                i-=1
                while(arr[i][j]==0):
                    i-=1
                    if i<0:
                        tmp.append(value)
                        break
                if i<0:
                    break
                if arr[i][j]!=value:
                    tmp.append(value)
                    if i==0:
                        tmp.append(arr[i][j])
                else:
                    tmp.append(value*2)
                    i-=1
                    if i==0:
                        tmp.append(arr[i][j])
            else:
                i-=1
                if i==0 and arr[i][j]!=0:
                    tmp.append(arr[i][j])
        if len(tmp)>0:
            for i in range(N-1, -1, -1):
                if i<len(tmp):
                    arr[N-1-i][j]=tmp[i]
                else:
                    arr[N-1-i][j]=0
    return arr

def left(arr):
    for i in range(N):
        tmp=[]
        j=0
        while(j<N-1):
            if arr[i][j]!=0:
                value=arr[i][j]
                j+=1
                while(arr[i][j]==0):
                    j+=1
                    if j>N-1:
                        tmp.append(value)
                        break
                if j>N-1:
                    break
                if arr[i][j]!=value:
                    tmp.append(value)
                    if j==N-1:
                        tmp.append(arr[i][j])
                else:
                    tmp.append(value*2)
                    j+=1
                    if j==N-1:
                        tmp.append(arr[i][j])
            else:
                j+=1
                if j==N-1 and arr[i][j]!=0:
                    tmp.append(arr[i][j])
        if len(tmp)>0:
            for j in range(N):
                if j<len(tmp):
                    arr[i][j]=tmp[j]
                else:
                    arr[i][j]=0
    return arr

def right(arr):
    for i in range(N):
        tmp=[]
        j=N-1
        while(j>0):
            if arr[i][j]!=0:
                value=arr[i][j]
                j-=1
                while(arr[i][j]==0):
                    j-=1
                    if j<0:
                        tmp.append(value)
                        break
                if j<0:
                    break
                if arr[i][j]!=value:
                    tmp.append(value)
                    if j==0:
                        tmp.append(arr[i][j])
                else:
                    tmp.append(value*2)
                    j-=1
                    if j==0:
                        tmp.append(arr[i][j])
            else:
                j-=1
                if j==0 and arr[i][j]!=0:
                    tmp.append(arr[i][j])
        if len(tmp)>0:
            for j in range(N-1, -1, -1):
                if j<len(tmp):
                    arr[i][N-1-j]=tmp[j]
                else:
                    arr[i][N-1-j]=0
    return arr

def case(lst):
    global max_v
    if len(lst)==5:
        new=copy.deepcopy(array)
        for l in lst:
            if l==0:
                new=up(new)
            elif l==1:
                new=down(new)
            elif l==2:
                new=left(new)
            elif l==3:
                new=right(new)
        for row in new:
            if max_v<max(row):
                max_v=max(row)
    else:
        for i in range(4):
            case(lst+[i])

case([])
print(max_v)            