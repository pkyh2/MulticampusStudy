T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    board = [input().split() for _ in range(N)]
    result = 0

    # 가로
    for y in range(N):
        cnt = 0
        for x in range(N):
            if board[y][x] == '1':
                cnt += 1
                if cnt == K:
                    result += 1
                elif cnt == K+1:
                    result -= 1
            else:
                cnt = 0

    for x in range(N):
        cnt = 0
        for y in range(N):
            if board[y][x] == '1':
                cnt += 1
                if cnt == K:
                    result += 1
                elif cnt == K+1:
                    result -= 1
            else:
                cnt = 0

    print('#{} {}'.format(t+1, result))