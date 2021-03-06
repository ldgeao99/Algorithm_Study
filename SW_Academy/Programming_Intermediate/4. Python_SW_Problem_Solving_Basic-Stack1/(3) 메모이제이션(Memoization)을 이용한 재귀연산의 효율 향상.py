"""<재귀호출을 사용하여 작성할 수 있는 피보나치 수열>
  @ 피보나치 수열
  - 0 과 1로 시작하고, 이전의 두 수의 합을 다음 항으로 하는 수열
  - F0 = 0, F1 = 1 이고, Fi = Fi-1 + Fi-2 (i>=2)
  - 메모이제이션을 사용하지 않고 구현하면 엄청난 중복 연산이 수행됨.

                                                        fibo(6)
                              fibo(5)                                                    fibo(4)
                fibo(4)                      fibo(3)                      fibo(3)                      fibo(2)

        fibo(3)        fibo(2)       fibo(2)        fibo(1)       fibo(2)        fibo(1)        fibo(1)       fibo(0)

   fibo(2)fibo(1)  fibo(1)fibo(0)  fibo(1)fibo(0)              fibo(1)fibo(0)

fibo(1)fibo(0)
"""


"""<메모이제이션(Memoization)>
  
  @ 메모이제이션 이란?
  - 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
  - Dynamic Programming(DP,동적계획법)의 핵심이 되는 기술

  @ 메모이제이션 단어의 의미
  - 글자 그대로 해석하면 메모리에 넣기(to put in memory) 라는 의미
  - 기억되어야 할 것 이라는 뜻의 라틴어 Memorandum에서 파생됨.
  - Memorization(기억하기, 암기하기)과 혼동하는데, 정확한 단어는 Memoization으로 동사형은 Memoize임

  @ 메모이제이션 방법을 적용한 알고리즘
  - 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장해주면 실행시간을 줄일 수 있음.
  - 만약 기존에 계산하여 저장된 값이 있을 경우에는 다시 계산하지 않겠다는 알고리즘을 사용하면 됨.
"""


########################################################################
# 재귀호출을 사용하는 피보나치함수 코드1(비효율적) -> 이런식의 구현은 엄청난 중복호출이 존재함

def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)


print(fibo1(0))  # 0
print(fibo1(1))  # 1
print(fibo1(2))  # 1
print(fibo1(3))  # 2
print(fibo1(4))  # 3
########################################################################


########################################################################
# 재귀호출을 사용하는 피보나치함수 코드2(효율적) -> 메모이제이션을 적용하여 중복호출을 없앤 코드

def fibo2(n):
    global memo  # global 변수를 함수에서 접근할 수 있음

    # n = 0 또는 n = 1 일땐 아래의 조건문 내부의 연산을 안거침
    # len(memo) > n 인 경우 아래의 조건문 내부의 연산을 거치지 않고 예전에 연산되어 있던 결과를 반환해줌 => 이것이 Key Point!!
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]


memo = [0, 1]   # memo 를 위한 리스트를 생성하고, memo[0]을 0으로 memo[1]은 1로 초기화 한다.

print(fibo2(1))  # 1
print(memo)     # [0, 1]

print(fibo2(2))  # 2
print(memo)     # [0, 1, 1]

print(fibo2(3))  # 2
print(memo)     # [0, 1, 1, 2]

print(fibo2(4))  # 3
print(memo)     # [0, 1, 1, 2, 3]
########################################################################