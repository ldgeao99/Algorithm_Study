# 주요변수에 대한 설명
# 생략

'''문제해결 팁
1. 행렬을 회전시키는 법
2. 회문인지 아닌지 확인하는 법 이 두가지를 알면 해결 가능
'''

# 회문형태의 리스트라면 1을 아니면 0을 반환한다.
def is_circular_list(lst):
    copied_lst1 = lst.copy()
    copied_lst2 = lst.copy()   # reverse 시킬 리스트

    for i in range(len(lst)//2):
        copied_lst2[i], copied_lst2[len(lst) - i - 1] = copied_lst2[len(lst) - i - 1], copied_lst2[i]

    if copied_lst1 == copied_lst2:
        return 1
    else:
        return 0

#리스트를 90도 오른쪽으로 회전시킨다.
def turn_lst(lst):
    turned_lst = []


    for i in range(len(lst)):
        l = []
        for j in range(len(lst)):
            l.append(lst[j][i])
        turned_lst.append(l)

    return turned_lst

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    N, M = map(int, input().split()) # N * N에서 M글자수의 회문.

    source = [list(input()) for i in range(N)]

    result = ""
    ############################################################

    #가로 테스트
    for i in range(N):
        line = source[i]              # 한줄을 가져옴
        for j in range(N + 1 - M):
            temp = []                 # M개의 원소를 담는 윈도우.
            for k in range(j,j+M):
                temp.append(source[i][k])
            if is_circular_list(temp):
                result = "".join(temp)  # ['a','b','c'] => "abc"
                break

    #source 리스트 90도 회전
    turned_lst = turn_lst(source)

    #세로 테스트
    for i in range(N):
        line = turned_lst[i]              # 한줄을 가져옴
        for j in range(N + 1 - M):
            temp = []                 # M개의 원소를 담는 윈도우.
            for k in range(j,j+M):
                temp.append(turned_lst[i][k])
            if is_circular_list(temp):
                result = "".join(temp)  # ['a','b','c'] => "abc"
                break

    # 최종 결과 출력
    print('#' + str(test_case) + ' ' + result)
