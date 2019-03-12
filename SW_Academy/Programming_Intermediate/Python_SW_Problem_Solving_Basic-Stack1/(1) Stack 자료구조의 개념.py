"""
<Stack>
- 믈건을 쌓아 올리듯 자료를 쌓아올린 형태의 자료구조
- 스택에 저장된 자료는 선형구조를 가짐
  @ 선형구조 : 자료 간의 관계가 1대 1의 관계를 가짐
  @ 비선형구조 : 자료 간의 관계가 1대 N의 관계를 가짐(예시 : 트리)
- 마지막에 삽입한 자료를 가장 먼저 꺼낼 수 밖에 없는 구조
- 스택에서 마지막에 삽입된 원소의 위치를 top이라고 부름(초기값은 -1)
- 후입선출 (LIFO, Last-In-First-Out) 이라고 부름
"""


"""
<자료를 선형으로 저장하기 위한 언어별 방법>
- C      : 배열을 사용할 수 있음.
- Python : 리스트를 사용할 수 있음.
"""


"""
<Stack 에서 사용되는 연산>
- push    : 저장소에 자료를 삽입하는 연산
- pop     : 삽입한 자료를 역순으로 꺼내는 연산
- isEmpty : 스택이 공백인지 아닌지 확인하는 연산
- peek    : 스택의 top에 있는 item을 pop하지 않고 참조만 하는 연산
"""


"""
<push 알고리즘 구현>
* Python으로 push 연산을 구현할 시 리스트 크기에 제한이 없으므로 Overflow 문제를 고려할 필요가 없다.
* 또한, append를 사용하면 top을 기억할 필요가 없다.
def push(item):
    s.append(item)

<pop 알고리즘 구현>
* Python으로 pop을 구현하면 len값으로 top의 값을 알 수 있으므로 top 변수가 필요 없다.
def pop():
    if len(s) == 0:       # 스택에 자료가 없는경우 underflow 처리를 함
        # underflow
        return
    else:
        return s.pop(-1)  # 리스트의 맨 뒤의 값을 반환해줌
"""


# <push, pop 예시코드>


def push(item):
    s.append(item)


def pop():
    if len(s) == 0:       # 스택에 자료가 없는경우 underflow 처리를 함
        print("Stack is Empty!!")
        return
    else:
        return s.pop(-1)  # 리스트의 맨 뒤의 값을 반환해줌
s = []
push(1)
push(2)
push(3)
print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())


"""
<Stack 을 List 로 구현시 고려할 사항>
장점 : 구현이 용이함
단점 : 리스트의 크기를 변경하는 작업은 내부적으로 큰 오버헤드 발생 작업으로 많은 시간이 소요됨

<단점을 해결하기 위한 방법>
방법1) 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
방법2) 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법
    @ 방법2)의 장점: 구현이 용이하고 데이터의 추가 삭제가 많이 일어날 경우 시간을 절약할 수 있음.
    @ 방법2)의 단점: 리스트로 구현하는 것보다 구현이 복잡함.
"""