def solution(n):
    arr=[[0]*i for i in range(1, n+1)]
    num=1
    x,y=0,0
    c=n
    while(num<=(n*(n+1)//2)):
        for _ in range(c):
            arr[x][y]=num
            num+=1
            x+=1
        x-=1
        y+=1
        c-=1
        for _ in range(c):
            arr[x][y]=num
            num+=1
            y+=1
        y-=2
        x-=1
        c-=1
        for _ in range(c):
            arr[x][y]=num
            num+=1
            x-=1
            y-=1
        x+=2
        y+=1
        c-=1
    answer=[]
    for i in arr:
        for j in i:
            answer.append(j)
    print(answer)
solution(4)