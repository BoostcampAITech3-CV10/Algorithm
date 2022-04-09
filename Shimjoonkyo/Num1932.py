import sys
n = int(input())
dp=[]
for _ in range(n):
    tree = list(map(int,sys.stdin.readline().split()))
    while len(tree)<n:
        tree.append(0)
    tree = [0] + tree
    dp.append(tree)

for i in range(1,n):
    for j in range(1,i+2):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + dp[i][j]
print(max(dp[n-1]))
