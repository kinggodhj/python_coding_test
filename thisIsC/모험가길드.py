N=int(input())
people=list(map(int, input().split(' ')))

people.sort()

count=0
i=0
for p in people:
    i+=1
    if i>=p:
        count+=1
        i=0
print(count)