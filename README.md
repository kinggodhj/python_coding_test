Python을 기반으로 하는 코딩 테스트 준비

유용한 함수&패키지들 정리
==================
> Queue
> 
>> from collections import queue

> 
> defaultdict
> 
>> from collections import defaultdict

> 
> minheap
> 
>> import heapq
> 
  
>   ord()
>>  e.g) ord('a')=97
>   
>   src()
>>  e.g) src(97)='a'
>
>   isdigit()
>>  e.g) a=100, 
>>  
>>  a.isdigit(): True
>>  
>   sort()
>>  e.g) a=[(3, 1, 1), (3, 1, 9), (3, 5, 5), (5, 1, 5)]
>>  
>>  a.sort(key=lambda x: (-int(x[0]), int(x[1]), int(x[2])) 
>>  
>>  #0번째 원소를 기준으로 내림차순 정렬
>>  #1번째 원소를 기준으로 오름차순 정렬
>>  #2번째 원소를 기준으로 오름차순 정렬
>>  
