# 주요변수에 대한 설명
# N : 총 카드 장수

'''문제해결 팁
1. 문자열 변수는 배열처럼 다룰 수 있다.
'''

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    nums = input()

    # 각각의 숫자 개수 카운트
    count = [0] * 10
    for num in nums :
        count[int(num)] += 1

    # 최다 빈도수 구하기
    mostFrequency = max(count)

    # 최다 빈도수를 가지는 숫자들 중 가장 큰 수를 찾기
    mostNums = []
    for i in range(len(count)) :
        if mostFrequency == count[i]:
            mostNums.append(i)
    resultNum = max(mostNums)

    # 최종 결과 출력
    print('#' + str(test_case) + ' '+ str(resultNum) + ' ' + str(mostFrequency))