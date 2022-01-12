# 풀이1(스택)
# 입력한 방향으로 스택을 쌓아간다 막다른 길이면 스택을 pop한다.

# T = int(input())
# for t in range(T):
#     N = int(input())
#     board = [[x for x in input()] for _ in range(N)]

#     # 2의좌표 확인
#     for y in range(N):
#         for x in range(N):
#             if board[y][x] == 2:
#                 numTwo = (y, x)  # numTwo[0] == 2  numTwo[1] == 0

#     stack = [numTwo]
#     i = 1
#     top = -1
#     # 시계 방향으로 찾는다.
#     while True:
#         # 오른쪽
#         while numTwo[1]+i < N:
#             stack.append((numTwo[0], numTwo[1]+i))
#             if board[numTwo[0]][numTwo[1]+i] == 1:
#                 stack.pop()
#                 break
#             elif board[numTwo[0]][numTwo[1]+i] == 3:
#                 break
#         if stack[top]

#         # 아래
#         while numTwo[0]+i < N:
#             stack.append((numTwo[0]+i, numTwo[1]))
#             if board[numTwo[0]+i][numTwo[1]] == 1:
#                 stack.pop()
#                 break
#             elif board[numTwo[0]+i][numTwo[1]] == 3:
#                 break
#         #왼쪽
#         while numTwo[1]-i >= 0:
#             stack.append((numTwo[0], numTwo[1]-i))
#             if board[numTwo[0]][numTwo[1]-i] == 1:
#                 stack.pop()
#                 break
#             elif board[numTwo[0]][numTwo[1]-i] == 3:
#                 break
#         # 위   
#         while numTwo[0]-i >= 0:
#             stack.append((numTwo[0]-i, numTwo[1]))
#             if board[numTwo[0]-i][numTwo[1]] == 1:
#                 stack.pop()
#                 break
#             elif board[numTwo[0]-i][numTwo[1]] == 3:
#                 break
#         if board[numTwo[0]][numTwo[1]] == 3:
#             print('#{} {}'.format(t+1, 1))
#             break
# 포기포기..

# 풀이2(재귀)
def func(i, j):
    global result
    visited[i][j] = 1

    if nums[i][j] == 3:
        result = 1
        return

    if i-1 >= 0 and nums[i-1][j] != 1 and visited[i-1][j] == 0:#상
        func(i-1, j)
        if result == 1:
            return
    if j-1 >= 0 and nums[i][j-1] != 1 and visited[i][j-1] == 0:#좌
        func(i, j - 1)
        if result == 1:
            return
    if j+1 < N and nums[i][j+1] != 1 and visited[i][j+1] == 0: #우
        func(i, j + 1)
        if result == 1:
            return
    if i+1 < N and nums[i+1][j] != 1 and visited[i+1][j] == 0: #하
        func(i+1, j)
        if result == 1:
            return

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = [list(map(int,input())) for _ in range(N)]

    ###입력 완료
    start = 0
    for x in range(N):
        for y in range(N):
            if nums[x][y] == 2:
                s_x = x
                s_y = y

    result = 0
    visited = [[0]*(N) for _ in range(N)]

    func(s_x, s_y)

    print('#{} {}'.format(tc,result))