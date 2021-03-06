"""<분할정복 알고리즘>

  @ 분할정복 알고리즘의 유래
  - 1805년 12월 2일, 아우스터리츠 전투에서 나폴레옹이 사용한 전략에서 유래하였으며
  - 전력이 우세한 연합군을 공격하기 위해 연합군의 중앙부로 침입한 후, 연합군을 둘로 나누고 둘로 나뉜 연합군을 한 부분씩 격파했다고 한다.

  @ 분할정복 알고리즘의 구성
  - 1) 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눔
  - 2) 정복 : 나눈 작은 문제를 각각 해결
  - 3) 통합 : (필요하다면) 해결된 해답을 모음
"""


"""<거듭제곱 알고리즘>

  @ 거듭제곱 알고리즘(일반적인)
  - 시간복잡도 : n번 곱하는 것이기에 O(n)
  - 실행코드는 아래에 있음
  - ex) C^2 = C * C
        C^3 = C * C * C
        C^n = C * C * ... *C  

  @ 거듭제곱 알고리즘(분할 정복 기반)
  - 시간복잡도 : n번 곱하는 것이기에 O(log2n)
  - 실행코드는 아래에 있음
  - ex) C^8 = C * C * C * C * C * C * C * C
        C^8 = C^4 * C^4 = ((C^2)^2)^2
        C^n = C^(n-1) * C = C^((n-1)/2) * C^((n-1)/2) * C = (C^((n-1)/2))^2 * C  
              C^(n/2) * C^(n/2)             ---> n이 짝수인 경우 
        C^n = 
              C^((n-1)/2) * C^((n-1)/2) * C ---> n이 홀수인 경우  
"""


"""<퀵정렬과 병합정렬의 비교>

                        @ 병합정렬                                            @ 퀵정렬
  -----------------------------------------------------------------------------------------------------------------
  공통점                               주어진 리스트를 두 개로 분할하고, 각각을 정렬한다.
  -----------------------------------------------------------------------------------------------------------------
       |                 분할할 때,                 |                          분할할 때,
       |            단순하게 두 부분으로 나눈다.         |  기준 아이템(Pivot Item)을 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴 
  차이점 |----------------------------------------------------------------------------------------------------------
       |           각 부분 정렬이 끝난 후,             |                각 부분 정렬이 끝난 후,
       |        병합이란 후처리 작업이 필요함            |               후처리 작업이 필요하지 않음
          
"""


"""<퀵정렬 알고리즘>

  @ 최악의 경우 시간복잡도 : O(n^2) 
  -> 병합정렬에 비해 효율이 떨어짐.
  -> 그런데 왜 퀵정렬 이라고 했을까?
  -> 퀵 정렬의 평균 복잡도는 O(n log n) 이기 때문임(최악의 경우 O(n^2)이지만 평균적으로는 가장 빠름)


  @ 알고리즘 동작 과정
  - 동작과정이 글자로 보면 이해가 어려우니 PPT 및 동영상 참고
  
  1. 초기에 리스트의 중앙의 값을 피봇으로 정한다.(단, 원소가 2개인 집합의 경우 L을 피봇으로 지정한다.)

  2. 초기에 리스트의 맨 왼쪽의 원소를 L, 맨 오른쪽의 원소를 R로 지정한다.

  3. L을 오른쪽으로 이동시키며 피봇보다 크거나 같은 원소를 찾는데 찾으면 그자리에 멈춘다.  
     그리고, R은 왼쪽으로 이동하면서 피봇보다 작은 원소를 찾는데 찾으면 그자리에 멈춘다.
     못찾으면 끝까지 이동할 수 있다.
   
  4. case1) L과 R이 같은 위치에서 멈췄으면, 피봇의 값과 교환한다. (단, L, R, 피봇 모두 같은 위치면 다음의 작업만 진행한다.)
            그리고, 위치가 바뀐 피봇의 값은 이후 정렬에서 제외시킨다. 
            또한, 바뀐 피봇을 기준으로 왼쪽집합, 오른쪽 집합으로 나눈다.

     case2) L과 R이 다른위치에서 멈췄으면 L과 R을 서로 교환한다. 이땐 정렬에서 제외하지 않는다.
            다시 1.로 돌아가서 같은 작업을 반복한다.

  5. {왼쪽 집합} 피봇 {오른쪽 집합}에 대해 왼쪽 집합 -> 오른쪽 집합 순서로 다시 퀵 정렬을 수행함.
     1.로 돌아가서 다시 같은 작업을 하는 것임.
     (단, 집합의 원소가 1개인 경우 퀵정렬을 수행하지 않고 바로 정렬에서 제외시킴.)
"""


########################################################################

# 거듭제곱 알고리즘(일반적인)
def power(base, exponent):

    if base == 0:
        return 1

    result = 1  # 변수 초기화

    for _ in range(exponent):
        result *= base
    return result


print(power(2, 4))
print(power(2, 5))
print()
########################################################################


########################################################################

# 거듭제곱 알고리즘(분할 정복 기반)
def power2(base, exponent):

    if exponent == 0 or base == 0:
        return 1

    # 지수가 짝수인 경우
    if exponent % 2 == 0:
        newbase = power2(base, exponent/2)  # 재귀적으로 하나의 값만 남을 때 까지 나눔.
        return newbase * newbase
    # 지수가 홀수인 경우
    else:
        newbase = power2(base, (exponent-1)/2)
        return (newbase * newbase) * base


print(power2(2, 4))
print(power2(2, 5))
print()
########################################################################


########################################################################


# 퀵정렬 알고리즘
def quickSort(a, begin, end):  # 정렬할리스트, 시작인덱스, 끝인덱스
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)


def partition(a, begin, end):

    pivot = (begin + end) // 2  # 피봇이 될 인덱스를 구함.
    L = begin
    R = end

    while L < R:
        while a[L] < a[pivot] and L < R:
            L += 1
        while a[R] >= a[pivot] and L < R:
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


arr = [4, 1, 3, 7, 5]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)

########################################################################