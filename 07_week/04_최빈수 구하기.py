T = int(input())

for _ in range(T):
    t = int(input())
    numbers = list(map(int, input().split()))       # 1000개의 수
    numbers.sort()                                  # 정렬
    cnt, max = 0, 0
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] == numbers[i-1]:
            cnt += 1
            if cnt > max:
                max = cnt
                result = numbers[i]
        else:
            cnt = 0
    print('#{} {}'.format(t, result))