import sys
import heapq
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
start, end = map(int,input().split())
distance = [1e9]*(N+1)
distance[start] = 0
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
dik(start)
print(distance[end])
