X=int(input())

count=0
while(X>1):
    if X%5==0:
        X=X//5
        count+=1
    elif X%3==0:
        X=X//3
        count+=1
    elif X%2==0:
        X=X//2
        count+=1
    else:
        X-=1
        count+=1

print(count)