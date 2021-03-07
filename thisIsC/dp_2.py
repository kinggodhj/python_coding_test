N=int(input())
numbers=[list(map(int, input().split(' '))) for n in range(N)]

for i in range(1, N):
    for j in range(len(numbers[i])):
        if j==0:
            numbers[i][j]=numbers[i-1][j]+numbers[i][j]
        elif j==len(numbers[i])-1:
            numbers[i][j]=numbers[i-1][j-1]+numbers[i][j]
        else:
            numbers[i][j]=max(numbers[i-1][j-1], numbers[i-1][j])+numbers[i][j]

print(max(numbers[-1]))