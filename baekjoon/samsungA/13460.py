import copy
N, M=map(int, input().rstrip().split(' '))
array=[]
min_time=int(1e9)
for _ in range(N):
    tmp=list(input().rstrip())
    array.append(tmp)
    for t in range(len(tmp)):
        if tmp[t]=='R':
            R_coord=[_, t]
        elif tmp[t]=='B':
            B_coord=[_, t]

def up(arr, rx, ry, bx, by):
    if ry==by:
        if rx>bx:
            i=bx
            while (arr[i-1][by])=='.':
                i-=1
            if arr[i-1][by]=='O':
                return False, None, None, None, None
            if i!=bx:
                arr[i][by]='B'
                arr[bx][by]='.'
                bx=i
            i=rx
            while (arr[i-1][ry])=='.':
                i-=1
            if arr[i-1][ry]=='O':
                return True, None, None, None, None
            if i!=rx:
                arr[i][ry]='R'
                arr[rx][ry]='.'
                rx=i
        elif rx<bx:
            check=False
            i=rx
            while (arr[i-1][ry])=='.':
                i-=1
            if arr[i-1][ry]=='O':
                check=True
                arr[rx][ry]='.'
            if i!=rx and check==False:
                arr[i][ry]='R'
                arr[rx][ry]='.'
                rx=i
            i=bx
            while (arr[i-1][by])=='.':
                i-=1
            if arr[i-1][by]=='O':
                return False, None, None, None, None
            if i!=bx:
                arr[i][by]='B'
                arr[bx][by]='.'
                bx=i
            if check==True:
                return True, None, None, None, None
    else:
        i=bx
        while (arr[i-1][by])=='.':
            i-=1
        if arr[i-1][by]=='O':
            return False, None, None, None, None
        if i!=bx:
            arr[i][by]='B'
            arr[bx][by]='.'
            bx=i
        i=rx
        while (arr[i-1][ry])=='.':
            i-=1
        if arr[i-1][ry]=='O':
            return True, None, None, None, None
        if i!=rx:
            arr[i][ry]='R'
            arr[rx][ry]='.'
            rx=i
    return arr, rx, ry, bx, by

def down(arr, rx, ry, bx, by):
    if ry==by:
        if rx<bx:
            i=bx
            while (arr[i+1][by])=='.':
                i+=1
            if arr[i+1][by]=='O':
                return False, None, None, None, None
            if i!=bx:
                arr[i][by]='B'
                arr[bx][by]='.'
                bx=i
            i=rx
            while (arr[i+1][ry])=='.':
                i+=1
            if arr[i+1][ry]=='O':
                return True, None, None, None, None
            if i!=rx:
                arr[i][ry]='R'
                arr[rx][ry]='.'
                rx=i
        elif rx>bx:
            check=False
            i=rx
            while (arr[i+1][ry])=='.':
                i+=1
            if arr[i+1][ry]=='O':
                check=True
                arr[rx][ry]='.'
            if i!=rx and check==False:
                arr[i][ry]='R'
                arr[rx][ry]='.'
                rx=i
            i=bx
            while (arr[i+1][by])=='.':
                i+=1
            if arr[i+1][by]=='O':
                return False, None, None, None, None
            if i!=bx:
                arr[i][by]='B'
                arr[bx][by]='.'
                bx=i
            if check==True:
                return True, None, None, None, None
    else:
        i=bx
        while (arr[i+1][by])=='.':
            i+=1
        if arr[i+1][by]=='O':
            return False, None, None, None, None
        if i!=bx:
            arr[i][by]='B'
            arr[bx][by]='.'
            bx=i
            
        i=rx
        while (arr[i+1][ry])=='.':
            i+=1
        if arr[i+1][ry]=='O':
            return True, None, None, None, None
        if i!=rx:
            arr[i][ry]='R'
            arr[rx][ry]='.'
            rx=i
    return arr, rx, ry, bx, by

