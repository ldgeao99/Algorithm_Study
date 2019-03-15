"""<버블정렬>
  @ 시간복잡도
  Best  : O(n^2)
  Avg   : O(n^2)
  Worst : O(n^2)

 @ 알고리즘 로직
 - 크기가 2인 윈도우를 맨 뒤까지 움직이면서 비교하고, 작은건 앞으로 큰건 뒤로 옮긴다.
 - 이를 리스트의 크기 - 1 번 만큼 반복한다. (한번을 마칠 때 마다 정렬이 완료된 숫자가 맨 뒤에 fix 된다.)
"""


# 오름차순 정렬
def bubble_sort(lst):
    new_list = lst.copy()

    for i in range(len(new_list)-1):
        for j in range(len(new_list)-1-i):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list


lst = [3, 2, 5, 1]
print(lst)
print(bubble_sort(lst))


