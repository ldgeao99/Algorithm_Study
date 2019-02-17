# 주요변수에 대한 설명
# str1 : pattern
# str2 : text

'''문제해결 팁
1. 고지식한 패턴 검색 알고리즘(Brute Force)의 코드를 기억하면 풀 수 있다.
'''

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    pattern = input()
    text = input()
    result = 0
    ############################################################

    p_len = len(pattern)
    t_len = len(text)

    p_index = 0
    t_index = 0

    while p_index < p_len and t_index < t_len :

        if pattern[p_index] != text[t_index] :
            t_index = t_index - p_index
            p_index = -1

        p_index += 1
        t_index += 1

    if p_index == p_len:
        result = 1
    else:
        result = 0

    # 최종 결과 출력
    print('#' + str(test_case) + ' ' + str(result))
