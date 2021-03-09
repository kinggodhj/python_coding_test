import copy
T = int(input())
for test_case in range(1, T + 1):
    N, K=map(int, input().split(' '))
    numbers=list(input())
    all_case=set()
    for _ in range(N//4):
        for j in range(0, N, N//4):
            tmp=''
            for k in range(N//4):
                tmp+=numbers[j+k]
            all_case.add(tmp)
        numbers.insert(0, numbers[-1])
        numbers=numbers[:-1]
    answer=sorted(all_case, reverse=True)[K-1]

    print('#%s %d'%(test_case, int(answer, 16)))