T = int(input())

for t in range(T):
    n, a, b = map(int, input().split()) # n명 p구독, T구독
    ma = min(a, b)
    if n < a + b:
        mi = a + b - n
    else:
        mi = 0
    print('#{} {} {}'.format(t+1, ma, mi))