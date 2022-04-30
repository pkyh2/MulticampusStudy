T = int(input())

for t in range(T):
    boardLine = int(input())
    board = [[list(map(str, input().split()))] for _ in range(boardLine)]
    # p1, p2, p3, p4 = [0, 0], [0, 0], [0, 0], [0, 0]
    start = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                start.append(i)
                start.append(j)
                break
        break

    row, col = 1, 1
    for i in range(len(board) - start[i]):
        if board[start[0]][start[1]+row] == '#' and board[start[0]+col][start[1]] == '#':
            row += 1
            col += 1
            if row != col:
                print('#{} {}'.format(t+1, 'NO'))
                break
        else:
            print('#{} {}'.format(t+1, 'YES'))
            break
# 모르겠다 ㅜㅜ