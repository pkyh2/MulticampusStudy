T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    board = [input().split() for _ in range(N)]
    cnt = 0

    # 가로
    for y in range(N):
        for x in range(N - K + 1):
            if x+K < N:
                if board[y][x:x+K] == list(['1']*K) and board[y][x+K] != '1':
                    cnt += 1
            else:
                if board[y][x:x+K] == list(['1']*K):
                    cnt += 1

    # for y in range(N):
    #     for x in range(N - K + 1):
    #         for z in range(K):
    #             if board[y][x+z] == '1'

    print(cnt)
    # 세로
    for x in range(N):
        for y in range(N - K + 1):
            for z in range(K):
                cnt_sub = 0
                if y+z < N:
                    if board[y+z][x] == '1' and board[y+z+1][x] != '1':
                        cnt_sub += 1
                    # elif 

    print('#{} {}'.format(t+1, cnt))
            
                
