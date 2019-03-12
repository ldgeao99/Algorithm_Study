# !!!아래의 내용은 하나도 빠짐없이 모두 숙지해야 하는 내용!!!
# 반복학습 횟수 : 1

'''
*셀렉션 알고리즘
- 저장되어 있는 자료로 부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함
- 정렬 알고리즘을 이용하여 자료를 정렬하고, 원하는 순서에 있는 원소를 가져오는 방식으로 동작한다.

예) k번째로 작은 원소를 찾는 알고리즘
       1. 다음의 행위를 k번 계속한다.
       2. 정렬이 안된 맨 앞의 원소와 그 뒤에 모든 원소들을 차례로 끝까지 비교하여 가장 작은 수가 위치한 곳을 찾아냄
       3. 찾아냈다면 두 숫자까리 위치를 서로 바꿈
       
       시간복잡도 : O(kn)
       -> k가 비교적 작을 때 유용함.  
       -> k는 몇번째의 것을 찾는지, n은 아마도 리스트의 크기

*선택정렬
- 셀렉션 알고리즘을 전체 자료에 적용한 것
- 가장 작은 값의 원소를 찾아 맨 앞의 것과 교환하는 방식을 이어가는 것 
       시간복잡도 : O(n^2)
'''

######### 셀렉션 알고리즘(k번째로 작은 원소를 찾는 알고리즘)
def select(arr, k):
    for i in range(0, k):
        minIndex = i
        #아래는 k번 작동하는 for문
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]: #정렬안된 맨 앞의 원소와 뒤의 모든 원소들을 차례로 끝까지 비교해서 가장 작은수가 위치한 곳을 찾아냄
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr[k-1]

arr = [4,5,2,1,3]
print(select(arr, 2)) # 2

######### 선택정렬
def selectionSort(arr):
    for i in range(0, len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

arr = [4,5,2,1,3]
selectionSort(arr)
print(arr)             # [1, 2, 3, 4, 5]