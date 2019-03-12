# !!!아래의 내용은 하나도 빠짐없이 모두 숙지해야 하는 내용!!!
# 반복학습 횟수 : 1

'''
<검색 이란?>
'검색' : 저장되어 있는 자료 중에서 '원하는 항목'을 찾는 방법
'원하는 항목' : 목적하는 탐색키(자료를 구별하여 인식할 수 있는 키)를 가진 항목
'''

'''
<검색의 종류>
*순차검색(Sequential Search)
- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
- List 혹은 Linked List 등 순차구조로 구현된 자료구조에서 유용함
- 구현이 쉽지만, 검색 대상이 많은 경우 수행시간의 증가로 비효율적임
- 2가지의 경우가 존재(정렬된 상태에서의 검색, 정렬되지 않은 상태에서의 검색)
- 순차검색은 정렬되어 있든 안되어 있든 평균 비교 횟수는 동일하며 시간복잡도는 O(n)이다.

case1) 정렬되지 않은 자료의 검색 과정
       1. 첫번째 원소부터 순서대로 검색대상과 키 값이 같은 원소가 있는지를 비교하여 찾음
       2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
       3. 자료구조의 마지막에 갈 때까지 검색 대상을 찾지 못하면 검색 실패로 종료
       
       시간복잡도 : O(n)
       -> 한번 만에 원소를 찾을 때는 1번 비교, 두번 만에 원소를 찾을 때는 1번 비교, ..., n번 만에 원소를 찾을 때는 n번 비교
       -> 평균 비교 횟수 = (1+2+...+n)/n = (n(n+1)/2)/n = (n+1)/2  
       -> 따라서 시간복잡도 = O(n)
       
case2) 정렬되지 않은 자료의 검색 과정
       1. 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
       2. 자료를 순차적으로 검색하면서 키 값을 비교함
       3. 원소의 키 값이 검색 대상의 키 값보다 크면 원소가 없다는 것을 의미하므로 검색 실패로 종료

       시간복잡도 : O(n)
       -> 한번 만에 원소를 찾을 때는 1번 비교, 두번 만에 원소를 찾을 때는 1번 비교, ..., n번 만에 원소를 찾을 때는 n번 비교
       -> 평균 비교 횟수 = (1+2+...+n)/n = (n(n+1)/2)/n = (n+1)/2  
       -> 따라서 시간복잡도 = O(n) 


*이진검색(Binary Search)
- 순차검색보다 효율적인 검색 방법
- 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 빠르게 검색을 수행함
- 이진검색을 사용하기 위해서는 자료가 정렬된 상태여야 함
- 자료에 삽입이나 삭제가 발생하였을 때 List의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요함

1. 자료의 중앙에 있는 원소를 선택
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교
3. 목표값 < 중앙 원소 값 : 자료의 왼쪽 절반에 대해서 새로 검색을 수행
   목표값 > 중앙 원소 값 : 자료의 오른쪽 절반에 대해서 새로 검색을 수행
4. 찾고자 하는 값을 찾을 때까지 [1 ~ 3]의 과정을 반복

       시간복잡도 : O(log n)
       -> 정렬된 데이터 n개가 있는 경우의 시간복잡도

* 인덱스(Index)
- 데이터베이스에서 유래, 테이블에 대한 동작 속도를 높임
- 데이터베이스 분야가 아닌 다른 분야에서는 같은 의미로 '룩 업 테이블' 등의 용어로 사용하기도 한다. 
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블 저장에 필요한 디스크 공간보다 작음
- 인덱스는 키 필드만 갖고 있고, 테이블의 다른 세부 항목은 갖고 있지 않으므로 .
- 대량의 데이터를 매번 정렬하면, 프로그램의 반응이 느려질 수 밖에 없는데, 이런 성능저하 문제를 해결하기위해 'List인덱스'틑 사용할 수 있음
- 원본 데이터에 데이터가 삽입될 경우 상대적으로 크기가 작은 인덱스 List를 정렬하기 때문에 속도가 빠름
'''


######### 순차검색(정렬되어 있지 않은 상태의 경우)
def sequentialSearch(arr, key):
    i = 0
    while i < len(arr) and arr[i] != key:
        i += 1

    if i < len(arr):
        return i
    else:
        return -1

arr = [8,2,4]
print("순차검색(정렬되어 있지 않은 상태의 경우)")
print(sequentialSearch(arr, 4))   # 2
print(sequentialSearch(arr, 1))   # -1

######### 순차검색(정렬되어 있는 상태의 경우)
def sequentialSearch2(arr, key):
    i = 0
    while i < len(arr) and arr[i] < key:
        i += 1

    if i < len(arr) and arr[i] == key :
        return i
    else:
        return -1

arr2 = [2,4,8]
print("순차검색(정렬되어 있는 상태의 경우)")
print(sequentialSearch2(arr2, 4)) # 1
print(sequentialSearch2(arr2, 9)) # -1

######### 이진검색(기본방법)
def binarySearch(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        middle = start + (end - start) // 2  # //은 나눗셈의 몫을 결과로 내줌

        if key == arr[middle]: #검색성공
            return middle
        elif key < arr[middle]:
            end = middle - 1   #end를 당겨서 탐색할 범위를 축소하는 것
        else:
            start = middle + 1 #start를 밀어서 탐색할 범위를 축소하는 것
    return -1  #검색실패

arr = [2, 4, 7, 9, 11, 19, 23] # 정렬되어있는 상태의 배열
print("이진검색(기본방법)")
print(binarySearch(arr, 7))    # 2
print(binarySearch(arr, 24))   # -1

######### 이진검색(재귀함수를 이용한 방법)
def binarySearch2(arr, start, end, key): # low, high는 탐색할 index의 구간을 설정하는 것이다.
    if start > end :
        return -1
    else:
        middle = (start + end) // 2  # //은 나눗셈의 몫을 결과로 내줌

        if key == arr[middle]:       # 검색성공
            return middle
        elif key < arr[middle]:
            return binarySearch2(arr, start, middle-1, key)
        elif arr[middle] < key :
            return binarySearch2(arr, middle+1, end, key)

arr = [2, 4, 7, 9, 11, 19, 23] # 정렬되어있는 상태의 배열
print("이진검색(재귀함수를 이용한 방법)")
print(binarySearch2(arr, 0, 6, 7))    # 2
print(binarySearch2(arr, 0, 6, 24))   # -1