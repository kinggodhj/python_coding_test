T=int(input().rstrip())

def rotate_right(x, dir, array):
    global case
    if x+1<4:
        if array[x][2]!=array[x+1][6]:
            case.append([x+1, -1*dir])
            rotate_right(x+1, -1*dir, array)

def rotate_left(x, dir, array):
    global case
    if 0<=x-1:
        if array[x][6]!=array[x-1][2]:
            case.append([x-1, -1*dir])
            rotate_left(x-1, -1*dir, array)

def rotate(r_case, array):
    for rc in r_case:
        idx=rc[0]
        d=rc[1]
        if d==1:
            tmp=array[idx].pop()
            array[idx].insert(0, tmp)
        elif d==-1:
            array[idx].append(array[idx][0])
            array[idx]=array[idx][1:]

for test_case in range(1, T+1):
    K=int(input().rstrip())
    blades=[list(map(int, input().rstrip().split(' '))) for _ in range(4)]
    rotation=[]
    for k in range(K):
        one, two=map(int, input().rstrip().split(' '))
        rotation.append([one-1, two])
    for rr in rotation:
        case=[]
        rotate_right(rr[0], rr[1], blades)
        rotate_left(rr[0], rr[1], blades)
        if len(case)>0:
            rotate(case, blades)
        rotate([rr], blades)
    value=0
    for b in range(4): 
        if blades[b][0]==1:
            value+=2**(b)
    print("#%d %d"%(test_case, value))