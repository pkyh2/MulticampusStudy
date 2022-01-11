
def searchThree(board, y, x):
    if 


T = int(input())
for t in range(T):
    N = int(input())
    board = [[x for x in input()] for _ in range(N)]

    # 2의좌표 확인
    for y in range(N):
        for x in range(N):
            if board[y][x] == 2:
                twoY, twoX = y, x

    searchThree(board, twoY, twoX)

    # 위 확인
    for i in range(1, numTwo[0]+1):
        if board[numTwo[0]-i][numTwo[1]] == 1:
            break
        elif board[numTwo[0]-i][numTwo[1]] == 3:
            print('#{} {}'.format(t+1, 1))
            break
        else:
            if numTwo == 0:
                # 우확인
            elif numTwo == 4:
                # 좌확인
            else:

            