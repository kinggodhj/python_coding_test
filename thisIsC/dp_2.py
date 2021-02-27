N=int(input())
wareHouse=list(map(int, input().split(' ')))
dp=[0]*N

dp[0]=wareHouse[0]
#dp[1]=wareHouse[1]
dp[1]=max(wareHouse[0], wareHouse[1])

for i in range(2, N):
    dp[i]=max(dp[i-1], dp[i-2]+wareHouse[i])

print(dp[N-1])