import itertools
import sys
import operator

arr=[i for i in range(9)]
arr.remove(0)

N=int(sys.stdin.readline())
order=[list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

permute=[]
for i in list(itertools.permutations(arr, 8)):
    tmp=list(i)
    tmp.insert(3, 0)
    permute.append(tmp)

result=[0]*len(permute)
for i in range(len(permute)):
    sorted_game=[]
    for game in range(N):
        tmp=[]
        for idx, sort_idx in enumerate(permute[i]):
            tmp.append(order[game][sort_idx])
        sorted_game.append(tmp)
    whole_v=0
    next_player=0
    for game in range(N):
        cnt=0
        value=0
        base=[]
        for player in range(next_player, 9*4):
            if cnt==3:
                next_player=player%9
                break
            if sorted_game[game][player%9]==0:
                cnt+=1
            else:
                if base:
                    base=list(map(operator.add, [sorted_game[game][player%9]]*len(base), base))
                base.append(sorted_game[game][player%9])
        for v in range(len(base)):
            if base[v]>3:
                value+=1
        whole_v+=value
    result[i]=whole_v

print(max(result))
#print(sorted(range(len(result)), key=lambda k: result[k]))