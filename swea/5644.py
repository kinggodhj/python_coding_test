T=int(input().rstrip())
move={0:[0,0], 1:[0,-1], 2:[1,0], 3:[0,1], 4:[-1,0]}
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for t in range(1, T+1):
    M, A=map(int, input().rstrip().split(' '))
    A_coord=[0]
    B_coord=[0]
    A_coord.extend(list(map(int, input().rstrip().split(' '))))
    B_coord.extend(list(map(int, input().rstrip().split(' '))))
    AP=[list(map(int, input().split(' '))) for _ in range(A)]
    map_info=[[0]*10 for _ in range(10)]

    for a in range(A):
        x=AP[a][0]-1
        y=AP[a][1]-1
        c=AP[a][2]
        p=AP[a][3]
        tmp_x=[]
        tmp_y=[]
        for j in range(c+1):
            for i in range(c-j, -1, -1):
                if 0<=x-i<10 and 0<=y-j<10:
                    if map_info[y-j][x-i]==0:
                        map_info[y-j][x-i]=[a]
                    else:
                        if map_info[y-j][x-i][-1]!=a:
                            map_info[y-j][x-i].extend([a])
                if 0<=x+i<10 and 0<=y-j<10:
                    if map_info[y-j][x+i]==0:
                        map_info[y-j][x+i]=[a]
                    else:
                        if map_info[y-j][x+i][-1]!=a:
                            map_info[y-j][x+i].extend([a])
                if j!=0:
                    if 0<=x-i<10 and 0<=y+j<10:
                        if map_info[y+j][x-i]==0:
                            map_info[y+j][x-i]=[a]
                        else:
                            if map_info[y+j][x-i][-1]!=a:
                                map_info[y+j][x-i].extend([a])
                    if 0<=x+i<10 and 0<=y+j<10:
                        if map_info[y+j][x+i]==0:
                            map_info[y+j][x+i]=[a]
                        else:
                            if map_info[y+j][x+i][-1]!=a:
                                map_info[y+j][x+i].extend([a])

    ax=0 
    ay=0
    bx=9
    by=9
    result=[]
    result_A=[]
    result_B=[]
    for coord in range(len(A_coord)):
        A_case=[]
        B_case=[]
        if 0<=ax+move[A_coord[coord]][0]<10 and 0<=ay+move[A_coord[coord]][1]<10:
            ax+=move[A_coord[coord]][0]
            ay+=move[A_coord[coord]][1]
            if map_info[ay][ax]!=0:
                A_case.extend(map_info[ay][ax])
        if 0<=bx+move[B_coord[coord]][0]<10 and 0<=by+move[B_coord[coord]][1]<10:
            bx+=move[B_coord[coord]][0]
            by+=move[B_coord[coord]][1]
            if map_info[by][bx]!=0:
                B_case.extend(map_info[by][bx])
        if len(A_case)>0 and len(B_case)>0:
            value=[[0]*len(B_case) for _ in range(len(A_case))]
            value_A=[]
            value_B=[]
            
            for i in range(len(A_case)):
                for j in range(len(B_case)):
                    if A_case[i]==B_case[j]:
                        value_A.append((AP[A_case[i]][3])//2)
                        value_B.append((AP[B_case[j]][3])//2)
                    else:
                        value_A.append(AP[A_case[i]][3])
                        value_B.append(AP[B_case[j]][3])
            count=0
            idx=0
            max_v=-1*int(1e9)
            for a,b in zip(value_A, value_B):
                if max_v<a+b:
                    max_v=a+b
                    idx=count
                count+=1   
            result_A.append(value_A[idx])
            result_B.append(value_B[idx])
        elif len(A_case)>0 and len(B_case)==0:
            value=[]
            for i in A_case:
                value.append(AP[i][3])
            result_A.append(max(value))
            result_B.append(0)
        elif len(A_case)==0 and len(B_case)>0:
            value=[]
            for i in B_case:
                value.append(AP[i][3])
            result_A.append(0)
            result_B.append(max(value))
        else:
            result_A.append(0)
            result_B.append(0)
    print("#%s %d"%(t, sum(result_A)+sum(result_B)))