'''
0 : 현재 속도 유지
1 : 가속
2 : 감속
'''
T = int(input())

for t in range(T): 

    distance, velocity = 0, 0
    N = int(input())

    for i in range(N):
        tmp = list(map(int, input().split()))   # 1, 2입력

        # 1일때
        if tmp[0] == 1:
            velocity += tmp[1]
        # 2일때
        elif tmp[0] == 2:
            # 후진은 없으니까 0이던지, 현재 속력에서 입력받은 속력값 빼던지
            velocity = max(0, velocity-tmp[1])

        # 1초마다니까 가속도가 거리다.
        distance += velocity

    print('#{} {}'.format(t+1, distance))