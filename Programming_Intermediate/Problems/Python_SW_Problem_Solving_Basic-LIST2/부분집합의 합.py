# 주요변수에 대한 설명
# N : 부분집합이 가지고 있을 수 있는 원소의 개수
# K : N개의 원소로 이루어진 부분집합들을 모두 합한 값

'''문제해결 팁
1. 전체 부분집합을 구하는 알고리즘에 대한 코드를 공부해둔다면 쉽게 해결할 수 있다.
'''

T = int(input())
A = [i for i in range(1, 13)] # [1,2,3,,,,12]

for test_case in range(1, T + 1):

    ############################################################
    N, K = map(int, input().split())
    count = 0
    ############################################################

    for i in range(1<<len(A)):
        arr = []
        for j in range(len(A)):
            if i & (1<<j):
                arr.append(A[j])
        if len(arr) == N and sum(arr) == K:
            count += 1


    # 최종 결과 출력

    print('#' + str(test_case) + ' ' + str(count))
