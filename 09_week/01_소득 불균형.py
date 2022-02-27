# 평균보다 작은 수의 개수를 출력

T = int(input())
for t in range(T):
    N = int(input())
    income = list(map(int, input().split()))

    avg = sum(income)/len(income)
    cnt = 0
    for i in income:
        if i <= avg:
            cnt += 1

    print('#{} {}'.format(t+1, cnt))