def solution(participant, completion):
    answer = ''

    # 이름의 개수를 센 딕셔너리를 참가자, 완주자에 대해서 각각 만듬
    p_dic = make_element_count_dictionary(participant)
    c_dic = make_element_count_dictionary(completion)

    # 중복된 이름이 없다면 1개만 나올 것임
    lst = list(set(p_dic.keys()) - set(c_dic.keys()))

    # 중복된 이름이 없는 경우
    if len(lst) == 1:
        answer = lst[0]
    # 중복된 이름이 있는 경우
    elif len(lst) == 0:
        for p in participant:
            if p_dic[p] != c_dic[p]:
                answer = p
                break

    return answer


# 참가자 혹은 완주자 리스트로 이름을 카운트한 딕셔너리 생성
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
