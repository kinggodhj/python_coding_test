S=list(input())

num=0
alpha=[]
for i in range(len(S)):
    if S[i].isdigit():
        num+=int(S[i])
    else:
        alpha.append(S[i])

alpha.sort()
print(''.join(alpha)+str(num))
