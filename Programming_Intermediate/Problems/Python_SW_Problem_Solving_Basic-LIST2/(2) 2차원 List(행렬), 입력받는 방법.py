# !!!아래의 내용은 세개의 해답 중 하나만 알면 되는 내용!!!
# 반복학습 횟수 : 1

''' 입력예시
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''
# 사용되는 변수는 n, m 그리고 mylist 이렇게 딱 3개만 사용된다.

######### 풀이1

n, m  = map(int, input().split())               # n = 3, m = 4

mylist = [0 for _ in range(n)]                  # mylist = [0, 0 , 0]
# mylist = [0] * n

for i in range(n):
    mylist[i] = list(map(int, input().split())) # mylist = [[0, 1, 0, 0][0, 0, 0, 0][0, 0, 1, 0]]

######### 풀이2

n, m  = map(int, input().split())

mylist = []

for i in range(n):
    mylist.append(list(map(int, input().split())))

######### 풀이3

n, m  = map(int, input().split())

mylist = [ list(map(int, input().split())) for _ in range(n) ]

