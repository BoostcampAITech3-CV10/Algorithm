import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    g = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(g)-1):
        if i%2==1:
            graph[g[0]].append([g[i],g[i+1]])
            
def BFS(v):
    max_val = 0
    visit = [0]*(n+1)
    total = [0]*(n+1)
    q = deque([v])
    visit[v] = 1
    while q:
        v = q.popleft()
        for i,cost in graph[v]:
            if visit[i]==0:
                q.append(i)
                visit[i]=1
                total[i] = total[v] + cost
    for i in total:
        if i>max_val:
            max_val = i
    return total.index(max(total)), max(total)

start = BFS(1)[0]
answer = BFS(start)[1]
print(answer)



