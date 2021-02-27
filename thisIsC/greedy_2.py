S=list(map(int, list(input())))

result=S[0]
for number in S[1:]:
    if number>1 and result>1:
        result*=number
    else:
        result+=number

print(result)