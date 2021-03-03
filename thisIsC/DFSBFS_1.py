from collections import defaultdict
from collections import deque

N, M, K, X =map(int, input().split(' '))
Node_dic=defaultdict(list)

for _ in range(M):
    node, dest=map(int, input().split(' '))
    Node_dic[node].append(dest)

check=[0]*(N+1)

def bfs(start, check, K):
    queue=deque([])
    queue.append([start, 0])
    check[start]=1
    result=[]
    while queue:
        node, length=queue.popleft()
        if length<K:
            for next_node in Node_dic[node]:
                if check[next_node]==0:
                    queue.append([next_node, length+1])
                    check[next_node]=1
        elif length==K:
            result.append(node)
    return result

res=bfs(X, check, K)
if len(res)>0:    
    res.sort()
    for r in res:
        print(r)
else:
    print(-1)