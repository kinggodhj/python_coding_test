def binSearch(array, target, start, end):
    while(start<=end):
        mid=(start+end)//2
        if target==array[mid]:
            return target
        elif target<array[mid]:
            end=mid-1
        else:
            start=mid+1
    return None