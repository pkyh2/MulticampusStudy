T = int(input())

for t in range(T):
    n, a, b = map(int, input().split())
    ma = min(a, b)
    if n < a + b:
        mi = a + b - n
    else:
        mi = 0
    print('#{} {} {}'.format(t+1, ma, mi))