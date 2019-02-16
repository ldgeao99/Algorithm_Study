# 주요변수에 대한 설명
# N : 정렬해야하는 원소들의 수
# arr : 정렬해야하는 원소를 가지고 있는 리스트

'''문제해결 팁
1. 전체 선택정렬 알고리즘에 대한 코드를 공부했다면 해결할 수 있다.
'''

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    N = int(input())
    arr = list(map(int, input().split()))
    ############################################################

    for i in range(N-1): # i  = 0~8
        select = i
        for j in range(i+1, N): # 1~9
            if i % 2 == 0 :
                if arr[select] < arr[j]:
                    select = j
            elif i % 2 != 0 :
                if arr[select] > arr[j]:
                    select = j
        arr[i], arr[select] = arr[select], arr[i]

    # 최종 결과 출력
    print('#' + str(test_case), end='')
    for i in range(10):
        print(' ' + str(arr[i]), end='')
    print()