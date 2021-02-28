N=list(map(int, input()))

sum_1=0
sum_2=0
for i in range(len(N)//2):
    sum_1+=N[i]
    sum_2+=N[len(N)//2+i]

if sum_1==sum_2:
    print("LUCKY")
else:
    print("READY")