import sys

N, L = map(int, sys.stdin.readline().split(' '))

road=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

count=0
for arr in road:
    check=True
    check_l=True
    pivot=0
    use_L=[0]*N
    for col in range(1, N):
        if arr[col]!=arr[pivot]:
            if abs(arr[pivot]-arr[col])==1:
                check=False
                if arr[pivot]>arr[col]:
                    if use_L[col]==1:
                        check_l=False
                        break
                    else:
                        use_L[col]=1
                        for l in range(1, L):
                            if col+l<N and arr[col]==arr[col+l] and use_L[col+l]==0:
                                check_l=True
                                use_L[col+l]=1
                            else:
                                use_L=[0]*N
                                check_l=False
                                break
                        if check_l==True:
                            if col+(L-1)<N:  
                                pivot=col
                                check=True
                            else:
                                break
                        else:
                            break
                else:
                    if use_L[pivot]==1:
                        check_l=False
                        break
                    else:
                        use_L[pivot]=1
                        for l in range(1, L):
                            if pivot-l>=0 and arr[pivot]==arr[pivot-l] and use_L[pivot-l]==0:
                                check_l=True
                                use_L[pivot-l]=1
                            else:
                                use_L=[0]*N
                                check_l=False
                                break
                        if check_l==True: 
                            if 0<=pivot-(L-1):  
                                pivot=col
                                check=True
                            else:
                                break
                        else:
                            break
            else:
                check=False
                break
        else:
            pivot=col
    if check==True:
        count+=1

for col in range(N):
    check=True
    check_l=True
    pivot=0
    use_L=[0]*N
    for row in range(1, N):
        if road[row][col]!=road[pivot][col]:
            if abs(road[pivot][col]-road[row][col])==1:
                check=False
                if road[pivot][col]>road[row][col]:
                    if use_L[row]==1:
                        check_l=False
                        break
                    else:
                        use_L[row]=1
                        for l in range(1, L):
                            if row+l<N and road[row][col]==road[row+l][col] and use_L[row+l]==0:
                                check_l=True
                                use_L[row+l]=1
                            else:
                                use_L=[0]*N
                                check_l=False
                                break
                        if check_l==True:
                            if row+(L-1)<N:
                                check=True
                                pivot=row
                            else:
                                break
                        else:
                            break
                else:
                    if use_L[pivot]==1:
                        check_l=False
                        break
                    else:
                        use_L[pivot]=1
                        for l in range(1, L):
                            if pivot-l>=0 and road[pivot][col]==road[pivot-l][col] and use_L[pivot-l]==0:
                                check_l=True
                                use_L[pivot-l]=1
                            else:
                                use_L=[0]*N
                                check_l=False
                                break
                        if check_l==True:
                            if 0<=pivot-(L-1):  
                                check=True
                                pivot=row
                            else:
                                break
                        else:
                            break
            else:
                check=False
                break
        else:
            pivot=row
    if check==True:
        count+=1

print(count)