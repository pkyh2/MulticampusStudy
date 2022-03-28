def promising(x):
    for i in range(x):
        # 같은 열 체크 or 대각선 체크
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True

def n_queens(x):
    global result
    if x == N:    # 마지막 행까지 말을 놨으면, 정답 += 1
        result += 1
    else:
        for i in range(N):  # 각 열 개수 만큼 반복
            col[x] = i
            if promising(x):
                n_queens(x + 1)

T = int(input())

for t in range(T):
    N = int(input())
    col = [0] * N
    result = 0
    n_queens(0)

    print("#{} {}".format(t+1, result))