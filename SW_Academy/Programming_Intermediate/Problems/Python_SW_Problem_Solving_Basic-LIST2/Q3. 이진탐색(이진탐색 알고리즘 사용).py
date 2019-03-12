# 주요변수에 대한 설명
# total_page : 총 페이지 수
# A_target : A가 찾아야 하는 페이지
# B_target : B가 찾아야 하는 페이지

'''문제해결 팁
1. 전체 이진탐색 알고리즘에 대한 코드를 공부해둔다면 쉽게 해결할 수 있다.
'''

def binarySearch(arr, key):
    start = 0          # start element's index
    end = len(arr)-1   # end   element's index
    count = 0
    while start <= end:

        middle = start + (end - start) // 2  # //은 나눗셈의 몫을 결과로 내줌
        count += 1

        if key == arr[middle]: #검색성공
            return middle, count
        elif key < arr[middle]:
            end = middle - 1   #end를 당겨서 탐색할 범위를 축소하는 것
        else:
            start = middle + 1 #start를 밀어서 탐색할 범위를 축소하는 것
    return -1, count  #검색실패

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    total_page, A_target, B_target = map(int, input().split())

    arr = [i for i in range(1, total_page+1)]

    winner = ''
    ############################################################

    index1, count1 = binarySearch(arr, A_target)
    index2, count2 = binarySearch(arr, B_target)

    if (index1 == -1) and (index2 == -1):
        winner = '0'

    elif (index1 == -1) and (index2 != -1):
        winner = 'B'

    elif (index1 != -1) and (index2 == -1):
        winner = 'A'

    elif (index1 != -1) and (index2 != -1):
        if count1 < count2:
            winner = 'A'
        elif count1 > count2:
            winner = 'B'
        elif count1 == count2:
            winner = '0'

    '''
        index1  index2
           -1      -1    -> 비김
           -1      n     -> B승리
            n      -1    -> A승리
            n       n    -> count비교(A승리 or B승리 or 비김)
    '''
    # 최종 결과 출력
    print('#' + str(test_case) + ' ' + winner)