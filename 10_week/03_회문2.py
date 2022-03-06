for t in range(1):
    T = int(input())
    board = [list(input()) for _ in range(100)]
    len = list(range(1, 101))
    maxLen = 0
    # 회문을 찾으면 다음 길이로 넘어감
    for y in range(100):
        for x in range(100):
            for i in len:    # 회문의 길이
                if board[y][x:i] == board[y][i-1::-1]:
                    print(i)
                    # maxLen = len(board[y][x:i])

    print()
    zipboard = list(map(list, zip(*board)))
    for y in range(100):
        for x in range(100):
            for i in len:    # 회문의 길이
                if zipboard[y][x:i] == zipboard[y][i-1::-1]:
                    print(i)
