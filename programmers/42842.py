def solution(brown, yellow):
    cand=[]
    for i in range(1, yellow+1):
        if yellow%i==0:
            if i>yellow//i:
                break
            cand.append([yellow//i, i])
    for x,y in cand:
        if (x+2)*(y+2)==brown+yellow:
            return [x+2, y+2]

#solution(10, 2)
#solution(8, 1)
#solution(24, 24)