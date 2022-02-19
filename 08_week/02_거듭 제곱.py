def power(num, sum, cnt):
    if cnt == 0:
        return sum
    else:
        sum *= num
        return power(num, sum, cnt-1)

for t in range(10):
    T = int(input())
    N, M = map(int, input().split())
    result = power(N, 1, M)
    print('#{} {}'.format(T, result))