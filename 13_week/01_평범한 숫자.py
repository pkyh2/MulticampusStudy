T = int(input())
for t in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        if P[i] != max(P[i-1], P[i], P[i+1]) and P[i] != min(P[i-1], P[i], P[i+1]):
            cnt += 1

    print('#{} {}'.format(t+1, cnt))