import heapq
import sys

INF=int(1e9)
n, m=map(int, sys.stdin.readline().split(' '))
start=int(sys.stdin.readline())

graph=[[] for _ in range(n)]
distance=[INF]*(n+1)

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split(' '))
    graph[a].append((b, c))

def dijstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dis, now=heapq.heappop(q)
        if distance[now]<dis:
            continue
        for next_info in graph[now]:
            cost=dis+next_info[1]
            if cost<distance[next_info[0]]:
                distance[next_info[0]]=cost
                heapq.heappush(q, (cost, next_info[0]))




















