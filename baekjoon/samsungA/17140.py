r,c,k=map(int, input().rstrip().split(' '))
r-=1
c-=1
array=[[int(1e9)]*101 for _ in range(101)]
for _ in range(3):
    array[_][0], array[_][1], array[_][2]=map(int, input().rstrip().split(' '))

row=3
col=3
def R_operation():
    global col
    for i in range(100):
        tmp=0
        count=[int(1e9)]*101
        for j in range(100):
            if array[i][j]==int(1e9):
                break
            if array[i][j]==0:
                continue
            if count[array[i][j]]==int(1e9):
                count[array[i][j]]=1
                tmp+=1
            else:
                count[array[i][j]]+=1
            array[i][j]=0
            
        col=max(col, tmp*2)
        col=min(col, 100)
        next_arr=[x for x in sorted(enumerate(count), key=lambda x:x[1])]
        for idx in range(50):
            if next_arr[idx][1]==int(1e9):
                break
            else:
                array[i][idx*2]=next_arr[idx][0]
                array[i][idx*2+1]=next_arr[idx][1]

def C_operation():
    global row
    for j in range(100):
        tmp=0
        count=[int(1e9)]*101
        for i in range(100):
            if array[i][j]==int(1e9):
                break
            if array[i][j]==0:
                continue
            if count[array[i][j]]==int(1e9):
                count[array[i][j]]=1
                tmp+=1
            else:
                count[array[i][j]]+=1
            array[i][j]=0
        row=max(row, tmp*2)
        row=min(row, 100)
        next_arr=[x for x in sorted(enumerate(count), key=lambda x:x[1])]
        for idx in range(50):
            if next_arr[idx][1]==int(1e9):
                break
            else:
                array[idx*2][j]=next_arr[idx][0]
                array[idx*2+1][j]=next_arr[idx][1]
time=0
while(time<=100):
    if array[r][c]==k:
        print(time)
        exit(0)
    elif time==100 and array[r][c]!=k:
        print('-1')
        exit(0)
    if row>=col:
        R_operation()
        for i in range(row):
            for j in range(col):
                if array[i][j]==int(1e9):
                    array[i][j]=0
    else:
        C_operation()
        for j in range(col):
            for i in range(row):
                if array[i][j]==int(1e9):
                    array[i][j]=0
    time+=1