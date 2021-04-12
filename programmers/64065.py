from collections import Counter

def solution(s):
    s=s.split(',')
    s=[s[i].strip("{},") for i in range(len(s))]
    counter=Counter(s).most_common()
    answer=[]
    for num, _ in counter:
        answer.append(int(num))
    return answer
    
#solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
#solution("{{20,111},{111}}")