import sys
import heapq
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int,input().split())

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

ans1 = 0
visit1=[1,v1,v2,n]
for i in range(3):
    distance = [1e9]*(n+1)
    dik(visit1[i])
    ans1 += distance[visit1[i+1]]

ans2 = 0
visit2=[1,v2,v1,n]
for i in range(3):
    distance = [1e9]*(n+1)
    dik(visit2[i])
    ans2 += distance[visit2[i+1]]
    
val = min(ans1,ans2)
if val >= 1e9:
    print(-1)
else:
    print(val)
