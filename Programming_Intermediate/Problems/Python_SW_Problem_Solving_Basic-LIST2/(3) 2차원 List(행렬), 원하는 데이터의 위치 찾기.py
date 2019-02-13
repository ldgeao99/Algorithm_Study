# !!!아래의 내용은 하나도 빠짐없이 모두 숙지해야 하는 내용!!!
# 반복학습 횟수 : 1

''' 입력예시
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''

######### 풀이1

n, m = map(int, input().split())

newlist = []

mylist = [0 for _ in range(n)]

for i in range(n):
    mylist[i] = list(map(int, input().split()))
    for j in range(m):
        if mylist[i][j] == 1:
            newlist.append([i,j])

######### 풀이2

n, m = map(int, input().split())

mylist = [list(map(int, input().split())) for _ in range(n)]

newlist = [(i,j) for i in range(n) for j in range(m) if mylist[i][j] == 1]