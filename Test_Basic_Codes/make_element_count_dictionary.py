"""<make_element_count_dictionary>
리스트를 인자로 받아서 각각의 원소를 카운트 한 결과를 딕셔너리로 반환해준다.
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