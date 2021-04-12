def solution(people, limit):
    people.sort()
    i=0
    j=len(people)-1
    answer=0
    while(i<=j):
        if i==j:
            answer+=1
            return answer
        if people[i]+people[j]<=limit:
            i+=1
        answer+=1
        j-=1
    return answer

#solution([10, 10, 90, 90], 100)
#solution([70, 50, 80, 50], 100)
#solution([70, 80, 50], 100)