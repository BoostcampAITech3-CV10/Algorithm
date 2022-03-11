import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
t = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
party = []
for _ in range(m):
    p = list(map(int,sys.stdin.readline().split()))[1:]
    party.append(p)
    for i in p:
        for j in p:
            if i!=j:
                if j not in graph[i]:
                    graph[i].append(j)
                if i not in graph[j]:
                    graph[j].append(i)

if t[0] == 0:
    print(m)
else:
    answer = 0
    truth = t[1:]
    new=[]
    for v in truth:
        visit = [0]*(n+1)
        q = deque([v])
        visit[v] = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if visit[i]==0:
                    q.append(i)
                    visit[i]=1
                    new.append(i)
    truth.extend(list(set(new)))
    for p in party:
        temp = True
        for i in p:
            if i in truth:
                temp = False
                break
        if temp:
            answer += 1
    print(answer)