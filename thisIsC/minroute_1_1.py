import heapq

n=int(input())
m=int(input())
INF=int(1e9)

graph=[[INF]*(n) for _ in range(n)]
for a in range(n):
    for b in range(n):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a, b, c=map(int, input().split(' '))
    if c<graph[a-1][b-1]:
        graph[a-1][b-1]=c

def floyd(graph):
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
    
    return graph

graph=floyd(graph)
for row in graph:
    for r in row:
        print(r, end=' ')
    print('')