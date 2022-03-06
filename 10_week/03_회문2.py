def palindrome(board):
    global maxLen
    for y in range(100):
        for x in range(100):
            for i in list(range(100, 1, -1)):   # 가장 긴 회문이니까 큰 수부터
                if board[y][x:i] == board[y][i-1:x-1:-1]:
                    if maxLen < i-x:
                        maxLen = i-x

for t in range(10):
    T = int(input())
    board = [list(input()) for _ in range(100)]
    maxLen = 0
    # 가로줄
    palindrome(board)
    # 세로줄
    zipboard = list(map(list, zip(*board)))
    palindrome(zipboard)

    print("#{} {}".format(T, maxLen))