def divide(w):
    u=""
    count=0
    for i in range(len(w)):
        if len(u)>1 and count==0:
            break
        else:
            if w[i]=='(':
                count+=1
                u+="("
            else:
                count-=1
                u+=")"
    v=w[len(u):]
    return u, v

def check(u):
    count=0
    for i in range(len(u)):
        if count<0:
            return False
        if u[i]=="(":
            count+=1
        else:
            count-=1
    return True

def solution(p):
    if p=="":
        return ""
    elif check(p)==True:
        return p
    u, v=divide(p)
    right=check(u)
    if right==True:
        return u+solution(v)
    else:
        empty="("
        empty+=solution(v)
        empty+=")"
        if len(u)>2:
            u=u[1:-1]
            for i in range(len(u)):
                if u[i]=="(":
                    empty+=")"
                else:
                    empty+="("
        else:
            u=""
        return empty

#solution("()))((()")