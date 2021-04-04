wheels=[list(map(int, input().rstrip())) for _ in range(4)]
K=int(input().rstrip())
rotate=[]
for _ in range(K):
    i, r=map(int, input().rstrip().split(' '))
    rotate.append([i-1, r])

for i, d in rotate:
    case=[[i, d]]
    left=wheels[i][6]
    right=wheels[i][2]
    idx=i
    nd=d
    while(idx-1>=0):
        if left!=wheels[idx-1][2]:
            case.append([idx-1, -1*nd])
            left=wheels[idx-1][6]
            nd*=-1
            idx-=1
        else:
            break
    idx=i
    nd=d
    while(idx+1<4):
        if right!=wheels[idx+1][6]:
            case.append([idx+1, -1*nd])
            right=wheels[idx+1][2]
            nd*=-1
            idx+=1
        else:
            break
    
    for w, r in case:
        if r==1:
            wheels[w]=[wheels[w][-1]]+wheels[w][0:-1]
        elif r==-1:
            wheels[w]=wheels[w][1:]+[wheels[w][0]]

answer=0
for i in range(4):
    if wheels[i][0]==1:
        answer+=1*(2**i)

print(answer)