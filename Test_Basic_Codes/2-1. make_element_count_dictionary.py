"""<make_element_count_dictionary>
  @ 함수설명
  - 리스트를 인자로 받아서 각각의 원소를 카운트 한 결과를 딕셔너리로 반환해준다.

  @ 주의점
  - count 메소드를 사용하면 똑같은 구간을 계속 탐색하는 비효율이 발생하여 효율이 떨어질 수 있다.
"""


def make_element_count_dictionary(lst):
    dic = {}

    for item in lst:
        keys = dic.keys()
        # 딕셔너리에 없다면 생성 후 1로 초기화
        if item not in keys:
            dic[item] = 1
        # 딕셔너리에 있다면 카운트 1증가
        else:
            dic[item] += 1

    return dic


lst = ['a', 'b', 'c', 'c', 'd']
print(make_element_count_dictionary(lst))  # {'a': 1, 'b': 1, 'c': 2, 'd': 1}

lst = [1, 2, 2, 3, 4]
print(make_element_count_dictionary(lst))  # {1: 1, 2: 2, 3: 1, 4: 1}

