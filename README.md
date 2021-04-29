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

> bin()
>> e.g) bin(4)=0b100


_________________________________________________________

## Data science

- null check
> null 개수 출력
>> 
>> `data.isnull().sum()`
>> 
> null인 column만 출력하기
>> 
>> `data.isnull().sum()[data.isnull().sum()>0]`
>> 
>> `len(data.isnull().sum()[data.isnull().sum()>0])`
>>
> missing value의 총 개수
>> 
>> `sum(data.isnull().sum()[data.isnull().sum()>0])`
>> 
> missing value를 0으로 채우기
>> data.fillna(0)
>>  #fillna option
>>  
>>    method=bfill: 뒤의 것으로 채우기
>>    
>>    method=ffill: 앞의 것으로 채우기

> missing value를 mean으로 채우기
>> 
>> from sklearn.impute import SimpleImputer
>> 
>> import numpy as np
>>
>> imp_mean=SimImputer(missing_values=np.nan, strategy='mean')
>> 
>> imp_mean.fit(data)
>> 
>> imp_mean.transform(data)

- Categorical 데이터 처리
> eg) `data=[['apple', 0.7], ['pear', 0.3], ['strawberry', 0.4], ['apple', 0.6]]`

> 해당 feature drop

>> `drop_data = data.select_dtypes(exclude=['object']) //object이면 text로 된 데이터`

> Label encoding

>> from sklearn.preprocessing import LabelEncoder

>> apple:1, pear:2, strawberry:3 
>> 
>> `data=[[1, 0.7], [2, 0.3], [3, 0.4], [1, 0.6]]`

> One-hot encoding

>> from sklearn.preprocessing import OneHotEncoder

>> enc=OneHotEncoder()
>>
>> ```
>> obj_col=[col for col in data.columns if data[col].dtype=='object']
>> 
>> obj_nuique=list(map(lambda x:data[x].nunique(), obj_col))
>>
>> object_nunique=[data]
>> ```
>>
>> `enc.fit_transform(data[col])`
>> 
>> `data=[[1, 0, 0, 0.7], [0, 1, 0, 0.3], [0, 0, 1, 0.4], [1, 0 , 0, 0.6]]`

- .

> numpy
> 
> pandas
> 
> pandas dataframe 크기 출력
> 
>> `data.shape`  #shape() 아님 주의!


>> data.loc['label_name'] #label_name에 해당하는 모든 행 출력 
>
>sklearn
>
>> from sklearn.model_selection import train_test_split
>> 
>> x_train, x_val, y_train, y_val=train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

