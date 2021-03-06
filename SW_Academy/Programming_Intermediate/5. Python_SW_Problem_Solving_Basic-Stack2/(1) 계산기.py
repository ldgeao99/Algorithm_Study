"""<계산기에서 Stack의 활용>

  @ 문자열 수식 계산의 일반적인 방법
   - 문자열 수식
   - 예) A * B - C / D, (6 + 5 * (2 - 8) / 2)
  1. 중위표기법의 수식을 후위표기법으로 변경(스택이용)
   - 중위표기법 : 연산자를 피연산자의 가운데 표기하는 방법
   - 예) A + B
  2. 후위표기법의 수식을 계산(스택이용)
   - 후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법
   - 예) A B +
"""


"""<STEP1. 중위표기식의 후위표기식으로 변환 방법>
  
  @ 사람머리로 할 때
  - 문자열 수식 : A * B - C / D
  
  1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
     -> ((A * B) - (C / D))
  2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
     -> ((A B) * (C D) /) -
  3. 괄호를 제거한다.
     -> A B * C D / -

  * 이 변환방법은 사람이 손으로 처리하기는 쉽지만 프로그램으로 작성하기는 어려움. 따라서 아래의 알고리즘이 개발됨.
  
  
  @ 컴퓨터로 할 때
  -> 글로보면 복잡하니까 PPT 의 시뮬레이션과 함께보자
    
  - 문자열 수식 : A * B - C / D
  - 변환과정에서 연산자(괄호포함)는 필히 스택을 거쳐가며, 피연산자는 후위 표기법 수식에 바로 출력된다는 큰 그림을 알고 아래의 순서를 따라가보자.
  - 그리고 연산자를 스택에 넣을 때 자기보다 스택내 우선순위(ISP)가 낮은것 바로 위에만 올라갈 수 있음. 
    
  1. 입력 받은 중위표기식에서 토큰을 읽음

  2-1. 토큰이 피연산자이라면,
       토큰을 바로 출력한다.

  2-2. 토큰이 연산자 이라면,
       case1) 토큰이 스택의 top 에 저장되어있는 연산자보다 스택 내 우선순위(ISP)가 '높으면' 스택에 push 한다.
       case2) 토큰이 스택의 top 에 저장되어있는 연산자보다 스택 내 우선순위(ISP)가 '같거나 낮으면' 토큰의 우선순위가 높을 때 까지 스택에서 pop 해서 출력한 후
              토큰의 연산자를 push 한다.
       case3) 스택의 top 에 연산자가 없으면 push 한다.

  2-3. 토큰이 여는 괄호 '(' 이라면,
       스택 밖에서 우선순위가 가장 높기 때문에 스택에 바로 push 한다. (스택 내부 우선순위만 따지는게 아니라 뭔 얘기인지 모르겠음.)


  2-4. 토큰이 닫는 괄호 ')' 이라면,
       닫는 괄호 ')'를 그냥 버리고, 스택 top 에 여는 괄호 '('가 나올 때 까지 스택에서 pop 연산을 수행하면서 pop 한 연산자를 계속 출력해주는데,
       pop 해서 나온 연산자가 왼쪽 괄호도 출력하지 않고 버린다.

  5. 중위표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1.부터 다시 반복한다.

  6. 마지막으로 스택에 남아있는 연산자를 모두 pop 하여 출력한다.
     이때 스택 밖의 여는 괄호 '(' 는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음.

  7. 수식이 끝나면 종료한다.
  
  @ 위 과정에서 사용되는 연산자 우선순위
   ICP : 스택의 밖에서 연산자의 우선순위
   ISP : 스택 내에 있을 때의 연산자 우선순위

   토큰    | ISP(스택 안)  |  ICP(스택 밖)    숫자가 클수록 우선순위가 높음.
   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    )     |     -       |      -
   *, /   |     2       |      2
   +, -   |     1       |      1
    (     |     0       |      3       여는 괄호 '('의 특징 : 스택의 밖에 있을 땐 우선순위가 가장 높기 때문에 무조건 스택에 push 할 수 있지만,
                                                스택의 안에 있을 땐 우선순위가 가장 낮기 때문에 어느 연산자든 위에 쌓을 수 있다는 성질이 있다.        
"""


"""<STEP2. 후위표기법의 수식을 스택을 이용하여 계산>

1. 피연산자를 만나면 스택에 push 한다.
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop 하여 연산하고, 연산결과를 다시 스택에 push 한다.
   (주의!! 먼저 꺼낸건 뒤에, 나중에 꺼낸건 앞에 두고 연산해야한다.)
3. 수식이 끝나면, 마지막으로 스택을 pop 하여 출력한다.

* STEP1 에서는 연산자를 스택에 쌓았지만, STEP2 에서는 피연산자를 스택에 쌓아 계산한다는 차이가 있다. 
"""


"""<Python eval 내장함수>
- eval 내장함수는 문자열로 된 수식을 계산함.
- evaluation의 약자
- 스택을 두 번 사용해서 처리했던 연산을 파이썬에서 제공되는 eval() 내장 함수로 계산할 수 있음.
- 올바른 수식이 아닌 경우 SyntaxError 예외가 발생함
- eval("6+5*(2-8)/2") 

"""


########################################################################

# eval() 함수 예시
print(eval("6+5*(2-8)/2"))  # -9.0
print(eval("'hi'+'a'"))     # hia

########################################################################