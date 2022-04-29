T = int(input())

for t in range(T):
    boardLen = int(input())
    board = [[list(map(str, input().split()))] for _ in range(boardLen)]
    p1, p2, p3, p4 = [0, 0], [0, 0], [0, 0], [0, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                if 