def left(arr, rx, ry, bx, by):
    if rx==bx:
        if ry>by:
            j=by
            while (arr[bx][j-1])=='.':
                j-=1
            if arr[bx][j-1]=='O':
                return False, None, None, None, None
            if j!=by:
                arr[bx][j]='B'
                arr[bx][by]='.'
                by=j
            j=ry
            while (arr[rx][j-1])=='.':
                j-=1
            if arr[rx][j-1]=='O':
                return True, None, None, None, None
            if j!=ry:
                arr[rx][j]='R'
                arr[rx][ry]='.'
                ry=j
        elif ry<by:
            check=False
            j=ry
            while (arr[rx][j-1])=='.':
                j-=1
            if arr[rx][j-1]=='O':
                check=True
                arr[rx][ry]='.'

            if j!=ry and check==False:
                arr[rx][j]='R'
                arr[rx][ry]='.'
                ry=j
            j=by
            while (arr[bx][j-1])=='.':
                j-=1
            if arr[bx][j-1]=='O':
                return False, None, None, None, None
            if j!=by:
                arr[bx][j]='B'
                arr[bx][by]='.'
                by=j
            if check==True:
                return True, None, None, None, None
    else:
        j=by
        while (arr[bx][j-1])=='.':
            j-=1
        if arr[bx][j-1]=='O':
            return False, None, None, None, None
        if j!=by:
            arr[bx][j]='B'
            arr[bx][by]='.'
            by=j
            
        j=ry
        while (arr[rx][j-1])=='.':
            j-=1
        if arr[rx][j-1]=='O':
            return True, None, None, None, None
        if j!=ry:
            arr[rx][j]='R'
            arr[rx][ry]='.'
            ry=j
    return arr, rx, ry, bx, by

def right(arr, rx, ry, bx, by):
    if rx==bx:
        if ry<by:
            j=by
            while (arr[bx][j+1])=='.':
                j+=1
            if arr[bx][j+1]=='O':
                return False, None, None, None, None
            if j!=by:
                arr[bx][j]='B'
                arr[bx][by]='.'
                by=j
            j=ry
            while (arr[rx][j+1])=='.':
                j+=1
            if arr[rx][j+1]=='O':
                return True, None, None, None, None
            if j!=ry:
                arr[rx][j]='R'
                arr[rx][ry]='.'
                ry=j
        elif ry>by:
            check=False
            j=ry
            while (arr[rx][j+1])=='.':
                j+=1
            if arr[rx][j+1]=='O':
                check=True
                arr[rx][ry]='.'
            if j!=ry and check==False:
                arr[rx][j]='R'
                arr[rx][ry]='.'
                ry=j
            j=by
            while (arr[bx][j+1])=='.':
                j+=1
            if arr[bx][j+1]=='O':
                return False, None, None, None, None
            if j!=by:
                arr[bx][j]='B'
                arr[bx][by]='.'
                by=j
            if check==True:
                return True, None, None, None, None
    else:
        j=by
        while (arr[bx][j+1])=='.':
            j+=1
        if arr[bx][j+1]=='O':
            return False, None, None, None, None
        if j!=by:
            arr[bx][j]='B'
            arr[bx][by]='.'
            by=j
            
        j=ry
        while (arr[rx][j+1])=='.':
            j+=1
        if arr[rx][j+1]=='O':
            return True, None, None, None, None
        if j!=ry:
            arr[rx][j]='R'
            arr[rx][ry]='.'
            ry=j
    return arr, rx, ry, bx, by

def move(lst, new, rx, ry, bx, by):
    global min_time
    if type(new)!=list:
        return
    l=lst[-1]
    if l==0:
        new, rx, ry, bx, by=up(new, rx, ry, bx, by)
        if type(new)!=list and new==False:
            return None
    elif l==1:
        new, rx, ry, bx, by=down(new, rx, ry, bx, by)
        if type(new)!=list and new==False:
            return None
    elif l==2:
        new, rx, ry, bx, by=left(new, rx, ry, bx, by)
        if type(new)!=list and new==False:
            return None
    elif l==3:
        new, rx, ry, bx, by=right(new, rx, ry, bx, by)
        if type(new)!=list and new==False:
            return None
    if type(new)!=list and new==True:
        if min_time>len(lst):
            min_time=len(lst)
            print(min_time)
            exit(0)
    return [lst, new, rx, ry, bx, by]

lst=[]
result=[]
for k in range(10):
    n=len(result)
    for t in range(4):
        if n>0:
            for i in range(n):
                if lst[i][-1]==t:
                    continue
                r=move(lst[i]+[t], copy.deepcopy(result[i][0]), result[i][1], result[i][2], result[i][3], result[i][4])
                if r is not None:
                    result.append(r[1:])
                    lst.append(r[0])
        else:
            r=move([t], copy.deepcopy(array), R_coord[0], R_coord[1], B_coord[0], B_coord[1])
            if r is not None:
                result.append(r[1:])
                lst.append(r[0])
    result=result[n:]
    lst=lst[n:]
print('-1')