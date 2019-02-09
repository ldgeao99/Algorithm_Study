# 주요변수에 대한 설명
# K : 한 번 충전으로 최대한 이동할 수 있는 거리
# N : 0에서 출발하여 도착해야하는 번호
# M : 설치된 충전기 개수
# bus_stops : 충전소가 설치된 곳

# Q. 전기버스

'''문제해결 팁
1. 문서에 수도코드를 가장먼저 작성하라, 커다란 Case로 나누면서
2. 조건문 혹은 조건문에 사용되는 조건을 추가할 때는 신중히해라
3. 입력예제는 코드 완성하자 마자 바로 넣어본다.
4. for문 중간에 중단점을 걸어두고 디버깅을 시행한다.
5. 간단한 문제로 수정이 가능하다면 생각을 바꿀 수 있다.
'''

T = int(input())

for test_case in range(1, T + 1):

    ############################################################
    # 입력으로부터 K, N, M 분리
    line = input()
    l = line.split()
    l = [int(item) for item in l]
    K = l[0]                      # K : 한 번 충전으로 최대한 이동할 수 있는 거리
    N = l[1]                      # N : 0에서 출발하여 도착해야하는 번호
    M = l[2]                      # M : 설치된 충전기 개수

    # 입력으로부터 버스정류장 분리
    line = input()
    l = line.split()
    bus_stops = [int(item) for item in l]

    # 한칸씩 나아갈때마다 life가 깎이는데 충전소를 만나면 다시 life가 K로 충전됨
    life = K

    # 최종 결과값
    charge_count = 0

    # 충전소가 정상설치 되어있는지
    isAvailable = True

    ############################################################

    # Case1) 충전소가 설치된 위치만 보았을 때 아예 도착이 불가능한 경우 (충전소 사이의 간격이 K보다 큰 경우 최종 결과값 = 0)

    #1) 충전소가 설치된 정류장의 리스트에 출발지인 0을 추가, 종점지인 N을 추가
    maked_stops = bus_stops
    maked_stops.append(N)
    maked_stops.insert(0, 0)

    #2) maked_stops에서  [i+1] - [i] 을 len(위의 리스트) 번 보다 적게 반복 수행하여 K	보다 큰 값이 있나 확인

    for i in range(len(maked_stops)-1):
        if ( maked_stops[i+1] - maked_stops[i] ) > K:
            isAvailable = False
            break

    ###########################################################

    # Case2) 충전소 설치가 정상적이어서 최소 충전값을 구해야 하는 경우

    # 문제를 단순화 하면 마지막 충전소(종점)까지 갈 수 있냐 없냐를 따지는 문제로 볼 수 있어서 bus_stops에 종점을 추가해준 뒤 풀이하면 좀더 단순해진다.
    maked_stops.pop(0)

    if isAvailable:
        for current_pos in range(1, N+1):
            life -= 1

            if current_pos != N:
                if current_pos in  maked_stops:
                    if (life + current_pos) < maked_stops[1]:
                        life = K
                        charge_count += 1
                    maked_stops.pop(0)

    ###########################################################

    # 최종 결과 출력

    print('#' + str(test_case) + ' ' + str(charge_count))