N, M = map(int, input().split(' '))
coins=[int(input()) for _ in range(N)]

dp=[0]*(1000)

for c in coins:
    dp[c]=1

for i in range(coins[0], M+1):
    for c in coins:
        if i-c>=0 and i not in coins:
            if dp[i-c]!=0:
                if dp[i]!=0:
                    dp[i]=min(dp[i-c]+1, dp[i])
                else:
                    dp[i]=dp[i-c]+1
        else:
            break
if dp[M]==0:
    print(-1)
else:
    print(dp[M])