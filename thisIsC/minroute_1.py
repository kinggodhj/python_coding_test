import heapq

n=int(input())
m=int(input())
INF=int(1e9)

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, input().split(' '))
    graph[a].append((b, c))

def dijkstra(start, distance):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        for city in graph[now]:
            if distance[now]<dist:
                continue
            cost=dist+city[1]
            if cost<distance[city[0]]:
                distance[city[0]]=cost
                heapq.heappush(q, (cost, city[0]))
    return distance

for node in range(1, n+1):
    distance=[INF]*(n+1)
    distance=dijkstra(node, distance)
    for i in range(1, len(distance)):
        print(distance[i], end=' ')
    print('')