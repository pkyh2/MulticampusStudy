T = int(input())

for t in range(T):
    N, M, K = map(int, input().split()) # N명, M초, K개
    time = list(map(int, input().split())); time.sort()
    bread, flag = 0, 0
    for i in range(len(time)):
        bread = (time[i] // M) * K
        if bread < i+1:     # 빵 수 < 사람 수
            print('#{} {}'.format(t+1, 'Impossible'))
            flag = 1
            break
    if flag == 0:
        print('#{} {}'.format(t+1, 'Possible'))