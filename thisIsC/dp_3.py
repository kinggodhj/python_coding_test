N=int(input())
schedule=[[0,0]]
for _ in range(N):
    schedule.append(list(map(int, input().split(' '))))

dp=[0]*(N+2)

for days in range(1, N+1):
    time=schedule[days][0]+days
    if time>N+1:
        continue
    pay=schedule[days][1]
    dp[time]=max(dp[time], max(dp[:days+1])+pay)

print(max(dp))