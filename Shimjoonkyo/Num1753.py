import sys
import heapq
V,E = map(int,input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
distance = [1e9]*(V+1)
distance[k] = 0
def dik(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
dik(k)
for i in distance[1:]:
    if i==1e9:
        print('INF')
    else:
        print(i)
