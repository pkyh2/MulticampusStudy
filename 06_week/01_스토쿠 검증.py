T = int(input())
from1to9 = set(range(1, 10))

for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    row, col = [], []
    check = 1

    # 가로 세로 확인
    zipSudoku = list(map(list, zip(*sudoku)))   # 세로줄을 가로줄로 반전
    for i in range(3):
        for j in range(3):
            if set(sudoku[i*3:(i*3)+3][0:3][j]) != from1to9 or set(zipSudoku[i*3:(i*3)+3][0:3][j]) != from1to9:
                check = 0    

    # 3x3확인
    for i in range(0, 9, 3):
        for j in range(3):
            box = []
            for k in range(3):
                box += sudoku[i+k][j*3:(j*3)+3]
            if set(box) != from1to9:
                check = 0

    print('#{} {}'.format(t+1, check))


    # for i in range(9):
    #     for j in range(9):
    #         row.append(sudoku[i][j])
    #         col.append(sudoku[j][i])
    #     if from1to9 != set(row) or from1to9 != set(col):
    #         check = 0
