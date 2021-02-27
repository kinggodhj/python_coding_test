S=list(map(int, input()))

count=0
i=0
while(i<len(S)-1):
    if S[i]!=S[i+1]:
        count+=1
        j=i+2
        while(j<len(S)-1):
            if S[i+1]==S[j]:
                j+=1
            else:
                break
        i=j
    else:
        i+=1

print(count)