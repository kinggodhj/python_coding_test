N=int(input().rstrip())
dp=[0]*(10**6+1)
dp[0]=0
dp[1]=0
dp[2]=1
dp[3]=1
for n in range(4, N+1):
    dp1=int(1e9)
    dp2=int(1e9)
    if n%3==0:
        dp1=dp[n//3]+1
    if n%2==0:
        dp2=dp[n//2]+1
    dp[n]=min(dp[n-1]+1, dp1, dp2)

print(dp[N])