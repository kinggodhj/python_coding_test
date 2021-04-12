answer="-1"
def sub(new, c, k):
    global answer
    if c==k:
        if int(new)>int(answer):
            answer=new
            return
    else:
        for i in range(len(new)):
            if int(new[:i]+new[i+1:])>=int(new[:-1]):
                sub(new[:i]+new[i+1:], c+1, k)

def solution(number, k):
    '''
    answer=""
    while(k>0):
        max_v="-1"
        idx=-1
        if k==len(number):
            number=""
            k=0
        else:
            for i in range(k+1):
                if number[i]>max_v:
                    max_v=number[i]
                    idx=1
            number=number[idx+1:]    
            k-=idx
            answer+=max_v
    answer+=number
    '''
    answer=""
    x=0
    stack=""
    while(k>0):
        r=0
        for i in range(x, x+k+1):
            #if k-r==0:
            #    answer+=stack+number[i:]
            #    return answer
            if len(stack)==0:
                stack+=number[i]
            else:
                if number[i]>stack[-1]:
                    l=len(stack)
                    while(l>0):
                        if number[i]>stack[-1] and k-r>0:
                            r+=1
                            stack=stack[:-1]
                            l-=1
                        else:
                            break
                    if k-r==0:
                        answer+=stack+number[i:]
                        return answer
                    stack+=number[i]
                else:
                    stack+=number[i]
        x+=(k+1)
        k-=r
        if k==0:
            answer+=stack
            if x<len(number):
                answer+=number[x:]
                return answer
        if len(stack)>=len(number)-k:
            r=0
            while(k-r>0):
                if stack[-1]<number[x]:
                    r+=1
                    stack=stack[:-1]
                else:
                    return stack[:len(number)-k]
            stack+=number[x]
            return stack
        '''
        if len(stack)>=len(number)-k:
            return stack[:len(number)-k]
        '''

solution("9875321", 2)
#solution("1911111119", 8)