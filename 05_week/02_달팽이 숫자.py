T = int(input())

for t in range(T):
    N = int(input())
    board = [[0]*N for i in range(N)]

    # 오른쪽, 아래, 왼쪽, 위
    direction = ['R', 'D', 'L', 'U']

    x, y, index = -1, 0, 0 
    cnt = 1

    for i in range(N*N):
        if direction[index] == "R":
            x += 1
            if x >= N or board[y][x] != 0:
                x -= 1
                y += 1
                index = 1
        elif direction[index] == "D":
            y += 1
            if y >= N or board[y][x] != 0:
                x -= 1
                y -= 1
                index = 2
        elif direction[index] == "L":
            x -= 1
            if x < 0 or board[y][x] != 0:
                x += 1
                y -= 1
                index  = 3
        elif direction[index] == "U":
            y -= 1
            if y < 0 or board[y][x] != 0:
                x += 1
                y += 1
                index = 0
        
        board[y][x] = cnt
        cnt += 1

    print('#{}'.format(t+1))
    for i in range(N):
        print(*board[i])