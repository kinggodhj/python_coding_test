import sys

N=int(sys.stdin.readline().rstrip())
have=list(map(int, sys.stdin.readline().split(' ')))

M=int(sys.stdin.readline().rstrip())
check=list(map(int, sys.stdin.readline().split(' ')))

have.sort()

def binSearch(array, target, start, end):
    if start>end:
        return False
    mid=(start+end)//2

    if target==array[mid]:
        return True
    elif target<array[mid]:
        return binSearch(array, target, start, mid-1)
    else:
        return binSearch(array, target, mid+1, end)

for c in check:
    result=binSearch(have, c, 0, len(have)-1)
    if result==False:
        print('no', end=' ')
    else:
        print('yes', end=' ')    