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
  null 개수 출력
> 
> `data.isnull().sum()`
> 
  null인 column만 출력하기
> 
> `data.isnull().sum()[data.isnull().sum()>0]`
> 
> `len(data.isnull().sum()[data.isnull().sum()>0])`
>
- missing value 다루기

  missing value의 총 개수
> 
> `sum(data.isnull().sum()[data.isnull().sum()>0])`
> 
  missing value를 0으로 채우기
> data.fillna(0)
>  #fillna option
>  
>    method=bfill: 뒤의 것으로 채우기
>    
>    method=ffill: 앞의 것으로 채우기

  missing value를 mean으로 채우기
  ```
> from sklearn.impute import SimpleImputer
> 
> import numpy as np
>
> imp_mean=SimImputer(missing_values=np.nan, strategy='mean')
> 
> imp_mean.fit(data)
> 
> imp_mean.transform(data)
  ```

- Categorical 데이터 처리
  eg) `data=[['apple', 0.7], ['pear', 0.3], ['strawberry', 0.4], ['apple', 0.6]]`

  해당 feature drop

> `drop_data = data.select_dtypes(exclude=['object']) //object이면 text로 된 데이터`

  Label encoding
> 
> `apple:1, pear:2, strawberry:3 `
> 
```
> 1. 
> 
> from sklearn.preprocessing import LabelEncoder
> 
> 2. 
> 
> obj_col=[col for col in data.columns if data[col].dtype=='object']
> 
> for col in obj_col:
> 
>    data.loc[data[col]=="apple", col]=1
>    
>    data.loc[data[col]=="pear", col]=2
>    
>    data.loc[data[col]=="strawberry", col]=3
>`
```
> 
> `data=[[1, 0.7], [2, 0.3], [3, 0.4], [1, 0.6]]`

  One-hot encoding

  ```
> 1. 
> 
> from sklearn.preprocessing import OneHotEncoder

> enc=OneHotEncoder()
> 
> obj_col=[col for col in data.columns if data[col].dtype=='object']
>
> enc.fit_transform(data[obj_col])
> 
> 2.
> 
> data=pd.concat([data, pd.get_dummies(data[col_name])], axis=1)
> 
>  data=[[1, 0, 0, 0.7], [0, 1, 0, 0.3], [0, 0, 1, 0.4], [1, 0 , 0, 0.6]]
```

- numpy
 
- pandas
 
  변수 특성 탐색
 
> data frame 크기 출력: `data.shape`

> price 열 정보 출력: `data["price"].describe() == data.price.describe()`
> 
> area 열의 범주 출력: `data["area"].unique()`
> 
> 범주 당 개수 출력: `data["area"].value_counts()`

> 평균: `data["price"].mean()`
 
  map & operator
> 
> price 열의 각 요소들에 mean을 빼줌: `data["price"].map(lambda p: p - data["price"].mean())`

> `data["price"]=data["price"]-data["price"].mean()`

> '한국-서울' 만들기: `data["country"]+ "-" + data["area"]`

  데이터 선택
 
> iloc: index 기반, loc: label 기반 
> 
> iloc
> 
> i번째 행 출력: `data.iloc[i]`
> 
> i, i+100, i+202 번째 행 출력: `data.iloc[[i, i+100, i+202]]`
> 
> i번째 열 출력: `data.iloc[:, i]`
> 
> loc
> 
> i번째 행 출력: `data.loc[i]`
> 
> col 열의 모든 행 출력: `data.loc[:, col]` 

> area 열 중 "seoul" 과 "busan"인 것만 출력

> `data["area"].isin(["seoul", "busan"])`
> 
  
  두 가지 이상의 조건
 
> `data.loc[(조건 1) & (조건 2)]`
> 
> area가 "seoul" "busan" 인 것 중 start 5 이상인 것 출력
> 
> `data.loc[(data["area"].isin(["seoul", "busan"])) & (data["start"]>=5)]`

> `data.hist("col_name")` #col_name 열에 대한 분포 확인
 
  string column의 길이 출력하기
> 
> `data[column].str.len()`  # len(data[column].str) 아님 주의!
> 
  date type 

> `pd.to_datetime(data["Date"], format="%m/%d/%Y")`
> 
> date type에서 day, month, year 선택
> 
> `data["Date"].dt.day`
> `data["Date"].dt.month`
> `data["Date"].dt.year`

>> 

- sklearn

  데이터셋 나누기
  ```
  > from sklearn.model_selection import train_test_split
  >  
> x_train, x_val, y_train, y_val=train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)
```

