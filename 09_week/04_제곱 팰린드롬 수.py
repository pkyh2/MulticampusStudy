import math

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    nums = list(range(a, b+1))
    cnt = 0
    for i in nums:
        if str(math.sqrt(i))[-1] == '0':     # 정수가 되야해
            tp = str(int(math.sqrt(i)))
            if tp[:] == tp[::-1]:
                drome = str(i)
                if drome[:] == drome[::-1]:
                    cnt += 1

    print('#{} {}'.format(t+1, cnt))