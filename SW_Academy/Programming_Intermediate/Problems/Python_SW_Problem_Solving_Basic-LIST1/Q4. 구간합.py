# 주요변수에 대한 설명
# N : 숫자의 개수
# M : 윈도우 크기
# nums : 숫자들
# window_sums : 윈도우가 움직이면서 합했던 값들

'''문제해결 팁
1. 문서에 수도코드를 작성하라
2. window로 움직이면서 합을 구하는 건 이중 for문을 이용하면서 sum을 이용해라
'''

T = int(input())

for test_case in range(1, T + 1):

    # 입력파싱
    input_line = input()
    params = input_line.split()
    N = int(params[0])
    M = int(params[1])

    input_line = input()
    nums = input_line.split()
    nums = [int(num) for num in nums]

    window_sums = []

    # 윈도우를 움직이면서 합 구하기.
    for i in range(N - (M-1)):      # N = 0~9
        sum = 0
        for k in range(i, i+M):
            sum = sum + nums[k]
        window_sums.append(sum)

    print("#%d %d" % (test_case, (max(window_sums) - min(window_sums))))