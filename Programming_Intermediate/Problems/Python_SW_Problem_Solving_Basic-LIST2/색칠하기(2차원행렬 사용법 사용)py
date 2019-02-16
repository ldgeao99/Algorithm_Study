# 주요변수에 대한 설명
# N : 칠할 영역의 개수
# arr : 그림판

'''문제해결 팁
1. 주의할점. arr선언할 때 [] * 10 하면 절대안됨. 똑같은 주소를 가리키는 리스트가 10개 복사되어서 한 원소의 값을 바꾸려 해도 10개의 원소가 바뀜.
'''

T = int(input())

for test_case in range(1, T + 1):

    ############################################################

    N = int(input())
    arr = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]for _ in range(10)]

    ############################################################

    for _ in range(N):
        start_x, start_y, end_x, end_y, color = map(int, input().split())

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if arr[i][j] == -1:
                    arr[i][j] = 0
                else:
                    if arr[i][j] != color:
                        arr[i][j] = 3

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 3:
                count += 1

    # 최종 결과 출력

    print('#' + str(test_case) + ' ' + str(count))
