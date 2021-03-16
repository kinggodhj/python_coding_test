N=int(input().rstrip())
array=list(map(int, input().rstrip().split(' ')))
B,C=map(int, input().rstrip().split(' '))

array=list(map(lambda x:x-B, array))
count=N
for i in array:
    if i>0:
        if i%C==0:
            count+=(i//C)
        else:
            count+=(i//C)+1
print(count)