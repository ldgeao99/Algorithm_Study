# Q. 양수들 중 최소값과 최대값의 차이를 출력

'''문제해결 팁
477162 658880 751280 이런식으로 입력을 한번에 여러개 받는 것은 문자열로 통째로 받아 split()한뒤 list comprehension을 이용해 데이터형을 바꿔줄 수 있다.
'''

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_str = input()

    l = num_str.split(' ')
    l = [int(item) for item in l]

    min_value = min(l)
    max_value = max(l)

    gap = max_value - min_value

    result = "#" + str(test_case) + " " + str(gap)

    print(result)