import sys
from collections import deque
n = int(input())
graph = [[] for _ in range(1+n)]
for _ in range(n-1):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((e,t))
    graph[e].append((s,t))
visit = [0]*(1+n)
dist = [0]*(1+n)
def BFS(v):
    visit[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        for next, d in graph[v]:
            if visit[next] == 0:
                q.append(next)
                visit[next] = 1
                dist[next] = dist[v] + d
BFS(1)
far = dist.index(max(dist))
visit = [0]*(1+n)
dist = [0]*(1+n)
BFS(far)
print(max(dist))
