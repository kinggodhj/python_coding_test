import sys

ans=[]
T=int(sys.stdin.readline())
for t in range(T):
    n, m=map(int, sys.stdin.readline().split(' '))
    idx=[-1-m, -1, m-1]
    golds=list(map(int, sys.stdin.readline().split(' ')))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    for col in range(1, m):
        for row in range(0,  n*m, m):
            tmp=0
            for i in idx:
                if 0<=row+col+i<n*m:
                    tmp=max(golds[row+col+i], tmp)
            golds[row+col]=golds[row+col]+tmp
    ans.append(max(golds))   

for a in ans:
    print(a)    