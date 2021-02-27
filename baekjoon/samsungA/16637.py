from collections import deque

N=int(input())
equation=input()

def getNumAOp(equation):
    num=[]
    op=[]
    for n in range(N):
        if n%2==0:
            num.append(int(equation[n]))
        else:
            op.append(equation[n])
    return num, op

def cal(num1, num2, op):
    if op=='*':
        return num1*num2
    elif op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2

def bfs(num, op, idx):
    queue=deque([])
    queue.append([num[idx], idx])
    value=float('-inf')
    while queue:
        number, now_idx=queue.popleft()
        if number>value and now_idx==len(op):
            value=number
        if now_idx<len(op):            
            #그냥 더하는 경우
            queue.append([cal(number, num[now_idx+1], op[now_idx]), now_idx+1])
            #괄호 하는 경우 
            if now_idx+1<len(op): #다음 오퍼레이션이 있어야됨
                tmp=cal(num[now_idx+1], num[now_idx+2], op[now_idx+1])
                queue.append([cal(number, tmp, op[now_idx]), now_idx+2])
    return value

num, op=getNumAOp(equation)
print(bfs(num, op, 0))