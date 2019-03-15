"""<make_element_count_collections.Counter>
  @ 함수설명
  - 리스트를 인자로 받아서 각각의 원소를 카운트 한 결과를 딕셔너리로 반환해준다.

  @ 특이점
  - 결과는 등장빈도가 높은것부터 낮은순으로 정렬되어 나온다.
  - 결과로 나온 것 끼리 덧셈과 뺄셈이 가능하다는 점.
  - 덧셈을 할 경우 값 합산과 합집합이 동시에 일어난다.
  - 뺄셈을 할 경우 값 뺄셈과 여집합이 동시에 일어난다.
"""

import collections

# collections.Count(list) 결과확인
A = ["aa", "aa", "bb", "cc", "dd"]
B = ["aa", "bb", "bb", "cc"]

print(collections.Counter(A))    # Counter({'aa': 2, 'bb': 1, 'cc': 1})
print(collections.Counter(B))    # Counter({'bb': 2, 'aa': 1, 'cc': 1})
print()


# collections.Count(list) 덧셈, 뺄셈 결과확인
subs_result = collections.Counter(A) - collections.Counter(B)
plus_result = collections.Counter(A) + collections.Counter(B)
print(subs_result)               # Counter({'aa': 1})
print(plus_result)               # Counter({'aa': 3, 'bb': 3, 'cc': 2})
print()

# collections.Count(list) 에서 키 값만 얻기
print(list(subs_result.keys()))  # ['aa', 'dd']
print(list(plus_result.keys()))  # ['aa', 'bb', 'cc', 'dd']
print()


# collections.Count(list) 에서 모든 원소의 key, value 접근
for key, value in subs_result.items():
    print(key, value)
print()


# collections.Count(list) 에서 모든 원소의 key, value 접근
for item in list(subs_result.items()):
    print(item)
