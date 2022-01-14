'''
N번, 2N번, ... kN번
0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
1. N = 1295 -> 1, 2, 5, 9
2. 2N = 2950 -> 0, 2, 5, 9
3. 현재까지 본 숫자 0, 1, 2, 5, 9
'''

# 풀이1(set)

T = int(input())
for t in range(T):
    num = int(input())
    result = set()
    cnt = 0
    idx = 1
    sheep = num
    while True:

        nums = list(str(sheep))
        for i in nums:
            result.add(int(i))
        if len(result) == 10:
            break
        else:
            idx += 1
            cnt += 1
            sheep = num * idx

    print('#{} {}'.format(t+1, sheep))
