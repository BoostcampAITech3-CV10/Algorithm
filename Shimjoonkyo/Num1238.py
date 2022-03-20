import sys
import heapq
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((e,t))

distance = [1e9]*(n+1)
max_val=0
def dik(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dik(x)
away = distance
for i in range(1,n+1):
    distance = [1e9]*(n+1)
    dik(i)
    val = away[i] + distance[x]
    if val > max_val:
        max_val = val
print(max_val)
