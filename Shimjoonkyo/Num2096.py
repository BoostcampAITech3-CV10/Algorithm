import sys
N = int(input())
li = list(map(int,sys.stdin.readline().split()))
dp1, dp2 = li, li
for _ in range(N-1):
    li = list(map(int,sys.stdin.readline().split()))
    dp1 = [li[0] + max(dp1[0],dp1[1]), li[1] + max(dp1), li[2] + max(dp1[1],dp1[2])]
    dp2 = [li[0] + min(dp2[0],dp2[1]), li[1] + min(dp2), li[2] + min(dp2[1],dp2[2])]
print(max(dp1),min(dp2))
