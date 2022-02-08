for _ in range(10):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    sumList = []
    
    for y in range(100):
        row, col = [], []
        cross1, cross2 = [], []
        for x in range(100):
            row.append(board[y][x])
            col.append(board[x][y])
            if y == x:
                cross1.append(board[y][x])
            if x == 99 - y:
                cross2.append(board[y][99-x])
        sumList.append(max(sum(row), sum(col), sum(cross1), sum(cross2)))
    
    print('#{} {}'.format(T, max(sumList)))