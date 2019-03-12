# 주요변수에 대한 설명
# 생략

'''문제해결 팁
1. 딕셔너리 사용법을 알고있으면 쉽게 해결가능
'''

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    str1 = input()
    str2 = input()
    result = 0
    ############################################################

    str1_list = list(str1)
    str2_list = list(str2)

    dic = {}

    for i in range(len(str1_list)):
        dic[str1_list[i]] = 0

    for i in range(len(str1_list)):
        if dic[str1_list[i]] == 0:
            for j in range(len(str2_list)):
                if str1_list[i] == str2_list[j]:
                    dic[str1_list[i]] += 1

    result = max(list(dic.values()))

    # 최종 결과 출력
    print('#' + str(test_case) + ' ' + str(result))
