"""<make_element_count_list>
- 리스트를 인자로 받아서 각각의 원소를 카운트 한 결과를 리스트로 반환해준다.
- count 메소드를 사용하면 똑같은 구간을 계속 탐색하는 비효율이 발생하여 효율이 떨어질 수 있다.

"""


def make_element_count_list(lst):
    result_lst = []

    # 유니크한 원소를 뽑아냄.
    unique_element_list = lst.copy()
    unique_element_list = set(unique_element_list)

    # 유니크한 원소들을 이용해 카운트 하기전 초기상태 세팅
    for unique_element in unique_element_list:
        result_lst.append([unique_element, 0])

    # 리스트에서 숫자를 하나씩 꺼내서 카운트
    for element in lst:
        for item, i in zip(result_lst, range(len(result_lst))):
            if item[0] == element:
                result_lst[i][1] += 1

    return result_lst


lst = ['a', 'b', 'c', 'c', 'd']
print(make_element_count_list(lst))  # [['b', 1], ['c', 2], ['d', 1], ['a', 1]]

lst = [1, 2, 2, 3, 4]
print(make_element_count_list(lst))  # [[1, 1], [2, 2], [3, 1], [4, 1]]
